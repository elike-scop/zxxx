# -*- coding: utf-8 -*-
import os

# 脚本所在目录
script_dir = os.path.dirname(os.path.abspath(__file__))
# 上一层目录，1~25文件夹放在这里
BASE_DIR = os.path.dirname(script_dir)

统计 = {
    "文章数量": 0,
    "空文件": 0,
    "缺少标题": 0,
    "缺少图片": 0,
    "缺少内链": 0,
    "包含测试": 0
}


def 检查文件(路径):
    try:
        with open(
            路径,
            "r",
            encoding="utf-8"
        ) as f:
            内容 = f.read()
    except Exception:
        return

    if not 内容.strip():
        统计["空文件"] += 1
    if not 内容.lstrip().startswith("#"):
        统计["缺少标题"] += 1
    if "![" not in 内容:
        统计["缺少图片"] += 1
    if ".md)" not in 内容:
        统计["缺少内链"] += 1
    if "测试" in 内容:
        统计["包含测试"] += 1


# 遍历上一层的 1 ~ 25 文件夹
for folder_num in range(1, 26):
    folder_name = str(folder_num)
    target_folder = os.path.join(BASE_DIR, folder_name)
    if not os.path.isdir(target_folder):
        continue  # 编号文件夹不存在则跳过

    for 根目录, 目录, 文件列表 in os.walk(target_folder):
        for 文件 in 文件列表:
            if 文件.endswith(".md"):
                if 文件 in ["文章目录.md"]:
                    continue
                路径 = os.path.join(根目录, 文件)
                统计["文章数量"] += 1
                检查文件(路径)


print("==========================")
print("文章质量检查完成")
print("==========================")
for 名称, 数量 in 统计.items():
    print(
        名称,
        ":",
        数量
    )
print("==========================")
input("按回车退出")
