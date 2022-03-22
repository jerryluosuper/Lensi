'''
Author: your name
Date: 2022-03-20 13:18:04
LastEditTime: 2022-03-21 11:19:06
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \Lensi\Lensi_install.py
'''
import os
from urllib.request import urlretrieve
def choco_install_app(app_name):
    os.system("choco install"+app_name)

def Scoop_install_app(app_name):
    os.system("scoop install " + app_name)

def winget_install_app_id(app_id):
    os.system("winget install --silent --accept-source-agreement --id "+ app_id)

def web_install_normal(web_download_url):
    web_download_name = web_download_url[web_download_url.rfind("/"):]
    web_download_name = web_download_name.strip("/")
    print("Downloading to",web_download_name)
    urlretrieve(web_download_url,web_download_name)
    os.system(web_download_name)
    print("下载完成")

def web_install_hippo(web_download_url):
    web_download_name = web_download_url[web_download_url.rfind("="):]
    web_download_name = web_download_name.strip("=")
    print("Downloading to",web_download_name)
    urlretrieve(web_download_url,web_download_name)
    os.system(web_download_name)
    print("下载完成")


def Lensi_install(app_name,app_source):
    if app_source == "Choco":
        choco_install_app(app_name)
    elif app_source == "Scoop":
        Scoop_install_app(app_name)
    elif app_source == "Winget":
        winget_install_app_id(app_name)
    elif app_source == "qq" or app_source == "360":
        web_install_normal(app_name)
    elif app_source == "Hippo":
        web_install_hippo(app_name)