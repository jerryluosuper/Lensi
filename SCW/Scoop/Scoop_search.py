'''
Author: your name
Date: 2022-03-09 18:55:19
LastEditTime: 2022-03-09 18:57:56
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \Work\Lensi\Scoop_out\Scoop_search.py
'''
import subprocess
def Scoop_search(app_name):
    return subprocess.getoutput('scoop search '+ app_name)
print(Scoop_search("BitTorrent-Portable"))