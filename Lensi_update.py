'''
Author: your name
Date: 2022-03-21 11:04:10
LastEditTime: 2022-03-21 11:26:25
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \Lensi\Lensi_update.py
'''
import os

def choco_update_all():
    os.system("choco upgrade all --yes")

def choco_update_app(app_name):
    os.system("choco upgrade " + app_name)

def choco_update():
    os.system("choco upgrade chocolatey -y")

def Scoop_update_all():
    os.system("scoop update *")

def Scoop_update_app(app_name):
    os.system("scoop update "+ app_name)

def Scoop_update():
    os.system("scoop update")

def winget_update_all():
    os.system("winget upgrade --silent --all")

def winget_update_app_id(app_id):
    os.system("winget upgrade --silent --id --accept-source-agreement"+ app_id)

def winget_update_source():
    os.system("winget source update")


def Lensi_update_app(app_name,app_source):
    if app_source == "Choco":
        choco_update_app(app_name)
    elif app_source == "Scoop":
        Scoop_update_app(app_name)
    elif app_source == "Winget":
        winget_update_app_id(app_name)

def Lensi_update_all(app_source):
    if app_source == "Choco":
        choco_update_all()
        choco_update()
    elif app_source == "Scoop":
        Scoop_update_all()
    elif app_source == "Winget":
        winget_update_all()
        winget_update_source()

def Lensi_update(app_source):
    if app_source == "Choco":
        choco_update()
    elif app_source == "Scoop":
        Scoop_update()
    elif app_source == "Winget":
        winget_update_source()