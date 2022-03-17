'''
Author: your name
Date: 2022-03-08 19:53:42
LastEditTime: 2022-03-08 20:53:10
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \Work\Lensi\Scoop\Scoop_install_apps.py
'''
import os
def Scoop_install_apps(app_name):
    os.system("scoop install " + app_name)