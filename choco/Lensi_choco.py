'''
Author: your name
Date: 2022-03-13 13:51:43
LastEditTime: 2022-03-14 11:52:23
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \Lensi\choco\Lensi_choco.py
'''
import subprocess
import os
def choco_info(app_name):
    return subprocess.getoutput('choco info '+ app_name)

def choco_update_all():
    os.system("choco upgrade all --yes")

def choco_update_app(app_name):
    os.system("choco upgrade " + app_name)

def choco_install_gitee():
    choco_install_gitee = open("choco_install_gitee.ps1", "w")
    choco_install_gitee.write("mkdir D:\Choco_all" + "\n"+ "$env:ChocolateyInstall='D:\Choco_all'"+"\n"+"[Environment]::SetEnvironmentVariable('ChocolateyInstall', $env:ChocolateyInstall, 'User')"+"\n"+"git clone 'https://gitee.com/mirrors/chocolatey.git'" +"\n"+ "cd .\chocolatey\ " + "\n" + "sudo ./setup.ps1")
    choco_install_gitee.close()
    os.system("powershell -File choco_install_gitee.ps1 -NoProfile -WindowStyle Hidden")

def choco_install():
    choco_install = open("choco_install.ps1", "w")
    choco_install.write("mkdir D:\Choco_all" + "\n" + "$env:ChocolateyInstall='D:\Choco_all'"+ "\n"+"[Environment]::SetEnvironmentVariable('ChocolateyInstall', $env:ChocolateyInstall, 'User')"+"\n"+"Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))")
    choco_install.close()
    os.system("powershell -File choco_install.ps1 -NoProfile -WindowStyle Hidden")

def choco_search(app_name):
    search_result = subprocess.getoutput('choco search '+ app_name + ' --limitoutput ')
    # print(search_result)
    search_list = []
    search_list_all = search_result.split()
    for name in search_list_all:
        search_list.append(name.split("|")[0])
    return search_list

def choco_update():
    os.system("choco upgrade chocolatey -y")