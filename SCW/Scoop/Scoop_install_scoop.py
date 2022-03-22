'''
Author: your name
Date: 2022-02-22 20:02:02
LastEditTime: 2022-03-08 20:57:49
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \Work\Lensi\Scoop\Scoop_install.py
'''
import os
import time

print("Welcome to Scoop installer")
time_sleep = input("Type in the time you want sleep after every shell: ")
time.sleep(time_sleep)
print("Scoop helps you get the programs you need, with a minimal amount of point-and-clicking. Say goodbye to permission pop-ups. Scoop installs programs to your home directory by default. So you don’t need admin permissions to install programs, and you won’t see UAC popups every time you need to add or remove a program.(from https://scoop.sh/)")
time.sleep(time_sleep)
print("This progame will help you install Scoop from gitee mirror")
time.sleep(time_sleep)
scoop_installpath_all=input("Where to install?(default location is D:\Scoop_all,and it will also create \GlobalScoopApps \ScoopCache)")
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
    scoop_installpath_all="D:\Scoop_all"
    scoop_installpath_SCOOP="D:\Scoop_all\Scoop"
    scoop_installpath_SCOOP_GLOBAL="D:\Scoop_all\GlobalScoopApps"
    scoop_installpath_SCOOP_CACHE="D:\Scoop_all\ScoopCache"
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

