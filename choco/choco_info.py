'''
Author: your name
Date: 2022-03-06 13:41:56
LastEditTime: 2022-03-15 13:50:47
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \Work\Lensi\Scoop\Scoop_search.py
'''
import subprocess
def choco_info(app_name):
    return subprocess.getoutput('choco info '+ app_name)
print(choco_info("blender"))