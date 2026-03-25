#!/usr/bin/env python3
import re
import requests
import json
import time
import os

# 读取markdown文件
with open('全网最详细的Codex教程.md', 'r', encoding='utf-8') as f:
    content = f.read()

# 提取所有微信图片链接
pattern = r'https://mmbiz\.qpic\.cn[^)#]+'
urls = list(set(re.findall(pattern, content)))
urls.sort()

print(f"找到 {len(urls)} 张图片")

# 图床配置
UPLOAD_API = "https://upload.maynor1024.live/upload"
URL_PREFIX = "https://upload.maynor1024.live"

# 存储新旧URL映射
url_mapping = {}

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
}

for i, old_url in enumerate(urls):
    print(f"\n处理第 {i+1}/{len(urls)} 张图片...")
    
    try:
        # 下载图片
        print(f"下载: {old_url[:60]}...")
        resp = requests.get(old_url, headers=headers, timeout=30)
        
        if resp.status_code != 200:
            print(f"  下载失败: HTTP {resp.status_code}")
            continue
        
        # 获取图片内容
        img_data = resp.content
        
        # 上传到图床
        files = {'file': ('image.png', img_data, 'image/png')}
        upload_resp = requests.post(UPLOAD_API, files=files, timeout=30)
        
        if upload_resp.status_code == 200:
            result = upload_resp.json()
            # JSON路径: 0.src
            if isinstance(result, list) and len(result) > 0:
                img_path = result[0].get('src', '')
            elif isinstance(result, dict):
                img_path = result.get('src', '') or result.get('url', '')
            else:
                img_path = ''
            
            if img_path:
                # 构建完整URL
                if img_path.startswith('http'):
                    new_url = img_path
                else:
                    new_url = URL_PREFIX + ('/' if not img_path.startswith('/') else '') + img_path
                
                url_mapping[old_url] = new_url
                print(f"  ✓ 成功: {new_url}")
            else:
                print(f"  ✗ 上传返回格式错误: {result}")
        else:
            print(f"  ✗ 上传失败: HTTP {upload_resp.status_code}")
            print(f"     响应: {upload_resp.text[:200]}")
        
        # 避免请求过快
        time.sleep(0.5)
        
    except Exception as e:
        print(f"  ✗ 错误: {e}")
        continue

print(f"\n\n===== 上传完成 =====")
print(f"成功: {len(url_mapping)}/{len(urls)} 张")

# 保存映射关系
with open('url_mapping.json', 'w', encoding='utf-8') as f:
    json.dump(url_mapping, f, ensure_ascii=False, indent=2)
print("\n映射已保存到 url_mapping.json")

# 替换Markdown中的链接
new_content = content
for old_url, new_url in url_mapping.items():
    new_content = new_content.replace(old_url, new_url)

# 保存新文件
with open('全网最详细的Codex教程_新.md', 'w', encoding='utf-8') as f:
    f.write(new_content)
print("新文件已保存到: 全网最详细的Codex教程_新.md")

# 打印映射
print("\n===== URL映射 =====")
for old, new in url_mapping.items():
    print(f"{old[:50]}... -> {new}")
