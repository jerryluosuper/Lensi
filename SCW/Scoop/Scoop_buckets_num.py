'''
Author: your name
Date: 2022-02-22 20:01:38
LastEditTime: 2022-03-06 10:12:45
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \Work\Lensi\Scoop\get_buckets.py
'''
import os
os.chdir("D:\\Scoop\\buckets")
buckets_names = os.listdir()
cnt = 0 
for i in buckets_names:
    print(i)
    dir = "D:\\Scoop\\buckets\\" + i + "\\bucket"
    os.chdir(dir)
    bucket_list = os.listdir()
    cnt = cnt + len(bucket_list)
print(cnt)