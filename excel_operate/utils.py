# coding:utf-8
import os
import pandas as pd
import chardet

# 检测文件编码
def detect_encoding(file_path):
    with open(file_path, 'rb') as f:
        raw_data = f.read()
    result = chardet.detect(raw_data)
    return result['encoding']

# 合并CSV文件
def combine_csv_files(file_list, output_dir):
    all_data = pd.DataFrame()
    for file_path in file_list:
        if file_path.endswith(".csv"):
            encoding = detect_encoding(file_path)
            df = pd.read_csv(file_path, encoding=encoding)
            all_data = pd.concat([all_data, df], ignore_index=True)

    # 确保输出目录存在 python3.2之前
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 生成输出文件路径
    csv_output_path = os.path.join(output_dir, "combined_data.csv")
    excel_output_path = os.path.join(output_dir, "combined_data.xlsx")

    # 保存合并后的数据
    all_data.to_csv(csv_output_path, index=False, encoding='utf-8-sig')
    all_data.to_excel(excel_output_path, index=False, engine='openpyxl')

    print("combine successfully, file save as {} and {}".format(csv_output_path, excel_output_path))

# 统计多个CSV文件总行数
def count_total_rows(file_list):
    total_rows = 0
    for file_path in file_list:
        if file_path.endswith(".csv"):
            encoding = detect_encoding(file_path)
            df = pd.read_csv(file_path, encoding=encoding)
            total_rows += len(df)
    return total_rows
