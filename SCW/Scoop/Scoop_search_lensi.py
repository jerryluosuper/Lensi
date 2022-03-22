'''
Author: your name
Date: 2022-03-06 13:41:56
LastEditTime: 2022-03-09 18:54:11
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \Work\Lensi\Scoop\Scoop_search.py
'''
import csv
import os
from fuzzywuzzy import process

buckets_list_install = []

def Scoop_buckets_load():
    with open("buckets_list_install.csv", "r", encoding='UTF-8') as file:
        data = csv.reader(file)
        for row in data:
            buckets_list_install.append(row)

def Scoop_install_apps(app_name):
    os.system("scoop install " + app_name)
    
Scoop_buckets_load()
name = input("请输入软件名称：")
limit_name = 3
search_list = process.extract(name,buckets_list_install, limit=limit_name)
print(search_list)
app_name_1 = search_list[0][0][0][search_list[0][0][0].find('\\'):].strip("\\")
app_name_2 = search_list[1][0][0][search_list[1][0][0].find('\\'):].strip("\\")
app_name_3 = search_list[2][0][0][search_list[2][0][0].find('\\'):].strip("\\")
app_name_search = search_list[0][0][0]
app_name_search = search_list[1][0][0]
app_name_search = search_list[2][0][0]

print("1:",app_name_1)
print("2:",app_name_2)
print("3:",app_name_3)

result = input("What to install:")
if result == "1":
    Scoop_install_apps(app_name_1)
elif result == "2":
    Scoop_install_apps(app_name_2)
elif result == "3":
    Scoop_install_apps(app_name_3)
else:
    print("What are you doing?")