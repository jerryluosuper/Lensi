'''
Author: Lensit
Date: 2022-03-09 19:44:55
LastEditTime: 2022-03-15 09:46:54
LastEditors: Please set LastEditors
Description: Lensi_Scoop!
FilePath: \Lensi\Scoop\Lensi_scoop.py
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

def Scoop_buckets_num(Scoop_install_place):
    os.chdir( Scoop_install_place + "\\Scoop\\buckets")
    buckets_names = os.listdir()
    cnt = 0 
    for i in buckets_names:
        # print(i)
        dir = Scoop_install_place + "\\Scoop\\buckets\\" + i + "\\bucket"
        os.chdir(dir)
        bucket_list = os.listdir()
        cnt = cnt + len(bucket_list)
    return cnt

def data_write_csv(file_name, data1):
    file_csv = codecs.open(file_name,'w+','utf-8')#追加
    writer = csv.writer(file_csv, delimiter=' ', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
    for data in data1:
        list_data = [data]
        writer.writerow(list_data)
    
def Scoop_buckets_save(Scoop_install_place):
    buckets_list_install = []
    os.chdir( Scoop_install_place + "\\Scoop\\buckets")
    buckets_names = os.listdir()
    for i in buckets_names:
        # print(i)
        dir = Scoop_install_place + "\\Scoop\\buckets\\" + i + "\\bucket"
        os.chdir(dir)
        bucket_list = os.listdir()
        for j in bucket_list:
            buckets_list_install.append(i+"\\"+j.strip(".json"))
    os.chdir("D:\\快捷方式\\Desktop\\Work\\Lensi_all\\Lensi")
    data_write_csv("buckets_list_install.csv",buckets_list_install)
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
    # app_name_detail = app_json["shortcuts"][0][1]
    # app_version = app_json["version"]
    # app_description = app_json["description"]
    # app_homepage = app_json["homepage"]
    return app_detail

def Scoop_info(app_name):
    return subprocess.getoutput('scoop info '+ app_name)

def Scoop_install_apps(app_name):
    os.system("scoop install " + app_name)
def Scoop_install_scoop_silence(Scoop_install_place):
    scoop_install_all = open("scoop_install_all.ps1", "w")
    scoop_install_all.write("mkdir  " + Scoop_install_place  + "\n" + "mkdir  " + Scoop_install_place + "\Scoop" + "\n" + "mkdir  " + Scoop_install_place + "\GlobalScoopApps" + "\n" + "mkdir  " + Scoop_install_place + "\ScoopCache"+ "\n" + "Set-ExecutionPolicy RemoteSigned -scope CurrentUser;"+ "\n" + "$env:SCOOP=' " + Scoop_install_place + "\Scoop'"+ "\n" + "[Environment]::SetEnvironmentVariable('SCOOP', $env:SCOOP, 'User')"+ "\n" + "$env:SCOOP_GLOBAL=' " + Scoop_install_place + "\GlobalScoopApps'"+ "\n" + "[Environment]::SetEnvironmentVariable('SCOOP_GLOBAL', $env:SCOOP_GLOBAL, 'Machine')"+ "\n" + "$env:SCOOP_CACHE=' " + Scoop_install_place + "\ScoopCache'"+ "\n" + "[Environment]::SetEnvironmentVariable('SCOOP_CACHE', $env:SCOOP_CACHE, 'Machine')"+ "\n" + "iwr -useb https://gitee.com/glsnames/scoop-installer/raw/master/bin/install.ps1 | iex"+ "\n" + "scoop config SCOOP_REPO 'https://gitee.com/glsnames/Scoop-Core'"+ "\n" + "scoop update"+ "\n" + "scoop install aria2 git sudo"+ "\n" + "scoop config aria2-split 32"+ "\n" + "scoop config aria2-max-connection-per-server 64"+ "\n" + "scoop bucket add main 'https://gitclone.com/github.com/ScoopInstaller/Main.git'"+ "\n" + "scoop bucket add extras 'https://gitee.com/xumuyao/scoop-extras.git'"+ "\n" + "scoop bucket add nonportable 'https://gitee.com/lane_swh/scoop-nonportable.git'"+ "\n" + "scoop bucket add games 'https://gitee.com/helloCodeke/scoop-games.git'"+ "\n" + "scoop bucket add java 'https://gitee.com/xumuyao/scoop-java.git'"+ "\n" + "scoop bucket add versions 'https://gitee.com/lane_swh/scoop-versions.git'"+ "\n" + "scoop bucket add scoopcn 'https://gitclone.com/github.com/scoopcn/scoopcn.git'"+ "\n" + "scoop bucket add apps 'https://gitee.com/kkzzhizhou/scoop-apps'"+ "\n" + "scoop bucket add nerd-fonts 'https://gitee.com/helloCodeke/scoop-nerd-fonts.git'"+ "\n" + "scoop bucket add scoopMain 'https://gitee.com/glsnames/scoop-main.git'"+ "\n" + "scoop update")
    scoop_install_all.close()
    os.system("powershell -File scoop_install_all.ps1 -NoProfile -WindowStyle Hidden")

def Scoop_install_scoop():
    print("Welcome to Scoop installer")
    time_sleep = input("Type in the time you want sleep after every shell: ")
    time.sleep(time_sleep)
    print("Scoop helps you get the programs you need, with a minimal amount of point-and-clicking. Say goodbye to permission pop-ups. Scoop installs programs to your home directory by default. So you don’t need admin permissions to install programs, and you won’t see UAC popups every time you need to add or remove a program.(from https://scoop.sh/)")
    time.sleep(time_sleep)
    print("This progame will help you install Scoop from gitee mirror")
    time.sleep(time_sleep)
    scoop_installpath_all=input("Where to install?(default location is D:\APP,and it will also create \GlobalScoopApps \ScoopCache)")
    scoop_installpath_SCOOP=scoop_installpath_all+"\Scoop"
    scoop_installpath_SCOOP_GLOBAL=scoop_installpath_all+"\GlobalScoopApps"
    scoop_installpath_SCOOP_CACHE=scoop_installpath_all+"\ScoopCache"
    try:
        os.mkdir(scoop_installpath_all)
        print("Has create",scoop_installpath_all)
        os.mkdir(scoop_installpath_SCOOP)
        print("Has create",scoop_installpath_SCOOP)
        os.mkdir(scoop_installpath_SCOOP_CACHE)
        print("Has create",scoop_installpath_SCOOP_CACHE)
        os.mkdir(scoop_installpath_SCOOP_GLOBAL)
        print("Has create",scoop_installpath_SCOOP_GLOBAL)
    except:
        scoop_installpath_all="D:\APP"
        scoop_installpath_SCOOP="D:\APP\Scoop"
        scoop_installpath_SCOOP_GLOBAL="D:\APP\GlobalScoopApps"
        scoop_installpath_SCOOP_CACHE="D:\APP\ScoopCache"
        os.mkdir(scoop_installpath_all)
        print("Has create",scoop_installpath_all)
        time.sleep(time_sleep)
        os.mkdir(scoop_installpath_SCOOP)
        print("Has create",scoop_installpath_SCOOP)
        time.sleep(time_sleep)
        os.mkdir(scoop_installpath_SCOOP_CACHE)
        print("Has create",scoop_installpath_SCOOP_CACHE)
        time.sleep(time_sleep)
        os.mkdir(scoop_installpath_SCOOP_GLOBAL)
        print("Has create",scoop_installpath_SCOOP_GLOBAL)

    scoop_setpath_text = "$env:SCOOP='" + scoop_installpath_SCOOP + "'" + "\n"+"[Environment]::SetEnvironmentVariable('SCOOP', $env:SCOOP, 'User')" + "\n" + "$env:SCOOP_GLOBAL='" + scoop_installpath_SCOOP_GLOBAL +"\n"+ "'[Environment]::SetEnvironmentVariable('SCOOP_GLOBAL', $env:SCOOP_GLOBAL, 'Machine')" + "\n" + "$env:SCOOP_CACHE='" + scoop_installpath_SCOOP_CACHE + "/n" +"'[Environment]::SetEnvironmentVariable('SCOOP_CACHE', $env:SCOOP_CACHE, 'Machine')"
    os.system("powershell -Command " + scoop_setpath_text+ "-NoProfile -WindowStyle Hidden")
    print("Has already set location")
    time.sleep(time_sleep)
    print("It is time to download and install!")

    scoop_install = open("scoop_install.ps1", "w")
    scoop_install.write("iwr -useb https://gitee.com/glsnames/scoop-installer/raw/master/bin/install.ps1 | iex")
    scoop_install.close()
    os.system("powershell -File scoop_install.ps1 -NoProfile -WindowStyle Hidden")
    os.remove("scoop_install.ps1")
    print("Has installed successfully!")
    time.sleep(time_sleep)

    print("Now to set config SCOOP_REPO")
    scoop_config_text = "scoop config SCOOP_REPO 'https://gitee.com/glsnames/Scoop-Core'" + "\n" + "scoop update"
    os.system(scoop_config_text)

    time.sleep(time_sleep)
    print("Install some basic apps")
    os.system("scoop install aria2 git sudo ")

    time.sleep(time_sleep)
    scoop_buckets = open("scoop_buckets.ps1", "w")
    scoop_buckets.write("scoop bucket add main 'https://gitclone.com/github.com/ScoopInstaller/Main.git' " + "\n" + "scoop bucket add extras 'https://gitee.com/xumuyao/scoop-extras.git'"+ "\n" + "scoop bucket add nonportable 'https://gitee.com/lane_swh/scoop-nonportable.git'"+ "\n" + "scoop bucket add games 'https://gitee.com/helloCodeke/scoop-games.git'"+ "\n" + "scoop bucket add java 'https://gitee.com/xumuyao/scoop-java.git'"+ "\n" + "scoop bucket add versions 'https://gitee.com/lane_swh/scoop-versions.git'"+ "\n" + "scoop bucket add scoopcn 'https://gitclone.com/github.com/scoopcn/scoopcn.git'"+ "\n" + "scoop bucket add apps 'https://gitee.com/kkzzhizhou/scoop-apps'"+ "\n" + "scoop bucket add nerd-fonts 'https://gitee.com/helloCodeke/scoop-nerd-fonts.git'"+ "\n" + "scoop bucket add scoopMain 'https://gitee.com/glsnames/scoop-main.git'"+ "\n" + "scoop update")
    scoop_buckets.close()
    print("Add some basic buckets")
    os.system("powershell -File scoop_buckets.ps1 -NoProfile -WindowStyle Hidden")
    os.remove("scoop_install.ps1")

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

buckets_list_install = []
print(Scoop_buckets_num("D:\\"))
Scoop_buckets_save("D:\\")
buckets_list_install = Scoop_buckets_load()
search_result = Scoop_search_lensi("geek",buckets_list_install)
print(search_result)
print(Scoop_search_info(search_result[0][1],"D:\\"))
# Scoop_install_apps(search_result[1][0])