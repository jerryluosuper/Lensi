'''
Author: your name
Date: 2022-03-16 12:37:40
LastEditTime: 2022-03-16 15:38:47
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \Lensi\Lensi_.py
'''
import os
import subprocess
def Scoop_install_scoop_silence():
    scoop_install_all = open("scoop_install_all.ps1", "w")
    scoop_install_all.write("mkdir D:" + "\n" + "mkdir D:\Scoop" + "\n" + "mkdir D:\GlobalScoopApps" + "\n" + "mkdir D:\ScoopCache"+ "\n" + "Set-ExecutionPolicy RemoteSigned -scope CurrentUser;"+ "\n" + "$env:SCOOP='D:\Scoop'"+ "\n" + "[Environment]::SetEnvironmentVariable('SCOOP', $env:SCOOP, 'User')"+ "\n" + "$env:SCOOP_GLOBAL='D:\GlobalScoopApps'"+ "\n" + "[Environment]::SetEnvironmentVariable('SCOOP_GLOBAL', $env:SCOOP_GLOBAL, 'Machine')"+ "\n" + "$env:SCOOP_CACHE='D:\ScoopCache'"+ "\n" + "[Environment]::SetEnvironmentVariable('SCOOP_CACHE', $env:SCOOP_CACHE, 'Machine')"+ "\n" + "iwr -useb https://gitee.com/glsnames/scoop-installer/raw/master/bin/install.ps1 | iex"+ "\n" + "scoop config SCOOP_REPO 'https://gitee.com/glsnames/Scoop-Core'"+ "\n" + "scoop update"+ "\n" + "scoop install aria2 git sudo"+ "\n" + "scoop config aria2-split 32"+ "\n" + "scoop config aria2-max-connection-per-server 64"+ "\n" + "scoop bucket add main 'https://gitclone.com/github.com/ScoopInstaller/Main.git'"+ "\n" + "scoop bucket add extras 'https://gitee.com/xumuyao/scoop-extras.git'"+ "\n" + "scoop bucket add nonportable 'https://gitee.com/lane_swh/scoop-nonportable.git'"+ "\n" + "scoop bucket add games 'https://gitee.com/helloCodeke/scoop-games.git'"+ "\n" + "scoop bucket add java 'https://gitee.com/xumuyao/scoop-java.git'"+ "\n" + "scoop bucket add versions 'https://gitee.com/lane_swh/scoop-versions.git'"+ "\n" + "scoop bucket add scoopcn 'https://gitclone.com/github.com/scoopcn/scoopcn.git'"+ "\n" + "scoop bucket add apps 'https://gitee.com/kkzzhizhou/scoop-apps'"+ "\n" + "scoop bucket add nerd-fonts 'https://gitee.com/helloCodeke/scoop-nerd-fonts.git'"+ "\n" + "scoop bucket add scoopMain 'https://gitee.com/glsnames/scoop-main.git'"+ "\n" + "scoop update")
    scoop_install_all.close()
    os.system("powershell -File scoop_install_all.ps1 -NoProfile -WindowStyle Hidden")
def choco_install():
    choco_install = open("choco_install.ps1", "w")
    choco_install.write("mkdir D:\Choco_all" + "\n" + "$env:ChocolateyInstall='D:\Choco_all'"+ "\n"+"[Environment]::SetEnvironmentVariable('ChocolateyInstall', $env:ChocolateyInstall, 'User')"+"\n"+"Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))")
    choco_install.close()
    os.system("powershell -File choco_install.ps1 -NoProfile -WindowStyle Hidden")

check_result = subprocess.getoutput('scoop -h')
if check_result.find("不是内部或外部命令，也不是可运行的程序或批处理文件。") != -1:
    Scoop_install_scoop_silence()
else:
    print("Scoop is installed")

check_result = subprocess.getoutput('choco -h')
if check_result.find("不是内部或外部命令，也不是可运行的程序或批处理文件。") != -1:
    choco_install()
else:
    print("Choco is installed")
