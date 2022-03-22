'''
Author: your name
Date: 2022-02-22 20:01:38
LastEditTime: 2022-03-08 20:52:12
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \Work\Lensi\Scoop\get_buckets.py
'''
import os
import json
os.chdir("D:\\Scoop_all\\Scoop\\buckets")
buckets_names = os.listdir()
for i in buckets_names:
    print(i)
    dir = "D:\\Scoop_all\\Scoop\\buckets\\" + i + "\\bucket"
    os.chdir(dir)
    bucket_list = os.listdir()
    for j in bucket_list:
        print(j)
        os.chdir(dir)
        f = open(j,"w+")
        line = f.readline()
        d = json.load(f)
        print(d)
        # TODO: 替换所有的github至镜像站
        # text.replace("https://github.com","https://ghproxy.com/https://github.com")
        # text2 = json.dumps(text)
        # print(text2)
        # f.write(text2)
        # f.close