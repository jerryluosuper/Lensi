'''
Author: your name
Date: 2022-03-13 08:57:20
LastEditTime: 2022-03-14 21:10:08
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \Lensi\choco\choco_search.py
'''
import subprocess 
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
    
print(winget_search("blender"))

# winget_search("blender")
# print(subprocess.getoutput("winget search blender"))

# cmd = "winget search blender"
# search_result = open("search_result.txt", "w")
# pipe = subprocess.Popen(cmd, shell=True, stdout=search_result).stdout
# search_result.close()

# cmd = "winget search blender"
# f = open("search_result.txt","w", encoding='UTF-8')
# pipe = subprocess.Popen(cmd, shell=True, stdout=f)
# pipe.communicate()
# f.close()
# f = open("search_result.txt","r", encoding='UTF-8')
# search_result = f.read()
# print(search_result)
# f.close()