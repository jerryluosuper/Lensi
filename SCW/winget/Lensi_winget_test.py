'''
Author: your name
Date: 2022-03-14 11:53:00
LastEditTime: 2022-03-14 12:28:15
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \Lensi\winget\Lensi_winget.py
'''
import os
import subprocess 

def winget_install_app_id(app_id,install_locate):
    os.system("winget install --silent --location --accept-source-agreement"+ install_locate +" --id "+ app_id )
def winget_search(app_name):
    cmd = "winget search " + app_name
    f = open("search_result.txt","w", encoding='UTF-8')
    pipe = subprocess.Popen(cmd, shell=True, stdout=f)
    pipe.communicate()
    f.close()
    f = open("search_result.txt","r", encoding='UTF-8')
    search_result_list = f.readlines()[3:]
    
    search_result = []
    for i in search_result_list:
        search_result.append(i.split())
    
    for j in search_result:
        name = "".join(j[:len(j)-3])
        del(j[:len(j)-3])
        j.insert(0,name)
        # print(name)
    f.close()
    return search_result
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
def winget_update_all():
    os.system("winget upgrade --silent --all")
def winget_update_app_id(app_id):
    # subprocess.run(cmd = "winget upgrade --silent --id --accept-source-agreement"+ app_id , input="Y")
    os.system("winget upgrade --silent --id --accept-source-agreement"+ app_id)
def winget_update_source():
    os.system("winget source update")
print(winget_info_id(winget_search("blender")[0][1]))
winget_install_app_id(winget_search("blender")[3][1],"D:\APP\winget")