'''
Author: your name
Date: 2022-03-08 19:03:01
LastEditTime: 2022-03-09 19:00:05
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \Work\Lensi\Scoop\Scoop_buckets_load.py
'''
import csv
buckets_list_install = []
def Scoop_buckets_load(args):
    with open("buckets_list_install.csv", "r", encoding='UTF-8') as file:
        data = csv.reader(file)
        for row in data:
            buckets_list_install.append(row)
print(buckets_list_install)