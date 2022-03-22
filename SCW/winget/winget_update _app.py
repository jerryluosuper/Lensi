'''
Author: your name
Date: 2022-03-13 12:53:52
LastEditTime: 2022-03-14 11:42:52
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \Lensi\Scoop\Scoop_update.py
'''
import os


def winget_update_app_id(app_id):
    os.system("winget upgrade --silent --id --accept-source-agreement"+ app_id)
winget_update_app_id("BlenderFoundation.Blender")
