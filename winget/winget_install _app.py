'''
Author: your name
Date: 2022-03-13 12:53:52
LastEditTime: 2022-03-14 12:06:43
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \Lensi\Scoop\Scoop_update.py
'''
import os

def winget_install_app_id(app_id,install_locate):
    os.system("winget install --silent --location --accept-source-agreement"+ install_locate +" --id "+ app_id )
winget_install_app_id("BlenderFoundation.Blender","D:\APP\winget")
