'''
Author: your name
Date: 2022-03-06 13:41:56
LastEditTime: 2022-03-14 11:04:20
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \Work\Lensi\Scoop\Scoop_search.py
'''
import subprocess
def winget_info_id(app_id):
    cmd = "winget show --id " + app_id
    f = open("info_result.txt","w", encoding='UTF-8')
    pipe = subprocess.Popen(cmd, shell=True, stdout=f)
    pipe.communicate()
    f.close()
    f = open("info_result.txt","r", encoding='UTF-8')
    info_result = f.read()
    f.close()
    return info_result
print(winget_info_id("BlenderFoundation.Blender"))