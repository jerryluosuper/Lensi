'''
Author: your name
Date: 2022-02-22 20:01:38
LastEditTime: 2022-03-15 13:19:09
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \Work\Lensi\Scoop\get_buckets.py
'''
import os
import csv
import codecs

def data_write_csv(file_name, data1):#file_name为写入CSV文件的路径，datas为要写入数据列表
    file_csv = codecs.open(file_name,'w+','utf-8')#追加
    writer = csv.writer(file_csv, delimiter=' ', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
    for data in data1:
        list_data = [data]
        writer.writerow(list_data)
    print("保存文件成功，处理结束")

os.chdir("D:\\Scoop\\buckets")
buckets_names = os.listdir()
buckets_list_install = []  
# buckets_list_name = []  
for i in buckets_names:
    print(i)
    dir = "D:\\Scoop\\buckets\\" + i + "\\bucket"
    os.chdir(dir)
    bucket_list = os.listdir()
    for j in bucket_list:
        buckets_list_install.append(i+"\\"+j.strip(".json"))
        # buckets_list_name.append(j.strip(".json"))
os.chdir("D:\\快捷方式\\Desktop\\Work\\Lensi_all\\Lensi")
# data_write_csv("bucket_list_name.csv",buckets_list_name)
print(buckets_list_install)
data_write_csv("buckets_list_install.csv",buckets_list_install)