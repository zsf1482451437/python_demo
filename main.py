# coding:utf-8
import os

from excel_operate.utils import combine_csv_files
from excel_operate.utils import count_total_rows

# 指定文件列表
directory = "./excel_operate/input"

# 指定输出目录
output_dir = "./excel_operate/output"

file_list = [os.path.join(directory, filename) for filename in os.listdir(directory)]
# 合并
combine_csv_files(file_list, output_dir)
# 统计总行数
# total_rows = count_total_rows(file_list)
# print("Total rows: {}".format(total_rows))

