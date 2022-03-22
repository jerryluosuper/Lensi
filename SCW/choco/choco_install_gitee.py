'''
Author: your name
Date: 2022-03-06 09:40:02
LastEditTime: 2022-03-14 11:47:03
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \Work\Lensi\choco\choco_install.py
'''
import os
choco_install_gitee = open("choco_install_gitee.ps1", "w")
choco_install_gitee.write("mkdir D:\Choco_all" + "\n"+ "$env:ChocolateyInstall='D:\Choco_all'"+"\n"+"[Environment]::SetEnvironmentVariable('ChocolateyInstall', $env:ChocolateyInstall, 'User')"+"\n"+"git clone 'https://gitee.com/mirrors/chocolatey.git'" +"\n"+ "cd .\chocolatey\ " + "\n" + "sudo ./setup.ps1")
choco_install_gitee.close()
os.system("powershell -File choco_install_gitee.ps1 -NoProfile -WindowStyle Hidden")