'''
Author: your name
Date: 2022-03-21 11:28:28
LastEditTime: 2022-03-21 11:28:28
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \Lensi\winget\winget_uninstall.py
'''
import os
def winget_install_apps(app_name):
    os.system("winget uninstall " + app_name)