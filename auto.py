import os
import subprocess
import re

# 创建失败文件夹
os.makedirs("failed", exist_ok=True)

# 打开total.txt文件
with open("total.txt", "w") as total_file:
    # 遍历当前目录下的所有apk文件
    for file in os.listdir():
        if file.endswith(".apk"):
            # 生成随机字符串
            random_string = os.urandom(8).hex()
            # 重命名为随机字符串
            os.rename(file, random_string + ".apk")

            try:
                # 使用aapt命令获取apk文件的应用名称和版本号
                output = subprocess.check_output(["aapt", "dump", "badging", random_string + ".apk"], stderr=subprocess.STDOUT).decode("utf-8")
                app_name = re.search(r"application-label:'([^']+)'", output)
                app_version = re.search(r"versionName='([^']+)'", output)

                if app_name and app_version:
                    app_name = app_name.group(1)
                    app_version = app_version.group(1)
                    # 去除特殊字符
                    app_name = re.sub(r'[\\/:*?"<>|]', '', app_name)
                    # 重命名为 应用名称-版本 格式
                    new_name = f"{app_name}-{app_version}.apk"
                    os.rename(random_string + ".apk", new_name)
                    print(f"重命名 {file} 为 {new_name}")
                    # 输出重命名成功的文件名到total.txt
                    total_file.write(new_name + "\n")
                else:
                    print(f"无法获取 {file} 的应用名称或版本号，移动到失败文件夹")
                    os.rename(random_string + ".apk", os.path.join("failed", random_string + ".apk"))
            except subprocess.CalledProcessError as e:
                print(f"解析 {file} 时出错: {e.output.decode('utf-8').strip()}")
                os.rename(random_string + ".apk", os.path.join("failed", random_string + ".apk"))
