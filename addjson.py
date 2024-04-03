import os
import json

def add_apk_names_to_json(json_path):
    # 检查 JSON 文件是否存在
    if not os.path.exists(json_path):
        print("原始 JSON 文件不存在，请重新输入路径。")
        return
    
    # 获取当前目录下所有的 APK 文件名（不带后缀名）
    apk_files = [os.path.splitext(filename)[0] for filename in os.listdir() if filename.endswith('.apk')]

    # 读取原始 JSON 文件内容
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 将 APK 文件名添加到 JSON 数据中
    for i, apk_name in enumerate(apk_files, start=1):
        data[f'n{i}'] = apk_name

    # 生成新的 JSON 文件
    new_json_path = os.path.splitext(json_path)[0] + '_new.json'
    with open(new_json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    print("应用名称已成功添加到 JSON 文件中。")

if __name__ == "__main__":
    # 用户输入原始 JSON 文件路径
    json_path = input("请输入原始 JSON 文件的路径: ").strip()
    add_apk_names_to_json(json_path)
