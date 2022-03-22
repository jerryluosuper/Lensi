'''
Author: your name
Date: 2022-03-06 13:41:56
LastEditTime: 2022-03-09 18:57:43
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \Work\Lensi\Scoop\Scoop_search.py
'''
import subprocess
def Scoop_info(app_name):
    return subprocess.getoutput('scoop info '+ app_name)
# print(Scoop_info("BitTorrent-Portable"))