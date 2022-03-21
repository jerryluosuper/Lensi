'''
Author: your name
Date: 2022-03-21 11:18:19
LastEditTime: 2022-03-21 11:33:54
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \Lensi\Lensi_uninstall.py
'''
import os
def Scoop_uninstall_app(app_name):
    os.system("scoop uninstall " + app_name)

def choco_uninstall_app(app_name):
    os.system("choco uninstall " + app_name)

def winget_uninstall_app(app_name):
    os.system("winget uninstall " + app_name)

def Lensi_uninstall(app_name,app_source):
    if app_source == "Choco":
        choco_uninstall_app(app_name)
    elif app_source == "Scoop":
        Scoop_uninstall_app(app_name)
    elif app_source == "Winget":
        winget_uninstall_app(app_name)
