# -*- coding: utf-8 -*-
import os
# 脚本在工具文件夹，向上退一层，定位到【SEO工具一键完整版】总目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
替换文件 = os.path.join(BASE_DIR, "配置", "替换内容.txt")
print("总目录BASE_DIR：", BASE_DIR)
print("读取txt路径：",替换文件)
print("文件是否存在：", os.path.exists(替换文件))
if not os.path.exists(替换文件):
    print("找不到 配置/替换内容.txt")
    input("按回车退出")
    exit()
with open(替换文件, "r", encoding="utf-8") as f:
    新内容 = f.read()

扫描数量 = 0
替换数量 = 0

print("\n开始扫描 1~25 文件夹")
# 遍历总目录下 1 ~ 25 的文件夹
for folder_num in range(1, 26):
    folder_name = str(folder_num)
    target_folder = os.path.join(BASE_DIR, folder_name)
    if not os.path.isdir(target_folder):
        print(f"跳过不存在文件夹：{folder_name}")
        continue

    for 根目录,目录,文件列表 in os.walk(target_folder):
        for 文件 in 文件列表:
            if 文件.endswith(".md"):
                扫描数量 += 1
                路径 = os.path.join(根目录, 文件)
                print(f"找到md：{路径}")
                with open(路径, "r", encoding="utf-8") as f:
                    内容 = f.read()
                if "测试" in 内容:
                    print(f">>> 执行替换：{文件}")
                    新文章 = 内容.replace("测试", 新内容)
                    with open(路径, "w", encoding="utf-8") as f:
                        f.write(新文章)
                    替换数量 += 1

print("\n==========================")
print("批量替换完成")
print("==========================")
print("扫描文件:", 扫描数量)
print("成功替换:", 替换数量)
print("==========================")
input("按回车退出")
