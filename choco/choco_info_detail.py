'''
Author: your name
Date: 2022-03-06 13:41:56
LastEditTime: 2022-03-15 14:34:44
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \Work\Lensi\Scoop\Scoop_search.py
'''
import subprocess
def choco_info_detail(app_name):
    app_detail = subprocess.getoutput('choco info '+ app_name)
    app_detail_url = app_detail[int(app_detail.find('Software Site:')):int(app_detail.find("Software License: ",app_detail.find("Software Site:")))].strip("Software Site:")
    # print("url:",app_detail_url)
    return app_detail_url
print(choco_info_detail("blender"))