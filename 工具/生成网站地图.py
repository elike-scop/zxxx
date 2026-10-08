# -*- coding: utf-8 -*-
import os
from datetime import datetime
from urllib.parse import quote

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)
配置文件 = os.path.join(
    BASE_DIR,
    "配置",
    "GitHub账号配置.txt"
)
输出文件 = os.path.join(
    BASE_DIR,
    "网站地图.xml"
)

def 读取配置():
    配置 = {}
    if not os.path.exists(配置文件):
        print("找不到配置文件")
        return 配置
    with open(
        配置文件,
        "r",
        encoding="utf-8"
    ) as f:
        for 行 in f:
            if "=" in 行:
                key,value = 行.strip().split(
                    "=",
                    1
                )
                配置[key]=value
    return 配置

配置 = 读取配置()
用户名 = 配置.get(
    "用户名",
    ""
)
仓库名 = 配置.get(
    "仓库名",
    ""
)
分支 = 配置.get(
    "分支",
    "main"
)

if not 用户名 or not 仓库名:
    print(
        "请填写 GitHub账号配置.txt"
    )
    input(
        "按回车退出"
    )
    exit()

GitHub地址 = (
    f"https://github.com/"
    f"{用户名}/"
    f"{仓库名}/"
    f"blob/"
    f"{分支}/"
)

文章数量 = 0
链接列表 = []

# 只遍历总目录下 1 ~ 25 文件夹
for folder_num in range(1, 26):
    folder_name = str(folder_num)
    target_folder = os.path.join(BASE_DIR, folder_name)
    if not os.path.isdir(target_folder):
        continue

    for 根目录,目录,文件列表 in os.walk(target_folder):
        for 文件 in 文件列表:
            if 文件.endswith(".md"):
                if 文件 == "文章目录.md":
                    continue
                完整路径 = os.path.join(
                    根目录,
                    文件
                )
                相对路径 = os.path.relpath(
                    完整路径,
                    BASE_DIR
                )
                相对路径 = (
                    相对路径
                    .replace("\\","/")
                )
                地址 = (
                    GitHub地址
                    +
                    quote(
                        相对路径
                    )
                )
                链接列表.append(
                    地址
                )
                文章数量 += 1

XML = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
"""
for 地址 in 链接列表:
    XML += f"""
<url>
<loc>{地址}</loc>
<lastmod>{datetime.now().strftime('%Y-%m-%d')}</lastmod>
<changefreq>weekly</changefreq>
<priority>0.8</priority>
</url>
"""
XML += """
</urlset>
"""

with open(
    输出文件,
    "w",
    encoding="utf-8"
) as f:
    f.write(XML)

print("======================")
print("网站地图生成完成")
print(
    "文章数量:",
    文章数量
)
print(
    "保存位置:",
    输出文件
)
print("======================")
input(
    "按回车退出"
)
