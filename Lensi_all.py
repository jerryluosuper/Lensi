'''
Author: your name
Date: 2022-03-21 11:39:01
LastEditTime: 2022-03-22 11:26:20
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \Lensi\Lensi_all.py
'''
import json
import os
import re
import subprocess
from urllib import request
from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup
import json
import threading
from urllib.parse import quote 
import csv
import codecs
from fuzzywuzzy import process,fuzz
from xpinyin import Pinyin 

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

def Lensi_init():
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
    elif app_source == "hippo":
        web_install_hippo(app_name)

def choco_num():
    headers = {'User-Agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763'}
    url = 'https://community.chocolatey.org/packages'
    req = request.Request(url=url,headers=headers)
    html = urlopen(req)
    soup = BeautifulSoup(html.read(),"html.parser")
    data = soup.select('#package > div > div.col-md-8.col-xl-9.col-xxl-8.py-3.py-xl-5.pe-xxl-5 > div.d-lg-flex.align-items-lg-center.justify-content-lg-between > div:nth-child(1) > h3')
    for item in data:
        name = str(item.get_text())
    number_list = re.findall(r"\d+\.?\d*",name)
    num = number_list[0]
    return num

def scoop_num():
    os.chdir("D:\\Scoop_all\\Scoop\\buckets")
    buckets_names = os.listdir()
    cnt = 0 
    for i in buckets_names:
        print(i)
        dir = "D:\\Scoop_all\\Scoop\\buckets\\" + i + "\\bucket"
        os.chdir(dir)
        bucket_list = os.listdir()
        cnt = cnt + len(bucket_list)
    return cnt

def qq_num():
    headers = {'User-Agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763'}
    url = 'https://pc.qq.com/category/c0.html'
    req = request.Request(url=url,headers=headers)
    html = urlopen(req)
    soup = BeautifulSoup(html.read(),"html.parser")
    data = soup.select('body > div.category-wrap > div.category-siderbar.J_category_siderbar > div > ul > li.cat-item.J_select_class_li.cat-curr > a')
    for item in data:
        name = str(item.get_text())
    number_list = re.findall(r"\d+\.?\d*",name)
    num = number_list[0]
    return num

def get_yiju():
    headers = {'User-Agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763'}
    url = 'https://yijuzhan.com/api/word.php'
    req = request.Request(url=url,headers=headers)
    html = urlopen(req)
    html_text = bytes.decode(html.read())
    return html_text

class myThread (threading.Thread):
    def __init__(self, source, app_name,limit_num=3):
        threading.Thread.__init__(self)
        self.source = source
        self.app_name = app_name
        self.limit_num = limit_num
    def run(self):
        # print ("开始线程：" + self.app_name)
        self.result = lensi_search_all(self.source,self.app_name,self.limit_num) #多线程大函数
        # print ("退出线程：" + self.app_name)
    def get_result(self):  #获取return结果
        try:  
            return self.result  
        except Exception:  
            return None  

def web_360_search(app_name,limmit_num):
    headers = {'User-Agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763'}
    # 伪装标头
    app_name_search = quote(app_name)#输入转换成相应格式
    # app_name = "geek"
    baoku_search_url = 'https://bapi.safe.360.cn/soft/search?keyword='+ app_name_search + '&page=1'
    baoku_html_req = request.Request(url=baoku_search_url,headers=headers)
    baoku_html = urlopen(baoku_html_req)#使用标头获取html
    baoku_soup = BeautifulSoup(baoku_html.read(),"html.parser")
    baoku_str = str(baoku_soup)#字符串化 便于查找
    # print(baoku_str)
    '''
    TODO 未使用正则表达式 待优化
    '''
    baoku_name_search_1 = 0
    baoku_version_search_1 = 0
    baoku_download_search_1 =0 
    baoku_id_search_1 = 0 
    baoku_detail_search_1 = 0
    baoku_icon_search_1 = 0
    # 定义上一次查找结果
    baoku_search_all_list = []
    limmit_num_search = baoku_str.count('{"softid":')
    limmit_num_real = min(limmit_num,limmit_num_search)
    #防止找不到更多程序
    for i in range(0,limmit_num_real):
        baoku_name_search = baoku_str.find('"softname":"',baoku_name_search_1)
        baoku_name_search_1 = baoku_name_search + 1
        baoku_name = baoku_str[baoku_name_search:int(baoku_str.find(',',baoku_name_search))].strip('"softname":"')
        if baoku_name == '':
            return baoku_search_all_list #判断是否还有软件
        baoku_version_search = baoku_str.find('"version":"',baoku_version_search_1)
        baoku_version_search_1 = baoku_version_search + 1
        baoku_download_search = baoku_str.find('"soft_download":"',baoku_download_search_1)
        baoku_download_search_1 = baoku_download_search + 1
        baoku_id_search = baoku_str.find('[{"softid":',baoku_id_search_1)
        baoku_detail_search = baoku_str.find('"desc":"',baoku_detail_search_1)
        baoku_detail_search_1 = baoku_detail_search + 1
        baoku_id_search_1 = baoku_id_search + 1
        baoku_icon_search = baoku_str.find('"logo":"',baoku_icon_search_1)
        baoku_icon_search_1 = baoku_icon_search + 1
        #从上一次查找结果后开始查找，实现识别多个软件
        baoku_version= baoku_str[baoku_version_search:int(baoku_str.find(',',baoku_version_search))].strip('"version":"')
        baoku_download = baoku_str[baoku_download_search:int(baoku_str.find(',',baoku_download_search))].strip('"soft_download":"')
        baoku_id = baoku_str[baoku_id_search :int(baoku_str.find(',',baoku_id_search ))].strip('[{"softid":')
        baoku_detail_text = baoku_str[baoku_detail_search :int(baoku_str.find(',',baoku_detail_search ))].strip('"desc":"')
        baoku_icon = baoku_str[baoku_icon_search :int(baoku_str.find(',',baoku_icon_search ))].strip('"logo":"')
        #截获字符串
        baoku_download_url = baoku_download.replace('\\',"")
        baoku_icon_url = "https:" + baoku_icon.replace('\\',"") + "g"
        baoku_info_url = 'https://baoku.360.cn/soft/show/appid/' + baoku_id + 'd'
        #网址处理
        baoku_search_all = [baoku_name.strip(",").encode('ascii').decode('unicode_escape'),baoku_version.strip(","),baoku_detail_text.strip(",").encode('ascii').decode('unicode_escape'),baoku_info_url,baoku_download_url.strip(","),baoku_icon_url,fuzz.partial_ratio(app_name,baoku_name.strip(",").encode('ascii').decode('unicode_escape')),"360"]
        #整理格式
        baoku_search_all_list.append(baoku_search_all)
    return baoku_search_all_list

def web_qq_search(app_name,limmit_num):
    headers = {'User-Agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763'}
    # app_name = "geek"
    # app_name = app_name.encode('unicode_escape').decode('utf-8')
    # app_name_search = app_name.replace("\\","%")
    app_name_search = quote(app_name)
    # print(app_name_search)
    qq_search_url = 'https://s.pcmgr.qq.com/tapi/web/searchcgi.php?type=search&callback=searchCallback&keyword='+ app_name_search +'&page=1&pernum=' +str(limmit_num)+'&more=0'
    qq_html_req = request.Request(url=qq_search_url,headers=headers)
    qq_html = urlopen(qq_html_req)
    qq_soup = BeautifulSoup(qq_html.read(),"html.parser")
    qq_str = str(qq_soup)
    '''
    TODO 未使用正则表达式 待优化
    '''
    qq_search_all=[]
    qq_search_list=[]
    # print(qq_str)
    qq_name_find_1 = 0
    qq_version_find_1 = 0
    qq_download_find_1 = 0
    qq_id_find_1 = 0
    qq_detail_find_1 = 0  
    qq_icon_find_1 = 0
    limmit_num_real = min(limmit_num,qq_str.count('<versionname>'))
    #防止找不到更多程序
    for i in range(0,limmit_num_real):
        if i == 0:
            qq_name_find = qq_str.find('<![CDATA[',qq_name_find_1)
            qq_name_find_1 = qq_name_find + 1
        else:
            for j in range(0,7):
                qq_name_find = qq_str.find('<![CDATA[',qq_name_find_1)
                qq_name_find_1 = qq_name_find + 1
            # print(qq_name_find)
            #有7个“<![CDATA[”！！！ 之后才能找到正确软件名称
        qq_version_find = int(qq_str.find('<versionname>',qq_version_find_1))
        qq_version_find_1 = qq_version_find + 1
        # print(qq_name_find)
        qq_download_find = qq_str.find('[CDATA[http:',qq_download_find_1)
        qq_download_find_1 = qq_download_find + 1
        # print(qq_name_find)
        qq_id_find = qq_str.find('{"SoftID":"',qq_id_find_1)
        qq_id_find_1 = qq_id_find + 1 
        qq_detail_find = qq_str.find(r'<feature>\n                <![CDATA[',qq_detail_find_1) + 20
        qq_detail_find_1 = qq_detail_find + 1 
        qq_icon_find = qq_str.find('<logo48>',qq_icon_find_1) 
        qq_icon_find_1 = qq_icon_find + 1 
        # print(qq_name_find)
        #从上一次查找结果后开始查找，实现识别多个软件
        qq_name = qq_str[qq_name_find:int(qq_str.find("]",qq_name_find))].strip("<![CDATA[")
        if qq_name == '':
            return qq_search_list #判断是否还有软件
        qq_version = qq_str[qq_version_find:int(qq_str.find("&lt",qq_version_find))].strip("<versionname>")
        qq_download = qq_str[qq_download_find:int(qq_str.find("]",qq_download_find))].strip("![CDATA[")
        qq_id = qq_str[int(qq_id_find):int(qq_str.find(',',qq_id_find))].strip('{"SoftID":"')
        qq_detail = qq_str[qq_detail_find:int(qq_str.find(']',qq_detail_find))].strip(r"<feature>\n                <![CDATA[")
        qq_icon = qq_str[qq_icon_find:int(qq_str.find('&lt',qq_icon_find))].strip(' <logo48>')
        qq_icon_url = "https://pc3.gtimg.com/softmgr/logo/48/" + qq_icon + "g"
        qq_id_int = int(qq_id)
    # print(qq_id)
        qq_info_url = 'https://pc.qq.com/detail/'+ str(qq_id_int%20) + '/detail_' + qq_id + '.html' 
        # print(qq_detail)
        #截获字符串
        qq_download_url = qq_download.replace('\\',"")
        #网址处理
        qq_search_all = [qq_name.encode('ascii').decode('unicode_escape'),qq_version,qq_detail.encode('ascii').decode('unicode_escape'),qq_info_url,qq_download_url,qq_icon_url,fuzz.partial_ratio(app_name,qq_name.encode('ascii').decode('unicode_escape')),"qq"]
        #整理格式
        qq_search_list.append(qq_search_all)
    return qq_search_list
    # print (qq_name,"\n","Version:",qq_version,"\n",qq_download_url,"\n")

def Scoop_search_lensi(name,buckets_list_install,search_limit,Scoop_install_place ):
    for ch in name:
        if '\u4e00' <= ch <= '\u9fff': ##识别中文
            p = Pinyin() #scoop 中文搜索不好，转为拼音
            name = p.get_pinyin(name,'')
            break
    # print(name)
    search_list = process.extract(name,buckets_list_install, limit=search_limit) 
    # 模糊搜索
    # print(search_list)
    app_name_all = []
    for i in range(0,search_limit):
        app_name = search_list[i][0][0][search_list[i][0][0].find('\\'):].strip("\\")
        app_name_install = search_list[i][0][0]
        app_json = []
        # print(app_name_install,app_name)
        app_name_json = Scoop_install_place + "\\Scoop\\buckets\\" + app_name_install[:app_name_install.find('\\')] + "\\bucket\\" + app_name + ".json"
        # app_name_json = "D:\\Scoop\\buckets\\" + app_name_install[:app_name_install.find('\\')] + "\\bucket\\" + app_name + ".json"
        # print(app_name_json)
        try:
            with open(app_name_json, 'r') as f:
                app_json = json.load(f)
                # 解析json，获取detail
            app_detail = [app_name_install,app_json["version"],app_json["description"],app_json["homepage"],app_name,"https://scoop.netlify.app/scoop.svg",fuzz.partial_ratio(app_name,app_name_install),"Scoop"]
            app_name_all.append(app_detail) 
            # TODO The missing 'n' and other ----BUG 放弃！！！ (╯▔皿▔)╯
        except:
            pass
            # print("error")
    return app_name_all

def Scoop_buckets_save(Scoop_install_place):#遍历scoop bucket 存入csv中
    #简单来说就是获取每个buckets里bucket的文件
    buckets_list_install = []
    os.chdir(Scoop_install_place+"\\Scoop\\buckets")
    buckets_names = os.listdir()
    for i in buckets_names:
        # print(i)
        dir = Scoop_install_place + "\\Scoop\\buckets\\" + i + "\\bucket"
        os.chdir(dir)
        bucket_list = os.listdir()
        for j in bucket_list:
            buckets_list_install.append(i+"\\"+j.strip(".json"))
    os.chdir("D:\\")
    file_csv = codecs.open("buckets_list_install.csv",'w+','utf-8')#追加
    writer = csv.writer(file_csv, delimiter=' ', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
    for data in buckets_list_install:
        list_data = [data]
        writer.writerow(list_data) #写入csv 

def Scoop_buckets_load(): #加载csv到列表
    buckets_list_install = []
    os.chdir("D:\\")
    with open("buckets_list_install.csv", "r", encoding='UTF-8') as file:
        data = csv.reader(file)
        for row in data:
            # row_l = [row] 
            #读取csv
            # buckets_list_install.append(row_l)
            buckets_list_install.append(row)
    return buckets_list_install

def choco_search(app_name,limmit_num): #choco搜索解析
    '''
    大致输出格式
    app_name_1|app_version_1
    app_name_1|app_version_1
    '''
    try:
        for ch in app_name:
            if '\u4e00' <= ch <= '\u9fff':
                p = Pinyin() 
                app_name = p.get_pinyin(app_name,'') #一样的，拼音搜索
                break
        # print(app_name)
        cmd = 'choco search '+ app_name + ' --limitoutput --page=1 --page-size=' + str(limmit_num)
        pipe = subprocess.Popen(cmd, shell=True,stdout=subprocess.PIPE, universal_newlines=True)
        search_result = pipe.stdout.read()
        pipe.communicate()#等待
        # print(search_result.replace("Directory 'C:\ProgramData\chocolatey\lib' does not exist.",""))
        #怎么说，这段真的乱。。。
        search_list = [] #干嘛的？我怎么知道 看上去像用|进行分离后的列表
        search_list_all = search_result.split() #通过空行分离成列表
        search_list_all_a = []  #干嘛的？我怎么知道 看上去像返回的列表，所有搜索到的软件的整合
        for name in search_list_all:
            search_list.append(name.split("|")) #遍历空行分离后的列表，再用|进行分离
        if search_list[0] == ['Directory']:
            del(search_list[0:5]) #排除"Directory 'C:\ProgramData\chocolatey\lib' does not exist."的干扰
            #好低效的方法
        if search_list == []:
            search_list = None 
            #排除空列表的错误？我觉得没用啊
            return search_list
        else:
            # print(search_list)
            for i in search_list:
                app_name_true = i[0].replace("-","--") #获取非模糊名称
                cmd = 'choco info '+ app_name_true
                # print(cmd)
                app_detail = subprocess.Popen(cmd, shell=True,stdout=subprocess.PIPE,universal_newlines=True).stdout.read()
                # app_detail = subprocess.getoutput('choco info '+ app_name_true) #info 获取官网和detail
                if app_detail.find("0 packages found.") != -1:
                    return None
                app_home_url = app_detail[int(app_detail.find('Software Site:')):int(app_detail.find("\n",app_detail.find("Software Site:")))].strip("Software Site:")
                app_detail_info = app_detail[int(app_detail.find('Summary: ')):int(app_detail.find("\n",app_detail.find("Summary: ")))].strip("Summary: ")
                # 获取官网
                # 部分有bug啊，但我不想解决
                # print(i[0],i[1],app_detail_url,app_name_true)
                search_list_all_a.append([i[0],i[1],app_detail_info,app_home_url.strip("\n"),app_name_true,"https://chocolatey.org/assets/images/global-shared/logo.svg",fuzz.partial_ratio(app_name,i[0]),"Choco"])
            # search_list_all_a.append("Choco")
            return search_list_all_a
    finally:
        return search_list_all_a

def winget_search(app_name,limmit_num):#winget 搜索解析
    '''
    大致输出格式：
    -\|/ 
    名称          ID           版本    源
    -------------------------------------------
    xx xx xx xx
    <由于结果限制而截断了其他条目>
    '''
    try:
        search_result_list_all = []
        app_name = app_name.replace(" ","") #winget search 软件名中不能有空格
        # print(app_name)
        cmd = "winget search " + app_name + " -n " + str(limmit_num)
        # 一个非常非常非常又烂又低效的方法——存储到文件再读取
        # TODO 优化！！！
        pipe = subprocess.Popen(cmd, shell=True,stdout=subprocess.PIPE)#subprocess 将输出保存到search_result.txt中
        search_result_list_un = pipe.stdout.readlines()[2:]#去除前三行干扰 有bug
        search_result_list = []
        pipe.communicate()
        for i in search_result_list_un:
            search_result_list.append(i.decode("utf-8"))
        # print(search_result_list)
        pipe = subprocess.Popen(cmd, shell=True,stdout=subprocess.PIPE)#subprocess 将输出保存到search_result.txt中
        search_result_txt = pipe.stdout.read().decode("utf-8")
        pipe.communicate()#等待
        # print(search_result_txt)
        if search_result_txt.find("找不到与输入条件匹配的程序包。") != -1:
            return search_result_list_all #异常处理——找不到或根本不存在？
        if  search_result_txt.find("<由于结果限制而截断了其他条目>") != -1:
            search_result_list = search_result_list[:len(search_result_list)-1] # 去除末行干扰
        cnt_cut = 0
        for i in range(0,len(search_result_list)):
            if search_result_list[i] == "--------------------------------------------" : #为啥我觉得只要这一句就好了
                cnt_cut = i
                break
        del(search_result_list[:cnt_cut]) #顺带解决开机第一次100%加载的bug
        search_result = [] #这又在干嘛？ 以空行分隔后的软件列表
        # print(search_result_list)
        for i in search_result_list:
            search_result.append(i.split())#以空行分隔
        for j in search_result:
            name = "".join(j[:len(j)-3]) #因为id version source 是连续的 不带空格的，所以确定这三个把前面的连起来
            del(j[:len(j)-3])
            j.insert(0,name)
            # print(name)
        # print (search_result)
        del(search_result[0])
        if search_result == []:#判断是否为空，防止报错
            search_result_list_all = None
            return search_result_list_all
        else:
            # print(search_result)
            if len(search_result) == 1: #防止range（0，0）的错误
                cmd = "winget show --id " + search_result[0][1]
                #换汤不换药
                pipe = subprocess.Popen(cmd, shell=True,stdout=subprocess.PIPE)#subprocess 将输出保存到search_result.txt中
                info_result = pipe.stdout.read().decode("utf-8")
                pipe.communicate()#等待？
                info_result_url = info_result[int(info_result.find('URL:')):int(info_result.find("\n",info_result.find("URL:")))].strip("URL:")
                info_detail = info_result[int(info_result.find('描述: ')):int(info_result.find("\n",info_result.find("描述: ")))].strip("描述: ")
                #解析官网url
                # print(info_result_url)
                # print(info_detail)
                # for j in info_detail:
                #     app_info = "".join(j.replace(r"\r","")) #因为id version source 是连续的 不带空格的，所以确定这三个把前面的连起来
                search_result_app = [search_result[0][0],search_result[0][2],info_detail.replace("\r",""),info_result_url.replace("\r",""),search_result[0][1],None,fuzz.partial_ratio(app_name,search_result[0][0]),"Winget"]
                #统一格式
                # print(search_result_app)
                search_result_list_all.append(search_result_app)
                # search_result.append("Winget")
                return search_result_list_all
            else:
                # print(search_result)
                for i in range(0,len(search_result)-1):#除len = 1的情况 其余同上
                    # print(search_result)
                    cmd = "winget show --id " + search_result[i][1]
                    #换汤不换药
                    pipe = subprocess.Popen(cmd, shell=True,stdout=subprocess.PIPE)#subprocess 将输出保存到search_result.txt中
                    info_result = pipe.stdout.read().decode("utf-8")
                    pipe.communicate()#等待？
                    info_result_url = info_result[int(info_result.find('URL:')):int(info_result.find("\n",info_result.find("URL:")))].strip("URL:")
                    info_detail = info_result[int(info_result.find('描述: ')):int(info_result.find("\n",info_result.find("描述: ")))].strip("描述: ")
                    #解析官网url
                    # for j in info_detail:
                    #     app_info = "".join(j.replace(r"\r","")) #因为id version source 是连续的 不带空格的，所以确定这三个把前面的连起来
                    search_result_app = [search_result[i][0],search_result[i][2],info_detail.replace("\r",""),info_result_url.replace("\r",""),search_result[i][1],None,fuzz.partial_ratio(app_name,search_result[i][0]),"Winget"]
                    #统一格式
                    # print(search_result_app)
                    search_result_list_all.append(search_result_app)
                    # search_result.append("Winget")
                # search_result.append("Winget")
        return search_result_list_all
    finally:
        return search_result_list_all

def hippo_search_easy(app_name):
    headers = {'User-Agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763'}
    hippo_download_html_url = "https://filehippo.com/download_" + app_name + "/post_download/"
    hippo_information_html_url = "https://filehippo.com/download_" + app_name + "/"
    hippo_search_result = []
    try:
        hippo_information_html_req = request.Request(url=hippo_information_html_url,headers=headers)
        hippo_information_html = urlopen(hippo_information_html_req)
    except:
        # print("!")
        return None
    else:
        # print("From",hippo_download_html_url,"\n","And also from",hippo_information_html_url,"\n")
        hippo_information_soup = BeautifulSoup(hippo_information_html.read(),"html.parser")
        hippo_information_data = hippo_information_soup.select('body > div.page > div:nth-child(2) > div > div > div > section.mb-l > article > p:nth-child(3)')
        hippo_information_data_name = hippo_information_soup.select('body > div.page > div:nth-child(2) > div > div > div > section.program-header-content > div.program-header-content__main > div > div.media__body > h1')
        hippo_icon_url_detail = hippo_information_soup.select('body > div.page > div:nth-child(2) > div > div > div > section.program-header-content > div.program-header-content__main > div > div.media__image > img')
        hippo_version_detail = hippo_information_soup.select('body > div.page > div:nth-child(2) > div > div > div > section.program-header-content > div.program-header-content__main > div > div.media__body > p.program-header__version')
        for item in hippo_information_data_name:
            hippo_information_name = item.get_text()
        # print (hippo_information_name,"\n")
        for item1 in hippo_information_data:
            hippo_information = item1.get_text()
        for item2 in hippo_version_detail:
            hippo_version = item2.get_text()
        for item3 in hippo_icon_url_detail:
            hippo_icon_url = item3.get('src')
        # hippo_information = str(hippo_information)
        # print (hippo_information)
        try:
            hippo_download_html_req = request.Request(url=hippo_download_html_url,headers=headers)
            hippo_download_html = urlopen(hippo_download_html_req)
            hippo_download_soup = BeautifulSoup(hippo_download_html.read(),"html.parser")
            hippo_download_data = hippo_download_soup.select('body > div.page > script:nth-child(2)')
            for item2 in hippo_download_data:
                    hippo_download_url = item2.get('data-qa-download-url')
            # print (hippo_download_url)
        except:
            hippo_search_result_list = [hippo_information_name,hippo_version,hippo_information,hippo_information_html_url,None,hippo_icon_url,fuzz.partial_ratio(app_name,hippo_information_name),"hippo"]
            hippo_search_result.append(hippo_search_result_list)
            return hippo_search_result
        else:
            hippo_search_result_list = [hippo_information_name,hippo_version,hippo_information,hippo_information_html_url,hippo_download_url,hippo_icon_url,fuzz.partial_ratio(app_name,hippo_information_name),"hippo"]
            hippo_search_result.append(hippo_search_result_list)
            # print(hippo_search_result)
            return hippo_search_result

def lensi_search_all(source,app_name,limmit_num):#搜索大函数
        if source == "360":
            return web_360_search(app_name,limmit_num)
        elif source == "qq":
            return web_qq_search(app_name,limmit_num)
        elif source == "Scoop":
            buckets_list_install = Scoop_buckets_load()
            return Scoop_search_lensi(app_name,buckets_list_install,limmit_num,"D:")
        elif source == "Choco":
            return choco_search(app_name,limmit_num)
        elif source == "Winget":
            return winget_search(app_name,limmit_num)
        elif source == "Hippo":
            return hippo_search_easy(app_name)

def app_name_cmp(e):
    return e[6]

def Lensi_search(app_name,app_num):
    thread_360 = myThread( "360", app_name,app_num[0])
    thread_qq = myThread("qq", app_name,app_num[1])
    thread_S = myThread( "Scoop", app_name,app_num[2])
    thread_C = myThread( "Choco", app_name,app_num[3])
    thread_W = myThread( "Winget", app_name,app_num[4])
    thread_H = myThread( "Hippo", app_name,0)
    #多线程
    search_result = []
    # 开启新线程
    thread_360.start()
    thread_qq.start()
    thread_S .start()
    thread_C.start()
    thread_W.start()
    thread_H.start()
    #等待进程
    thread_360.join()
    thread_qq.join()
    thread_S.join()
    thread_C.join()
    thread_W.join()
    thread_H.join()
    # print ("退出主线程")
    #判断结果是否为空
    if thread_360.get_result() != None :
        search_result.extend(thread_360.get_result())
    if thread_qq.get_result() != None :
        search_result.extend(thread_qq.get_result())  
    if thread_S.get_result() != None :
        search_result.extend(thread_S.get_result())
    if thread_C.get_result() != None :  
        search_result.extend(thread_C.get_result())
    if thread_W.get_result() != None :  
        search_result.extend(thread_W.get_result())  
    if thread_H.get_result() != None :  
        search_result.extend(thread_H.get_result())  
    # print(search_result)
    search_result.sort(key=app_name_cmp,reverse=True)
    return search_result

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

def Lensi_update_all():
    choco_update_all()
    choco_update()
    Scoop_update_all()
    winget_update_all()
    winget_update_source()

def Lensi_update(app_source):
    if app_source == "Choco":
        choco_update()
    elif app_source == "Scoop":
        Scoop_update()
    elif app_source == "Winget":
        winget_update_source()
