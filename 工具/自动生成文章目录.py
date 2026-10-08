# -*- coding: utf-8 -*-
import os
# 当前项目目录
BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)
输出文件 = os.path.join(
    BASE_DIR,
    "文章目录.md"
)

内容 = "# 文章目录\n\n"
数量 = 0

# 遍历总目录下 1 ~ 25 的文件夹
for folder_num in range(1, 26):
    分类名称 = str(folder_num)
    分类路径 = os.path.join(BASE_DIR, 分类名称)
    if not os.path.isdir(分类路径):
        continue

    内容 += f"## {分类名称}\n\n"
    # 获取该文件夹下文件并排序
    文件列表 = sorted(os.listdir(分类路径))
    for 文件 in 文件列表:
        文件完整路径 = os.path.join(分类路径, 文件)
        if os.path.isfile(文件完整路径) and 文件.endswith(".md"):
            # 生成相对链接
            相对地址 = f"{分类名称}/{文件}"
            内容 += (
                f"- [{文件}]"
                f"({相对地址})\n"
            )
            数量 += 1
    内容 += "\n"

with open(
    输出文件,
    "w",
    encoding="utf-8"
) as f:
    f.write(内容)

print("===================")
print("文章目录生成完成")
print("文章数量:",数量)
print("生成位置:")
print(输出文件)
print("===================")
input("按回车退出")
