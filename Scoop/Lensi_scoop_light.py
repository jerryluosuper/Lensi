'''
Author: your name
Date: 2022-03-12 09:53:13
LastEditTime: 2022-03-12 10:05:54
LastEditors: your name
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \Lensi\Scoop\Lensi_scoop_light.py
'''
import csv
import subprocess
import os
import codecs
import json
import time
from fuzzywuzzy import process

def Scoop_buckets_load():
    buckets_list_install = []
    with open("buckets_list_install.csv", "r", encoding='UTF-8') as file:
        data = csv.reader(file)
        for row in data:
            row_l = [row]
            buckets_list_install.append(row_l)
    return buckets_list_install
    
def Scoop_buckets_save(Scoop_install_place):
    buckets_list_install = []
    os.chdir("D:\\App\\Scoop\\buckets")
    buckets_names = os.listdir()
    for i in buckets_names:
        # print(i)
        dir = Scoop_install_place + "\\Scoop\\buckets\\" + i + "\\bucket"
        os.chdir(dir)
        bucket_list = os.listdir()
        for j in bucket_list:
            buckets_list_install.append(i+"\\"+j.strip(".json"))
    os.chdir("D:\\快捷方式\\Desktop\\Work\\Lensi")
    file_csv = codecs.open("buckets_list_install.csv",'w+','utf-8')#追加
    writer = csv.writer(file_csv, delimiter=' ', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
    for data in buckets_list_install:
        list_data = [data]
        writer.writerow(list_data)

def Scoop_search_info(app_name_install,Scoop_install_place):
    app_json = []
    app_name_json = Scoop_install_place + "\\Scoop\\buckets\\" + app_name_install[:app_name_install.find('\\')] + "\\bucket\\" + app_name_install[app_name_install.find('\\'):].strip("\\") + ".json"
    with open(app_name_json, 'r') as f:
        app_json = json.load(f)
    app_detail = [app_json["shortcuts"][0][1],app_json["version"],app_json["description"],app_json["homepage"]]
    return app_detail

def Scoop_info(app_name):
    return subprocess.getoutput('scoop info '+ app_name)

def Scoop_install_apps(app_name):
    os.system("scoop install " + app_name)
def Scoop_install_scoop_silence():
    scoop_install_all = open("scoop_install_all.ps1", "w")
    scoop_install_all.write("mkdir D:\APP" + "\n" + "mkdir D:\APP\Scoop" + "\n" + "mkdir D:\APP\GlobalScoopApps" + "\n" + "mkdir D:\APP\ScoopCache"+ "\n" + "Set-ExecutionPolicy RemoteSigned -scope CurrentUser;"+ "\n" + "$env:SCOOP='D:\APP\Scoop'"+ "\n" + "[Environment]::SetEnvironmentVariable('SCOOP', $env:SCOOP, 'User')"+ "\n" + "$env:SCOOP_GLOBAL='D:\APP\GlobalScoopApps'"+ "\n" + "[Environment]::SetEnvironmentVariable('SCOOP_GLOBAL', $env:SCOOP_GLOBAL, 'Machine')"+ "\n" + "$env:SCOOP_CACHE='D:\APP\ScoopCache'"+ "\n" + "[Environment]::SetEnvironmentVariable('SCOOP_CACHE', $env:SCOOP_CACHE, 'Machine')"+ "\n" + "iwr -useb https://gitee.com/glsnames/scoop-installer/raw/master/bin/install.ps1 | iex"+ "\n" + "scoop config SCOOP_REPO 'https://gitee.com/glsnames/Scoop-Core'"+ "\n" + "scoop update"+ "\n" + "scoop install aria2 git sudo"+ "\n" + "scoop config aria2-split 32"+ "\n" + "scoop config aria2-max-connection-per-server 64"+ "\n" + "scoop bucket add main 'https://gitclone.com/github.com/ScoopInstaller/Main.git'"+ "\n" + "scoop bucket add extras 'https://gitee.com/xumuyao/scoop-extras.git'"+ "\n" + "scoop bucket add nonportable 'https://gitee.com/lane_swh/scoop-nonportable.git'"+ "\n" + "scoop bucket add games 'https://gitee.com/helloCodeke/scoop-games.git'"+ "\n" + "scoop bucket add java 'https://gitee.com/xumuyao/scoop-java.git'"+ "\n" + "scoop bucket add versions 'https://gitee.com/lane_swh/scoop-versions.git'"+ "\n" + "scoop bucket add scoopcn 'https://gitclone.com/github.com/scoopcn/scoopcn.git'"+ "\n" + "scoop bucket add apps 'https://gitee.com/kkzzhizhou/scoop-apps'"+ "\n" + "scoop bucket add nerd-fonts 'https://gitee.com/helloCodeke/scoop-nerd-fonts.git'"+ "\n" + "scoop bucket add scoopMain 'https://gitee.com/glsnames/scoop-main.git'"+ "\n" + "scoop update")
    scoop_install_all.close()
    os.system("powershell -File scoop_install_all.ps1 -NoProfile -WindowStyle Hidden")

def Scoop_search_lensi(name,buckets_list_install):
    search_list = process.extract(name,buckets_list_install, limit=3)
    # print(search_list)
    app_name_1 = search_list[0][0][0][0][search_list[0][0][0][0].find('\\'):].strip("\\")
    app_name_2 = search_list[1][0][0][0][search_list[1][0][0][0].find('\\'):].strip("\\")
    app_name_3 = search_list[2][0][0][0][search_list[2][0][0][0].find('\\'):].strip("\\")
    app_name_search1 = search_list[0][0][0][0]
    app_name_search2 = search_list[1][0][0][0]
    app_name_search3 = search_list[2][0][0][0]
    app_name_all = [[app_name_1,app_name_search1],[app_name_2,app_name_search2],[app_name_3,app_name_search3]]
    return app_name_all

def Scoop_search(app_name):
    return subprocess.getoutput('scoop search '+ app_name)

def Scoop_uninstall_apps(app_name):
    os.system("scoop uninstall " + app_name)

def Scoop_update():
    os.system("scoop update")