'''
Author: your name
Date: 2022-03-13 08:57:20
LastEditTime: 2022-03-13 10:02:30
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \Lensi\choco\choco_search.py
'''
import subprocess
def choco_search(app_name):
    search_result = subprocess.getoutput('choco search '+ app_name + ' --limitoutput ')
    # print(search_result)
    search_list = []
    search_list_all = search_result.split()
    for name in search_list_all:
        search_list.append(name.split("|")[0])
    return search_list
print(choco_search("blender"))