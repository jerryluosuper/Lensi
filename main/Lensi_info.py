'''
Author: your name
Date: 2022-03-21 11:09:43
LastEditTime: 2022-03-21 11:26:02
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \Lensi\Lensi_info.py
'''
import json
import subprocess
from urllib import request
from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup

def choco_info(app_name):
    return subprocess.getoutput('choco info '+ app_name)

def Scoop_search_info(app_name_install):
    app_json = []
    app_name_json = "D:\\App\\Scoop\\buckets\\" + app_name_install[:app_name_install.find('\\')] + "\\bucket\\" + app_name_install[app_name_install.find('\\'):].strip("\\") + ".json"
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

def winget_info_id(app_id):
    cmd = "winget show --id " + app_id
    pipe = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,universal_newlines=True).stdout.read()
    return pipe

def web_qq_info(qq_id):
    headers = {'User-Agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763'}
    qq_id_int = int(qq_id)
    # print(qq_id)
    qq_info_url = 'https://pc.qq.com/detail/'+ str(qq_id_int%20) + '/detail_' + qq_id + '.html' 
    # print(qq_info_url)
    qq_info_html_req = request.Request(url=qq_info_url,headers=headers)
    qq_info_html = urlopen(qq_info_html_req)
    qq_info_soup = BeautifulSoup(qq_info_html.read(),"html.parser")
    try:
        qq_info_data = qq_info_soup.select('body > div.category-wrap > div.container_16 > div > div > div.detail-wrap > div.detail-desc > div.cont-content > p:nth-child(1)')
        for item in qq_info_data:
            qq_info_main = item.get_text()
        qq_info_data_home = qq_info_soup.select('body > div.category-wrap > div.container_16 > div > div > div.detail-wrap > div.detail-desc > div.cont-content > p:nth-child(3) > a')
        for item in qq_info_data_home:
            qq_info_home = item.get('href')
        qq_info = [qq_info_home,qq_info_main,qq_info_url]
        return qq_info
    except:
        qq_info_data = qq_info_soup.select('body > div.category-wrap > div.container_16 > div > div.part1')
        for item in qq_info_data:
            qq_info_image = item.get('style')
        qq_info_image_url = qq_info_image[int(qq_info_image.find('url(')):int(qq_info_image.find(')',qq_info_image.find('{url(')))].strip('url(')
        qq_info_image_url = qq_info_image_url.rstrip(")!important")
        if qq_info_image_url[0] == "/":
            qq_info_image_url = "https:" + qq_info_image_url
        # print(qq_info_image_url)
        urlretrieve(url=qq_info_image_url,filename="qq_info.png")
        return qq_info_image_url
    # print(qq_info_main,"\n",qq_info_home)

def web_baoku_info(baoku_id):
    headers = {'User-Agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763'}
    # print(baoku_id)
    baoku_info_url = 'https://baoku.360.cn/soft/show/appid/' + baoku_id
    print(baoku_info_url)
    baoku_info_html_req = request.Request(url=baoku_info_url,headers=headers)
    baoku_info_html = urlopen(baoku_info_html_req)
    baoku_info_soup = BeautifulSoup(baoku_info_html.read(),"html.parser")
    baoku_info_data = baoku_info_soup.select('body > div.app-container > div:nth-child(2) > div.dashboard-container.pic-container > div > img')
    for item in baoku_info_data:
        baoku_info_image_url = item.get('src')
    baoku_info_image_url = "https:" +baoku_info_image_url
    # print(baoku_info_image_url)
    urlretrieve(url=baoku_info_image_url,filename="baoku_info.png")
    baoku_icon_data = baoku_info_soup.select('body > div.app-container > div:nth-child(2) > div:nth-child(2) > h1 > img')
    for item in baoku_icon_data:
        baoku_icon_image_url = item.get('src')
    baoku_icon_image_url = "https:" +baoku_icon_image_url
    print(baoku_icon_image_url)
    urlretrieve(url=baoku_icon_image_url,filename="baoku_icon.png")
    baoku_info_url = 'https://baoku.360.cn/soft/show/appid/' + baoku_id + 'd'
    # print(baoku_info_url)
    baoku_info_html_req = request.Request(url=baoku_info_url,headers=headers)
    baoku_info_html = urlopen(baoku_info_html_req)
    baoku_info_soup = BeautifulSoup(baoku_info_html.read(),"html.parser")
    baoku_detail = baoku_info_soup.select('body > div.wrap.clearfix > div.main-list.fr > div.app-info > div.app-introduce > div.introduce-txt1 > p')
    for item in baoku_detail:
        baoku_detail_text = item.get_text
    # print(baoku_detail_text)
    baoku_info = [baoku_detail_text,baoku_info_image_url]
    return baoku_info
    # print(baoku_info_main,"\n",baoku_info_home)

def web_hippo_info(app_name):
    headers = {'User-Agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763'}
    hippo_information_html_url = "https://filehippo.com/download_" + app_name + "/"
    hippo_information_html_req = request.Request(url=hippo_information_html_url,headers=headers)
    hippo_information_html = urlopen(hippo_information_html_req)
    hippo_information_soup = BeautifulSoup(hippo_information_html.read(),"html.parser")
    hippo_information_data = hippo_information_soup.select('body > div.page > div:nth-child(2) > div > div > div > section.mb-l > article')
    for item1 in hippo_information_data:
        hippo_information = item1.get_text()
    return hippo_information

def Lensi_info(app_name,app_source):
    if app_source == "Choco":
        choco_info(app_name)
    elif app_source == "Scoop":
        Scoop_info(app_name)
    elif app_source == "Winget":
        winget_info_id(app_name)
    elif app_source == "qq":
        web_qq_info(app_name)
    elif app_source == "360":
        web_baoku_info(app_name)
    elif app_source == "Hippo":
        web_hippo_info(app_name)