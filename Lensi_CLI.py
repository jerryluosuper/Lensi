#!/usr/bin/env python
# -*- coding:utf-8 _*-
import os
import shutil
from urllib import request
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
import threading
from urllib.parse import quote 
from fuzzywuzzy import fuzz,process
import fire
import configparser
from tqdm import tqdm
import winshell
import zipfile
from xpinyin import Pinyin 
import json
import csv
import codecs
import subprocess
import win32api,win32con

def Scoop_info(app_name):
    os.system('scoop info '+ app_name)

def Scoop_info_lensi(app_name_install,SIP):
    app_json = []
    app_name_json = SIP + "\\buckets\\" + app_name_install[:app_name_install.find('\\')] + "\\bucket\\" + app_name_install[app_name_install.find('\\'):].strip("\\") + ".json"
    with open(app_name_json, 'r') as f:
        app_json = json.load(f)
    app_detail = [app_json["shortcuts"][0][1],app_json["version"],app_json["description"],app_json["homepage"]]
    return app_detail

def winget_info_id(app_id):
    cmd = "winget show --id " + app_id
    os.system(cmd)

def choco_install_app(app_name):
    os.system("choco install "+app_name)

def Scoop_install_app(app_name):
    os.system("scoop install " + app_name)

def winget_install_app_id(app_id):
    os.system("winget install --silent --accept-source-agreement --id "+ app_id)


def Scoop_search_lensi(name,buckets_list_install,search_limit,Scoop_install_place):
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
        app_name_json = Scoop_install_place + "\\buckets\\" + app_name_install[:app_name_install.find('\\')] + "\\bucket\\" + app_name + ".json"
        # print(app_name_json)
        # app_name_json = "D:\\buckets\\" + app_name_install[:app_name_install.find('\\')] + "\\bucket\\" + app_name + ".json"
        # print(app_name_json)
        try:
            with open(app_name_json, 'r') as f:
                app_json = json.load(f)
                # 解析json，获取detail
            app_detail = [app_name_install,app_json["version"],app_json["description"],app_name,app_json["homepage"],app_name,"https://scoop.netlify.app/scoop.svg",fuzz.partial_ratio(app_name,app_name_install),"Scoop"]
            app_name_all.append(app_detail) 
            # TODO The missing 'n' and others ----BUG 放弃！！！ (╯▔皿▔)╯
        except:
            pass
            # print("error")
    return app_name_all

def Scoop_buckets_save(Scoop_install_place):#遍历scoop bucket 存入csv中
    #简单来说就是获取每个buckets里bucket的文件
    buckets_list_install = []
    os.chdir(Scoop_install_place+"\\buckets")
    buckets_names = os.listdir()
    for i in buckets_names:
        # print(i)
        dir = Scoop_install_place + "\\buckets\\" + i + "\\bucket"
        os.chdir(dir)
        bucket_list = os.listdir()
        for j in bucket_list:
            buckets_list_install.append(i+"\\"+j.strip(".json"))
    os.chdir("D:\\Lensi\\")
    file_csv = codecs.open("buckets_list_install.csv",'w+','utf-8')#追加
    writer = csv.writer(file_csv, delimiter=' ', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
    for data in buckets_list_install:
        list_data = [data]
        writer.writerow(list_data) #写入csv 

def choco_info(app_name):
    os.system("choco info "+ app_name)

def Scoop_uninstall_app(app_name):
    os.system("scoop uninstall " + app_name)

def choco_uninstall_app(app_name):
    os.system("choco uninstall " + app_name)

def winget_uninstall_app(app_name):
    os.system("winget uninstall " + app_name)

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
        # print(search_list)
        if len(search_list)==0:
            search_list = None 
            #排除空列表的错误？我觉得没用啊
            return search_list
            # print(search_list)
        # print(search_list)
        for i in search_list:
            app_name_true = str(i[0]) #获取非模糊名称
            # print(app_name_true)
            # print(cmd)
            cmd = "choco info "+ app_name_true
            # print(cmd)
            pipe = subprocess.Popen(cmd, shell=True,stdout=subprocess.PIPE)
            app_detail = str(pipe.stdout.read())
            pipe.communicate()
            app_detail = app_detail.replace("\\r","")
            app_detail = app_detail.replace("\\n","")
            # print(app_detail)
            # app_detail = subprocess.getoutput('choco info '+ app_name_true) #info 获取官网和detail
            if app_detail.find("0 packages found.") != -1:
                return None
            app_home_url = app_detail[int(app_detail.find('Software Site:')):int(app_detail.find("\n",app_detail.find("Software Site:")))].strip("Software Site:")
            app_detail_info = app_detail[int(app_detail.find('Summary: ')):int(app_detail.find("\n",app_detail.find("Summary: ")))].strip("Summary: ")
            # 获取官网
            # 部分有bug啊，但我不想解决
            # print(i[0],i[1],app_detail_url,app_name_true)
            search_list_all_a.append([i[0],i[1],app_detail_info,i[0],app_home_url.strip("\n"),app_name_true,"https://chocolatey.org/assets/images/global-shared/logo.svg",fuzz.partial_ratio(app_name,i[0]),"Choco"])
        # search_list_all_a.append("Choco")
        return search_list_all_a
    except:
        return None

def add_uninstall_app(app_name):
    os.chdir(lensi_path)
    f = open("app_list.txt","r")
    app_list = f.readlines()
    f.close()
    app_list_real = []
    for i in app_list:
        if i.find("Lensi") == -1:
            j=i.split()
            app_name_real = j[:len(j)-2]
            name = ""
            for k in app_name_real:
                name = name + k +" "
            name = name.strip(" ")
            del(j[:len(j)-2])
            j.insert(0,name.lower())
            j[len(j)-1] = j[len(j)-1].replace("\n","")
            app_list_real.append(j)
    for i in range(0,len(app_list_real)):
        try:
            if fuzz.partial_ratio(app_list_real[i][0],app_name)>=HAF:
                del(app_list_real[i])
            else:
                app_list_real[i][0] = app_list_real[i][0].title()
        except:
            pass
    write_text = ""
    for i in range(0,len(app_list_real)):
        write_text = write_text + app_list_real[i][0] + " " + app_list_real[i][1] + " " + app_list_real[i][2] + "\n"
    write_text = "Lensi 0.1.2 pip\n" + write_text
    with open("app_list.txt","w") as f:
        f.write(write_text)

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
        search_result_list = search_result_list[cnt_cut:] #顺带解决开机第一次100%加载的bug
        search_result = [] #这又在干嘛？ 以空行分隔后的软件列表
        # print(search_result_list)
        for i in search_result_list:
            search_result.append(i.split())#以空行分隔
        for j in search_result:
            app_name = j[:len(j)-3]
            name = ""
            # print(app_name)
            for k in app_name:
                name = name + k +" " #因为id version source 是连续的 不带空格的，所以确定这三个把前面的连起来
            name = name.strip(" ")
            del(j[:len(j)-3])
            j.insert(0,name)
            # print(name)
        # print (search_result)
        if search_result == []:#判断是否为空，防止报错
            search_result_list_all = None
            return search_result_list_all
        else:
            # print(len(search_result))
            # # print(search_result)
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
                search_result_app = [search_result[0][0],search_result[0][2],info_detail.strip("\r"),search_result[0][0],info_result_url.strip("\r"),search_result[0][1],None,fuzz.partial_ratio(app_name,search_result[0][0]),"Winget"]
                #统一格式
                # print(search_result_app)
                search_result_list_all.append(search_result_app)
                # search_result.append("Winget")
                return search_result_list_all
            else:
                #print(search_result)
                for i in range(0,len(search_result)):#除len = 1的情况 其余同上
                    cmd = "winget show --id " + search_result[i][1]
                    #换汤不换药
                    pipe = subprocess.Popen(cmd, shell=True,stdout=subprocess.PIPE)#subprocess 将输出保存到search_result.txt中
                    info_result = pipe.stdout.read().decode("utf-8")
                    pipe.communicate()#等待？
                    info_result_url = info_result[int(info_result.find('URL:')):int(info_result.find("\n",info_result.find("URL:")))].strip("URL:")
                    info_detail = info_result[int(info_result.find('描述: ')):int(info_result.find("\n",info_result.find("描述: ")))].strip("描述: ")
                    #解析官网url
                    # print(info_result_url)
                    search_result_app = [search_result[i][0],search_result[i][2],info_detail.strip("\r"),search_result[i][0],info_result_url.strip("\r"),search_result[i][1],None,fuzz.partial_ratio(app_name,search_result[i][0]),"Winget"]
                    #统一格式
                    # print(search_result_app)
                    search_result_list_all.append(search_result_app)
                    # search_result.append("Winget")
                # search_result.append("Winget")
        return search_result_list_all
    except:
        return None

def Scoop_buckets_load(): #加载csv到列表
    buckets_list_install = []
    os.chdir("D:\\Lensi\\")
    with open("buckets_list_install.csv", "r", encoding='UTF-8') as file:
        data = csv.reader(file)
        for row in data:
            # row_l = [row] 
            #读取csv
            # buckets_list_install.append(row_l)
            buckets_list_install.append(row)
    return buckets_list_install

def web_qq_info(qq_id):
    headers = {'User-Agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763'}
    qq_id_int = int(qq_id)
    # pprint_easy(qq_id)
    qq_info_url = 'https://pc.qq.com/detail/'+ str(qq_id_int%20) + '/detail_' + qq_id + '.html' 
    # pprint_easy(qq_info_url)
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
        # pprint_easy(qq_info_image_url)
        return qq_info_image_url
    # pprint_easy(qq_info_main,"\n",qq_info_home)

def web_baoku_info(baoku_id):
    headers = {'User-Agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763'}
    # pprint_easy(baoku_id)
    baoku_info_url = 'https://baoku.360.cn/soft/show/appid/' + baoku_id
    # pprint_easy(baoku_info_url)
    baoku_info_html_req = request.Request(url=baoku_info_url,headers=headers)
    baoku_info_html = urlopen(baoku_info_html_req)
    baoku_info_soup = BeautifulSoup(baoku_info_html.read(),"html.parser")
    baoku_info_data = baoku_info_soup.select('body > div.app-container > div:nth-child(2) > div.dashboard-container.pic-container > div > img')
    for item in baoku_info_data:
        baoku_info_image_url = item.get('src')
    baoku_info_image_url = "https:" +baoku_info_image_url
    # pprint_easy(baoku_info_image_url)
    baoku_icon_data = baoku_info_soup.select('body > div.app-container > div:nth-child(2) > div:nth-child(2) > h1 > img')
    for item in baoku_icon_data:
        baoku_icon_image_url = item.get('src')
    baoku_icon_image_url = "https:" + str(baoku_icon_image_url)
    # pprint_easy(baoku_icon_image_url)
    baoku_info_url = 'https://baoku.360.cn/soft/show/appid/' + baoku_id + 'd'
    # pprint_easy(baoku_info_url)
    baoku_info_html_req = request.Request(url=baoku_info_url,headers=headers)
    baoku_info_html = urlopen(baoku_info_html_req)
    baoku_info_soup = BeautifulSoup(baoku_info_html.read(),"html.parser")
    baoku_detail = baoku_info_soup.select('body > div.wrap.clearfix > div.main-list.fr > div.app-info > div.app-introduce > div.introduce-txt1 > p')
    for item in baoku_detail:
        baoku_detail_text = item.get_text
    # pprint_easy(baoku_detail_text)
    baoku_info = [baoku_detail_text,baoku_info_image_url]
    return baoku_info
    # pprint_easy(baoku_info_main,"\n",baoku_info_home)

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


class myThread_search (threading.Thread):
    def __init__(self, source, app_name,limit_num=3,SIP="D:\Scoop"):
        threading.Thread.__init__(self)
        self.source = source
        self.app_name = app_name
        self.limit_num = limit_num
        self.SIP = SIP
    def run(self):
        # print ("开始线程：" + self.app_name)
        self.result = lensi_search_all(self.source,self.app_name,self.limit_num,self.SIP) #多线程大函数
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
    baoku_search_all_list = []
    baoku_search_url = 'https://bapi.safe.360.cn/soft/search?keyword='+ app_name_search + '&page=1'
    baoku_html_req = request.Request(url=baoku_search_url,headers=headers)
    baoku_html = urlopen(baoku_html_req)#使用标头获取html
    baoku_soup = str(BeautifulSoup(baoku_html.read(),"html.parser"))
    baoku_json = json.loads(baoku_soup)
    # print(baoku_json)
    baoku_num_real = min(baoku_json['data']['total'],limmit_num)
    for i in range(0,baoku_num_real):
        baoku_name = baoku_json['data']['list'][i]['softname']
        baoku_version = baoku_json['data']['list'][i]['version']
        baoku_detail_text = baoku_json['data']['list'][i]['desc']
        baoku_id = baoku_json['data']['list'][i]['softid']
        baoku_info_url = "https://baoku.360.cn/soft/show/appid/" + str(baoku_id)
        baoku_download_url = baoku_json['data']['list'][i]['soft_download']
        baoku_icon_url = "https:" + baoku_json['data']['list'][i]['logo']
        baoku_search_all = [baoku_name,baoku_version,baoku_detail_text,baoku_info_url,baoku_id,baoku_download_url,baoku_icon_url,fuzz.partial_ratio(app_name,baoku_name),"360"]
        #整理格式
        baoku_search_all_list.append(baoku_search_all)
    return baoku_search_all_list

def web_qq_search(app_name,limmit_num):
    headers = {'User-Agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763'}
    # app_name = "geek"
    # app_name = app_name.encode('unicode_escape').decode('utf-8')
    # app_name_search = app_name.replace("\\","%")
    app_name_search = quote(app_name)
    # pprint_easy(app_name_search)
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
    # pprint_easy(qq_str)
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
            # pprint_easy(qq_name_find)
            #有7个“<![CDATA[”！！！ 之后才能找到正确软件名称
        qq_version_find = int(qq_str.find('<versionname>',qq_version_find_1))
        qq_version_find_1 = qq_version_find + 1
        # pprint_easy(qq_name_find)
        qq_download_find = qq_str.find('[CDATA[http:',qq_download_find_1)
        qq_download_find_1 = qq_download_find + 1
        # pprint_easy(qq_name_find)
        qq_id_find = qq_str.find('{"SoftID":"',qq_id_find_1)
        qq_id_find_1 = qq_id_find + 1 
        qq_detail_find = qq_str.find(r'<feature>\n                <![CDATA[',qq_detail_find_1) - 15
        qq_detail_find_1 = qq_detail_find + 1 
        qq_icon_find = qq_str.find('<logo48>',qq_icon_find_1) 
        qq_icon_find_1 = qq_icon_find + 1 
        # pprint_easy(qq_name_find)
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
    # pprint_easy(qq_id)
        qq_info_url = 'https://pc.qq.com/detail/'+ str(qq_id_int%20) + '/detail_' + qq_id + '.html' 
        # pprint_easy(qq_detail)
        #截获字符串
        qq_download_url = qq_download.replace('\\',"")
        #网址处理
        qq_detail_text = qq_detail.encode('ascii').decode('unicode_escape')
        qq_search_all = [qq_name.encode('ascii').decode('unicode_escape'),qq_version,qq_detail_text.strip(";\n            <feature>\n                <![CDATA["),qq_info_url,qq_id,qq_download_url,qq_icon_url,fuzz.partial_ratio(app_name,qq_name.encode('ascii').decode('unicode_escape')),"qq"]
        #整理格式
        qq_search_list.append(qq_search_all)
    return qq_search_list
    # print (qq_name,"\n","Version:",qq_version,"\n",qq_download_url,"\n")

def hippo_search_easy(app_name):
    headers = {'User-Agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763'}
    hippo_download_html_url = "https://filehippo.com/download_" + app_name + "/post_download/"
    hippo_information_html_url = "https://filehippo.com/download_" + app_name + "/"
    hippo_search_result = []
    try:
        hippo_information_html_req = request.Request(url=hippo_information_html_url,headers=headers)
        hippo_information_html = urlopen(hippo_information_html_req)
    except:
        # pprint_easy("!")
        return None
    else:
        # pprint_easy("From",hippo_download_html_url,"\n","And also from",hippo_information_html_url,"\n")
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
            hippo_search_result_list = [app_name,hippo_version,hippo_information,hippo_information_html_url,app_name,None,hippo_icon_url,fuzz.partial_ratio(app_name,hippo_information_name),"hippo"]
            hippo_search_result.append(hippo_search_result_list)
            return hippo_search_result
        else:
            hippo_search_result_list = [app_name,hippo_version,hippo_information,hippo_information_html_url,app_name,hippo_download_url,hippo_icon_url,fuzz.partial_ratio(app_name,hippo_information_name),"hippo"]
            hippo_search_result.append(hippo_search_result_list)
            # pprint_easy(hippo_search_result)
            return hippo_search_result

def lensi_search_all(source,app_name,limmit_num,SIP="D:\Scoop"):#搜索大函数
        if source == "360":
            try:
                return web_360_search(app_name,limmit_num)
            except:
                pass
        elif source == "qq":
            try:
                return web_qq_search(app_name,limmit_num)
            except:
                pass
        elif source == "Hippo" or source == "hippo":
            try:
                return hippo_search_easy(app_name)
            except:
                pass
        elif source == "Scoop":
            buckets_list_install = Scoop_buckets_load()
            return Scoop_search_lensi(app_name,buckets_list_install,limmit_num,SIP)
        elif source == "Choco":
            return choco_search(app_name,limmit_num)
        elif source == "Winget":
            return winget_search(app_name,limmit_num)

def Scoop_install_scoop_silence():
    scoop_install_all = open("scoop_install_all.ps1", "w")
    scoop_install_all.write("mkdir D:" + "\n" + "mkdir D:\Scoop" + "\n" + "mkdir D:\GlobalScoopApps" + "\n" + "mkdir D:\ScoopCache"+ "\n" + "Set-ExecutionPolicy RemoteSigned -scope CurrentUser;"+ "\n" + "$env:SCOOP='D:\Scoop'"+ "\n" + "[Environment]::SetEnvironmentVariable('SCOOP', $env:SCOOP, 'User')"+ "\n" + "$env:SCOOP_GLOBAL='D:\GlobalScoopApps'"+ "\n" + "[Environment]::SetEnvironmentVariable('SCOOP_GLOBAL', $env:SCOOP_GLOBAL, 'Machine')"+ "\n" + "$env:SCOOP_CACHE='D:\ScoopCache'"+ "\n" + "[Environment]::SetEnvironmentVariable('SCOOP_CACHE', $env:SCOOP_CACHE, 'Machine')"+ "\n" + "iwr -useb https://gitee.com/glsnames/scoop-installer/raw/master/bin/install.ps1 | iex"+ "\n" + "scoop config SCOOP_REPO 'https://gitee.com/glsnames/Scoop-Core'"+ "\n" + "scoop update"+ "\n" + "scoop install aria2 git sudo"+ "\n" + "scoop config aria2-split 16"+ "\n" + "scoop config aria2-max-connection-per-server 16"+ "\n" + "scoop bucket add main 'https://gitclone.com/github.com/ScoopInstaller/Main.git'"+ "\n" + "scoop bucket add extras 'https://gitee.com/xumuyao/scoop-extras.git'"+ "\n" + "scoop bucket add nonportable 'https://gitee.com/lane_swh/scoop-nonportable.git'"+ "\n" + "scoop bucket add games 'https://gitee.com/helloCodeke/scoop-games.git'"+ "\n" + "scoop bucket add java 'https://gitee.com/xumuyao/scoop-java.git'"+ "\n" + "scoop bucket add versions 'https://gitee.com/lane_swh/scoop-versions.git'"+ "\n" + "scoop bucket add scoopcn 'https://gitclone.com/github.com/scoopcn/scoopcn.git'"+ "\n" + "scoop bucket add apps 'https://gitee.com/kkzzhizhou/scoop-apps'"+ "\n" + "scoop bucket add nerd-fonts 'https://gitee.com/helloCodeke/scoop-nerd-fonts.git'"+ "\n" + "scoop bucket add scoopMain 'https://gitee.com/glsnames/scoop-main.git'"+ "\n" + "scoop update")
    scoop_install_all.close()
    os.system("powershell -File scoop_install_all.ps1 -NoProfile -WindowStyle Hidden")

def choco_install():
    choco_install = open("choco_install.ps1", "w")
    choco_install.write("mkdir D:\Choco_all" + "\n" + "$env:ChocolateyInstall='D:\Choco_all'"+ "\n"+"[Environment]::SetEnvironmentVariable('ChocolateyInstall', $env:ChocolateyInstall, 'User')"+"\n"+"Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))")
    choco_install.close()
    os.system("powershell -File choco_install.ps1 -NoProfile -WindowStyle Hidden")

def app_name_cmp(e):
    return e[7]

def create_shortcut_to_desktop(app_folder,file_name):  
    target = "D:\\Lensi\\APP_Portable\\" +app_folder + "\\" + file_name
    title = file_name
    s = os.path.basename(target)  
    fname = os.path.splitext(s)[0]  
    winshell.CreateShortcut(Path = os.path.join(winshell.desktop(), fname + '.lnk'),Target = target,Icon=(target, 0), Description=title)  

def create_shortcut_to_startup(app_folder,file_name):  
    target = "D:\\Lensi\\APP_Portable\\" +app_folder + "\\" + file_name
    title = file_name
    s = os.path.basename(target)  
    fname = os.path.splitext(s)[0] 
    winshell.CreateShortcut(Path = os.path.join(winshell.startup(),fname + '.lnk'),Target = target,Icon=(target, 0),Description=title) 

def create_shortcut_to_startmenu(app_folder,file_name):  
    target = "D:\\Lensi\\APP_Portable\\" +app_folder + "\\" + file_name
    title = file_name
    s = os.path.basename(target)  
    fname = os.path.splitext(s)[0] 
    Path = os.path.join(winshell.startup().strip("\Startup"),"Lensi Apps",fname + '.lnk')
    winshell.CreateShortcut(Path,Target = target,Icon=(target, 0),Description=title) 

def install(file_name,app_name,SO,app_source,app_version):
    os.chdir(lensi_path + "\Download")
    file_name_kinds = file_name[file_name.rfind("."):].strip(".")
    if SO != "True":
        if file_name_kinds == "zip":
            zip_file = zipfile.ZipFile(file_name)
            zip_file.extractall(lensi_path + "\APP_Portable\\" + app_name + "\\")
            file_list = zip_file.namelist()
            zip_file.close()
            file_name_exe = app_name + ".exe"
            file_name_real = process.extractOne(file_name_exe,file_list)[0]
            os.chdir(lensi_path + "\APP_Portable\\" + app_name)
            file_list_real = os.listdir()
            is_it_only_one_thing = 0
            # print(file_list_real)
            if len(file_list_real) == 1:
                if file_list_real[0].find(".") != -1:
                        is_it_only_one_thing = 1
            else:
                for i in range(0,len(file_list_real)-1):
                    if file_list_real[i].find(".") != -1:
                        is_it_only_one_thing = 1
            # print(file_list_real)
            if is_it_only_one_thing == 0:
                app_folder = app_name +"//" + file_list_real[0]
                # create_shortcut_to_startmenu(app_folder,file_name_real)
                if CDS == "True":
                    create_shortcut_to_desktop(app_folder,file_name_real)
                if CSS == "True":
                    create_shortcut_to_startmenu(app_folder,file_name_real)
            else:
                if CSS == "True":
                    create_shortcut_to_startmenu(app_name,file_name_real)
                if CDS == "True":
                    create_shortcut_to_desktop(app_name,file_name_real)
        elif file_name_kinds == "msi":
            cmd = "msiexec /i " + lensi_path + "\Download\\" + file_name + " /norestart /passive"
            # print(cmd)
            os.system(cmd)
        elif file_name_kinds == "exe":
            folder_path = "D:\Lensi\APP_Installed\\" + app_name
            try:
                os.mkdir(folder_path)
            except:
                pass
            exe_kind = "NSIS"
            if exe_kind == "NSIS":
                cmd = file_name + "/S /D=" + folder_path
                os.system(cmd)
        else:
            os.system(file_name)
    else:
        os.system(file_name)
    add_installed_app(app_name,app_source,app_version)

def DownloadandInstallFile(download_url,app_source,DAI,app_name,SO,app_version):
    save_url = lensi_path + "\Download"
    if app_source == "qq" or app_source == "360":
        file_name = download_url[download_url.rfind("/"):]
        file_name = file_name.strip("/")
    elif app_source == "hippo":
        file_name = download_url[download_url.rfind("="):]
        file_name = file_name.strip("=")
    if download_url is None or save_url is None or file_name is None:
        print('参数错误')
        return None
    if EAD == "True":
        print("Using Aria2")
        order = AP +' --dir=' +save_url +' --out=' + file_name +  ' --console-log-level=warn --allow-overwrite=true --split=16 --max-connection-per-server=16 --split=5 --no-conf=true --summary-interval=0 --min-split-size=20M "' + download_url + '"'
        os.system(order)
        print(file_name+' 下载完成！')
    else:
        res = requests.get(download_url,stream=True) 
        total_size = int(int(res.headers["Content-Length"])/1024+0.5)
        # 获取文件地址
        file_path = os.path.join(save_url, file_name)
        # 打开本地文件夹路径file_path，以二进制流方式写入，保存到本地
        with open(file_path, 'wb') as fd:
            print('开始下载文件：{},当前文件大小：{}KB'.format(file_name,total_size))
            for chunk in tqdm(iterable=res.iter_content(1024),total=total_size,unit='k',desc=None):
                fd.write(chunk)
            print(file_name+' 下载完成！')
    os.chdir(lensi_path + "\Download")
    install(file_name,app_name,SO,app_source,app_version)
    # os.system(file_name)
    os.chdir(lensi_path + "\Download")
    if DAI == "True":
        os.remove(file_name)

def Lensi_check_scoop():
    check_result = subprocess.getoutput('scoop -h')
    if check_result.find("不") != -1:
        return False
    else:
        return True
def Lensi_check_choco():
    check_result = subprocess.getoutput('choco -h')
    if check_result.find("不") != -1:
        return False
    else:
        return True

def DownloadFile_aria2(download_url,app_source):
    save_url = lensi_path + "\Download"
    if app_source == "qq" or app_source == "360":
        file_name = download_url[download_url.rfind("/"):]
        file_name = file_name.strip("/")
    elif app_source == "hippo":
        file_name = download_url[download_url.rfind("="):]
        file_name = file_name.strip("=")
    order = AP +' --dir=' +save_url +' --out=' + file_name +  ' --console-log-level=warn --allow-overwrite=true --split=16 --max-connection-per-server=16 --split=5 --no-conf=true --summary-interval=0 --min-split-size=20M "' + download_url + '"'
    os.system(order)
    print(file_name+' 下载完成！')
    os.system("start D:\Lensi\Download")

def DownloadFile(download_url,app_source):
    save_url = lensi_path + "\Download"
    if app_source == "qq" or app_source == "360":
        file_name = download_url[download_url.rfind("/"):]
        file_name = file_name.strip("/")
    elif app_source == "hippo":
        file_name = download_url[download_url.rfind("="):]
        file_name = file_name.strip("=")
    if download_url is None or save_url is None or file_name is None:
        print('参数错误')
        return None
    if EAD == "True":
        print("Using Aria2")
        order = AP +' --dir=' +save_url +' --out=' + file_name +  ' --console-log-level=warn --allow-overwrite=true --split=16 --max-connection-per-server=16 --split=5 --no-conf=true --summary-interval=0 --min-split-size=20M "' + download_url + '"'
        os.system(order)
        print(file_name+' 下载完成！')
        cmd = "start " + save_url
        os.system(cmd)
    else:
        res = requests.get(download_url,stream=True) 
        total_size = int(int(res.headers["Content-Length"])/1024+0.5)
        # 获取文件地址
        file_path = os.path.join(save_url, file_name)
        # 打开本地文件夹路径file_path，以二进制流方式写入，保存到本地
        with open(file_path, 'wb') as fd:
            print('开始下载文件：{},当前文件大小：{}KB'.format(file_name,total_size))
            for chunk in tqdm(iterable=res.iter_content(1024),total=total_size,unit='k',desc=None):
                fd.write(chunk)
            print(file_name+' 下载完成！')
        cmd = "start " + lensi_path + "\Download"
        os.system(cmd)

def Scoop_update():
    os.system("scoop update")

def pprint_easy(i,SIP="D:\Scoop"):
    print("From",i[8])
    print("App name:",i[0])
    print("App version:",i[1])
    print("App home:",i[3])
    print("App detail:",i[2])
    if i[8] == "Choco":
        Downloadfrom = "choco install " + i[5]
    elif i[8] == "Winget":
        Downloadfrom = "winget install --id " + i[5]
    elif i[8] == "Scoop":
        Downloadfrom = "scoop install " + SIP +"\\buckets\\" + i[0][:i[0].find('\\')] + "\\bucket\\" + i[0][i[0].find('\\'):].strip("\\") + ".json"
    else:
        Downloadfrom = i[5]
    print("Downloading from:",Downloadfrom)
    print("Installing from: lensi install",i[0],i[8])
    print("-------------------")

def get_all_installed_software():
    reg_root = win32con.HKEY_LOCAL_MACHINE
    reg_paths=[r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall",r"SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall",r"Software\Microsoft\Windows\CurrentVersion\Uninstall"]
    rst_list=[]
    for path in reg_paths:
        pkey = win32api.RegOpenKeyEx(reg_root,path)
        for item in win32api.RegEnumKeyEx(pkey):
            value_paths = path+"\\"+item[0]
            #print(value_paths)
            try:
                vkey = win32api.RegOpenKeyEx(reg_root,value_paths)
                DisplayName,key_type = win32api.RegQueryValueEx(vkey,"DisplayName")
                UninstallString,key_type = win32api.RegQueryValueEx(vkey,"UninstallString")
                #print({'name':DisplayName,'Uninstall string':UninstallString})
                rst_list.append((DisplayName,UninstallString))
                win32api.RegCloseKey(vkey)
            except:
                pass
        win32api.RegCloseKey(pkey)
    return rst_list

def get_software():
    rst_list = get_all_installed_software()
    rst =[]
    for each in rst_list:
        rst.append(each[0])
    return  rst

def uninstall_software(software_name):
    rst_list = get_all_installed_software()
    uninstall_string=""
    for each in rst_list:
        if each[0] == software_name:
            uninstall_string=each[1]
            break
    if uninstall_string=="":
        print("Not found installed program.")
        return
    else:
        uninstall_string = uninstall_string.replace('\\','\\\\')
        os.chdir("\\".join(uninstall_string.split('\\')[:-1]))
        cmd=uninstall_string.split('\\')[-1]
        print("Running",cmd,"in","\\".join(uninstall_string.split('\\')[:-1]))
        os.system(cmd)
        choice = input("Do you want to clean the folder(Y/N):")
        if choice == "Y" or choice == "y":
            try:
                shutil.rmtree("\\".join(uninstall_string.split('\\')[:-1]))
            except:
                pass

def add_installed_app(app_name,app_source,app_version=" "):
    os.chdir(lensi_path)
    f = open("app_list.txt","r")
    app_list = f.readlines()
    f.close()
    if len(app_list) == 0:
        with open("app_list.txt","w") as f:
            write_text = app_name + " " + app_version + " " + app_source + "\n"
            f.write(write_text)
            return
    app_list_real = []
    for i in app_list:
        if i.find("scoop") == -1 and i.find("choco") == -1 and i.find("winget") == -1 and i.find("Lensi") == -1:
            j=i.split()
            app_name_real = j[:len(j)-2]
            name = ""
            for k in app_name_real:
                name = name + k +" "
            name = name.strip(" ")
            del(j[:len(j)-2])
            j.insert(0,name)
            j[len(j)-1] = j[len(j)-1].replace("\n","")
            app_list_real.append(j)
    Has_yes = 0
    for i in range(0,len(app_list_real)):
        # print(app_list_real[i])
        # print(app_list_real[i][0])
        # print(app_name)
        # print(fuzz.partial_ratio(app_list_real[i][0],app_name))
        if fuzz.partial_ratio(app_list_real[i][0],app_name)>=HAF:
            app_list_real[i][0] = app_name
            app_list_real[i][1] = app_version
            app_list_real[i][2] = app_source
            Has_yes = 1
        app_list_real[i][0] = app_list_real[i][0]
    write_text = ""
    for i in range(0,len(app_list_real)):
        write_text = write_text + app_list_real[i][0] + " " + app_list_real[i][1] + " " + app_list_real[i][2] + "\n"
    if Has_yes == 0:
        write_text = write_text + app_name + " " + app_version + " " + app_source + "\n"
    write_text = "Lensi 0.1.2 pip\n" + write_text
    with open("app_list.txt","w") as f:
        f.write(write_text)

def get_app_installed():
    app_result = subprocess.getoutput("WMIC product get name")
    # print(app_result)
    app_list_get = app_result.split("\n")
    app_list = []
    for i in app_list_get:
        if i != '' and i != 'Name' and i != 'HOTKEY':
            app_list.append(i[:i.find("  ")])
    return app_list

def out_put_list():
    os.chdir(lensi_path)
    f = open("app_list.txt","r")
    app_list = f.readlines()
    f.close()
    app_list_real = []
    for i in app_list:
        if i.find("scoop") == -1 and i.find("choco") == -1 and i.find("winget") == -1 and i.find("Lensi") == -1 and i.find("lensi") == -1:
            j=i.split()
            app_name = j[:len(j)-2]
            name = ""
            for k in app_name:
                name = name + k +" "
            name = name.strip(" ")
            del(j[:len(j)-2])
            j.insert(0,name)
            j[len(j)-1] = j[len(j)-1].replace("\n","")
            del(j[len(j)-2])
            app_list_real.append(j)
    write_text = ""
    for i in range(0,len(app_list_real)):
        write_text = write_text + app_list_real[i][0] + " " + app_list_real[i][1] + "\n"
    os.chdir(path_now)
    with open("app_list.txt","w") as f:
        f.write(write_text)

def load_list_app_installed():
    os.chdir(lensi_path)
    f = open("app_list.txt","r")
    app_list = f.readlines()
    f.close()
    app_list_real = []
    for i in app_list:
        if i.find("scoop") == -1 and i.find("choco") == -1 and i.find("winget") == -1:
            j=i.split()
            app_name = j[:len(j)-2]
            name = ""
            for k in app_name:
                name = name + k +" "
            name = name.strip(" ")
            del(j[:len(j)-2])
            j.insert(0,name)
            j[len(j)-1] = j[len(j)-1].replace("\n","")
            app_list_real.append(j)
    return app_list_real

def in_put_list(file_name):
    os.chdir(path_now)
    f = open(file_name,"r")
    app_list = f.readlines()
    f.close()
    app_list_real = []
    for i in app_list:
        j=i.split()
        app_name = j[:len(j)-1]
        name = ""
        for k in app_name:
            name = name + k +" "
        name = name.strip(" ")
        del(j[:len(j)-1])
        j.insert(0,name)
        j[len(j)-1] = j[len(j)-1].replace("\n","")
        app_list_real.append(j)
    for i in app_list_real:
        search_list = lensi_search_all(i[1],i[0],1,SIP)
        if search_list != None:
            DownloadandInstallFile(search_list[0][5],search_list[0][8],DAI,search_list[0][0],SO,search_list[0][1])
        print(i[0],"is installed from",i[1])
    # print(app_list_real)
    

def Scoop_buckets_replace(Scoop_install_place,to_replace,replace_to):#遍历scoop bucket 存入csv中
    #简单来说就是获取每个buckets里bucket的文件
    Scoop_update()
    if not os.path.exists(Scoop_install_place + "\\buckets\\replaced\\bucket"):
        os.makedirs(Scoop_install_place + "\\buckets\\replaced\\bucket")
    cnt = 0
    os.chdir(Scoop_install_place+"\\buckets")
    buckets_names = os.listdir()
    for i in buckets_names:
        dir = Scoop_install_place + "\\buckets\\" + i + "\\bucket"
        os.chdir(dir)
        bucket_list = os.listdir()
        for j in bucket_list:
            try:
                with open(j,"r",encoding='utf-8') as f:
                    json_text = f.read()
                if json_text.find(to_replace) != -1:
                    json_text = json_text.replace(to_replace,replace_to)
                    cnt = cnt + 1
                    os.chdir(Scoop_install_place + "\\buckets\\replaced\\bucket")
                    with open(j,"w+") as f:
                        f.write(json_text)
                os.chdir(dir)
            except:
                pass
    return cnt

def json_buckets_replace(json_install_place,to_replace,replace_to):#遍历scoop bucket 存入csv中
    with open(json_install_place,"r",encoding='utf-8') as f:
        json_text = f.read()
    if json_text.find(to_replace) != -1:
        json_text = json_text.replace(to_replace,replace_to)
        with open(json_install_place,"w+") as f:
            f.write(json_text)

class Lensi(object):
    def __init__(self) -> None:
        try:
            global lensi_path,path_now
            lensi_path = "D:\Lensi"
            path_now = os.getcwd()
            if os.path.exists("D:\\") == False:
                lensi_path = "C:\Lensi"
            if os.path.exists(lensi_path) == False:
                os.mkdir(lensi_path)
            if os.path.exists(lensi_path + "\Download") == False:
                os.mkdir(lensi_path + "\Download")
                os.chdir(lensi_path)
                with open("app_list.txt","w+") as f:
                    f.write("Lensi 0.1.2 pip")
            if os.path.exists(lensi_path + "\APP_Portable") == False:
                os.mkdir(lensi_path + "\APP_Portable")
            if os.path.exists(lensi_path + "\APP_Installed") == False:
                os.mkdir(lensi_path + "\APP_Installed")
            os.chdir(lensi_path)
            Lensi_config = configparser.ConfigParser()
            global EW,qq_num,baoku_num,DAI,SO,ES,EC,EW,SIP,WT,scoop_num,choco_num,winget_num,buckets_list_install,NI,init_text,HAF,EAD,AP,CDS,CSS,TR,RT
            init_text = "[Lensi]\nqq_num = 1\n360_num = 1\nscoop_num = 1\nwinget_num = 1\nchoco_num = 1\nDAI(DeletedAfterInstalled) = True\nSO(SimplyOpen) = False\nES(EnableScoop) = True\nEC(EnableChoco) = True \nEW(EnableWinget) = True\nSIP(ScoopInstallPath) = D:\\Scoop\nNI(NormalInstall)=qq\nWT(WaitTime)=3\nHAF(HowAccurateFuzzywuzzy)=80\nEAD(EnableAria2Download)= False\nAP(Aria2Path)=D:\Scoop\shims\aria2c.exe\nCDS(CreateDesktopShotcut) = True\nCSS(CreateStartmenuShotcut) = False\nTR(ToReplace)=github.com\nRT(ReplaceTo)=hub.fastgit.xyz"
            Lensi_config.read("config.ini", encoding="utf-8")
            qq_num = Lensi_config.getint("Lensi", "qq_num")
            baoku_num = Lensi_config.getint("Lensi", "360_num")
            scoop_num = Lensi_config.getint("Lensi", "scoop_num")
            choco_num = Lensi_config.getint("Lensi", "choco_num")
            winget_num = Lensi_config.getint("Lensi", "winget_num")
            DAI = Lensi_config.get("Lensi","DAI(DeletedAfterInstalled)")
            SO = Lensi_config.get("Lensi","SO(SimplyOpen)")
            ES = Lensi_config.get("Lensi","ES(EnableScoop)")
            EC = Lensi_config.get("Lensi","EC(EnableChoco)")
            EW = Lensi_config.get("Lensi","EW(EnableWinget)") 
            SIP = Lensi_config.get("Lensi","SIP(ScoopInstallPath)")
            NI = Lensi_config.get("Lensi","NI(NormalInstall)")
            WT = Lensi_config.get("Lensi","WT(WaitTime)")
            HAF = Lensi_config.getint("Lensi","HAF(HowAccurateFuzzywuzzy)")
            EAD = Lensi_config.get("Lensi","EAD(EnableAria2Download)")
            AP = Lensi_config.get("Lensi","AP(Aria2Path)")
            CDS = Lensi_config.get("Lensi","CDS(CreateDesktopShotcut)")
            CSS = Lensi_config.get("Lensi","CSS(CreateStartmenuShotcut)")
            TR = Lensi_config.get("Lensi","TR(ToReplace)")
            RT = Lensi_config.get("Lensi","RT(ReplaceTo)")
        except:
            print("Initing the config.ini")
            os.chdir(lensi_path)
            f = open("config.ini","w",encoding="utf-8")
            f.write(init_text)
            f.close()
            Lensi_config = configparser.ConfigParser()
            os.chdir(lensi_path)
            Lensi_config.read("config.ini", encoding="utf-8")
        finally:
            qq_num = Lensi_config.getint("Lensi", "qq_num")
            baoku_num = Lensi_config.getint("Lensi", "360_num")
            scoop_num = Lensi_config.getint("Lensi", "scoop_num")
            choco_num = Lensi_config.getint("Lensi", "choco_num")
            winget_num = Lensi_config.getint("Lensi", "winget_num")
            DAI = Lensi_config.get("Lensi","DAI(DeletedAfterInstalled)")
            SO = Lensi_config.get("Lensi","SO(SimplyOpen)")
            ES = Lensi_config.get("Lensi","ES(EnableScoop)")
            EC = Lensi_config.get("Lensi","EC(EnableChoco)")
            EW = Lensi_config.get("Lensi","EW(EnableWinget)") 
            SIP = Lensi_config.get("Lensi","SIP(ScoopInstallPath)")
            NI = Lensi_config.get("Lensi","NI(NormalInstall)")
            WT = Lensi_config.getint("Lensi","WT(WaitTime)")
            HAF = Lensi_config.getint("Lensi","HAF(HowAccurateFuzzywuzzy)")
            EAD = Lensi_config.get("Lensi","EAD(EnableAria2Download)")
            AP = Lensi_config.get("Lensi","AP(Aria2Path)")
            CDS = Lensi_config.get("Lensi","CDS(CreateDesktopShotcut)")
            CSS = Lensi_config.get("Lensi","CSS(CreateStartmenuShotcut)")
            TR = Lensi_config.get("Lensi","TR(ToReplace)")
            RT = Lensi_config.get("Lensi","RT(ReplaceTo)")
            start_menu = winshell.startup().replace("Startup","Lensi Apps")
            # print(start_menu)
            if os.path.exists(start_menu) == False and CSS == "True":
                os.mkdir(start_menu)
            if Lensi_check_choco() == False:
                print("Didn't install choco")
                EC = "F"
            if Lensi_check_scoop() == False:
                print("Didn't install scoop")
                ES = "F"
            else:
                Scoop_buckets_save(SIP)
                buckets_list_install = Scoop_buckets_load()

    def info(self,app_name,app_source="all"):
        if app_source == "all":
            print("From QQ")
            try:
                qq_id = web_qq_search(app_name,1)[0][4]
            except:
                print("None")
            else:
                print(web_qq_info(qq_id))
            print("-------------------")
            print("From 360")
            try:
                baoku_id = web_360_search("360",app_name,1)[0][4]
            except:
                print("None")
            else:
                print(web_baoku_info(baoku_id))
            print("-------------------")
            print("From Hippo")
            try:
                print(web_hippo_info(app_name))
            except:
                print("None")
            print("-------------------")
            print("From Scoop")
            Scoop_info(app_name)
            print("From Choco")
            print("-------------------")
            choco_info(app_name)
            print("-------------------")
            print("From Winget")
            try:
                winget_id  = winget_search(app_name,1)[0][4]
            except:
                print("None")
            else:
                print(winget_info_id(winget_id))
        elif app_source == "qq":
            print("QQ")
            try:
                qq_id = web_qq_search(app_name,1)[0][4]
            except:
                print("None")
            else:
                print(web_qq_info(qq_id))
        elif app_source == "360":
            print("360")
            try:
                baoku_id = web_360_search("360",app_name,1)[0][4]
            except:
                print("None")
            else:
                print(web_baoku_info(baoku_id))
        elif app_source == "hippo" or app_source == "Hippo":
            print("Hippo")
            try:
                print(web_hippo_info(app_name))
            except:
                print("None")
        elif app_source == "choco":
            choco_info(app_name)
        elif app_source == "scoop":
            Scoop_info(app_name)
        elif app_source == "winget":
            try:
                winget_id  = winget_search(app_name,1)[0][4]
            except:
                print("None")
            else:
                winget_info_id(winget_id)

    def install(self,app_name,app_source="all"):
        os.chdir(path_now)
        if app_name == "scoop" or app_name == "Scoop":
            Scoop_install_scoop_silence()
        elif app_name == "choco" or app_name == "Choco":
            choco_install()
        elif app_name.find("\\") != -1 and app_name.find(".") == -1:
            print("Installing from scoop")
            app_name = SIP +"\\buckets\\" + app_name[:app_name.find('\\')] + "\\bucket\\" + app_name[app_name.find('\\'):].strip("\\") + ".json"
            json_buckets_replace(app_name,TR,RT)
            Scoop_install_app(app_name)
            json_buckets_replace(app_name,RT,TR)
            add_installed_app(app_name,"Scoop")
        elif os.path.exists(app_name) or app_name.find(".\\") != -1:
            print("Installing from",app_name)
            in_put_list(app_name)
        else:
            if app_source == "all":
                if NI == "Hippo" or NI=="hippo" or app_source == "h":
                    try:
                        print("Downloading from Hippo")
                        search_result = hippo_search_easy(app_name)
                        download_url = search_result[0][5]
                        app_name_real = search_result[0][0]
                        app_version = search_result[0][1]
                        # print(download_url)
                        DownloadandInstallFile(download_url,"hippo",DAI,app_name_real,SO,app_version)
                    except:
                        print("Hippo failed")
                        print("Downloading from QQ")
                        search_result =web_qq_search(app_name,1)
                        download_url = search_result[0][5]
                        app_name_real = search_result[0][0]
                        app_version = search_result[0][1]
                        DownloadandInstallFile(download_url,"qq",DAI,app_name_real,SO,app_version)
                elif NI == "360" or NI == "b":
                    print("Downloading from 360")
                    search_result = web_360_search(app_name,1)
                    download_url = search_result[0][5]
                    app_name_real = search_result[0][0]
                    app_version = search_result[0][1]
                    DownloadandInstallFile(download_url,"360",DAI,app_name_real,SO,app_version)
                elif NI == "qq" or NI == "q":
                    print("Downloading from QQ")
                    search_result = web_qq_search(app_name,1)
                    download_url = search_result[0][5]
                    app_name_real = search_result[0][0]
                    app_version = search_result[0][1]
                    DownloadandInstallFile(download_url,"qq",DAI,app_name_real,SO,app_version)
                elif ES == "True" and NI == "scoop" or NI == "s" or NI == "Scoop":
                    print("Installing from scoop")
                    if app_name.find("\\") != -1:
                        app_name = SIP +"\\buckets\\" + app_name[:app_name.find('\\')] + "\\bucket\\" + app_name[app_name.find('\\'):].strip("\\") + ".json"
                    Scoop_install_app(app_name)
                    add_installed_app(app_name,"Scoop")
                elif EC == "True" and NI == "choco" or NI == "c" or NI == "Choco":
                    print("Installing from choco")
                    choco_install_app(app_name)
                    add_installed_app(app_name,"choco")
                elif EW == "True" and NI == "winget" or NI == "w" or NI == "Winget":
                    print("Installing from winget")
                    try:
                        winget_id  = winget_search(app_name,1)[0][4]
                    except:
                        print("None")
                    else:
                        winget_install_app_id(winget_id)
                        add_installed_app(app_name,"winget")
                else:
                    print("Sorry. Lensi doesn't support this source now. /(ㄒoㄒ)/~~")
            elif app_source == "360" or app_source == "b":
                print("Downloading from 360")
                search_result = web_360_search(app_name,1)
                download_url = search_result[0][5]
                app_name_real = search_result[0][0]
                app_version = search_result[0][1]
                DownloadandInstallFile(download_url,"360",DAI,app_name_real,SO,app_version)
            elif app_source == "qq" or app_source == "q":
                print("Downloading from QQ")
                search_result = web_qq_search(app_name,1)
                download_url = search_result[0][5]
                app_name_real = search_result[0][0]
                app_version = search_result[0][1]
                DownloadandInstallFile(download_url,"qq",DAI,app_name_real,SO,app_version)
            elif app_source == "hippo" or app_source == "h":
                print("Downloading from Hippo")
                search_result = hippo_search_easy(app_name)
                download_url = search_result[0][5]
                app_name_real = search_result[0][0]
                app_version = search_result[0][1]
                # print(download_url)
                DownloadandInstallFile(download_url,"hippo",DAI,app_name_real,SO,app_version)
            elif ES == "True" and app_source == "scoop" or app_source == "s" or app_source == "Scoop":
                print("Installing from scoop")
                if app_name.find("\\") != -1:
                    app_name = SIP +"\\buckets\\" + app_name[:app_name.find('\\')] + "\\bucket\\" + app_name[app_name.find('\\'):].strip("\\") + ".json"
                    json_buckets_replace(app_name,TR,RT)
                    Scoop_install_app(app_name)
                    json_buckets_replace(app_name,RT,TR)
                else:
                    Scoop_install_app(app_name)
                add_installed_app(app_name,"Scoop")
            elif EC == "True" and app_source == "choco" or app_source == "c" or app_source == "Choco":
                print("Installing from choco")
                choco_install_app(app_name)
                add_installed_app(app_name,"choco")
            elif EW == "True" and app_source == "winget" or app_source == "w" or app_source=="Winget":
                print("Installing from winget")
                try:
                    winget_id  = winget_search(app_name,1)[0][4]
                except:
                    print("None")
                else:
                    winget_install_app_id(winget_id)
                    add_installed_app(app_name,"winget")
            else:
                print("Sorry. Lensi doesn't support this source now. /(ㄒoㄒ)/~~")

    def download(self,app_name,app_source="all"):
        if app_source == "all":
            if NI == "qq" or NI == "q":
                print("Downloading from QQ")
                download_url = web_qq_search(app_name,1)[0][5]
                DownloadFile(download_url,"qq")
            elif NI == "360" or NI == "b":
                print("Downloading from 360")
                download_url = web_360_search(app_name,1)[0][5]
                DownloadFile(download_url,"360")
            elif NI == "hippo" or NI == "h" or NI == "Hippo":
                print("Downloading from Hippo")
                download_url = hippo_search_easy(app_name)[0][5]
                # print(download_url)
                DownloadFile(download_url,"hippo")
            elif NI == "scoop" or NI == "scoop" or NI == "winget" or NI == "s" or NI == "w" or NI == "c":
                print("How to download things from scoop or choco or winget?")
                print("Use install!")
            else:
                print("Sorry. Lensi doesn't support this source now. /(ㄒoㄒ)/~~")
        elif app_source == "360" or app_source == "b":
            print("Downloading from 360")
            download_url = web_360_search(app_name,1)[0][5]
            DownloadFile(download_url,"360")
        elif app_source == "qq" or app_source == "q":
            print("Downloading from QQ")
            download_url = web_qq_search(app_name,1)[0][5]
            DownloadFile(download_url,"qq")
        elif app_source == "hippo" or app_source == "h":
            print("Downloading from Hippo")
            download_url = hippo_search_easy(app_name)[0][5]
            # print(download_url)
            DownloadFile(download_url,"hippo")
        else:
            print("Sorry. Lensi doesn't support this source now. /(ㄒoㄒ)/~~")


    def search(self,app_name,app_source="all",limmit_num = 0):
        app_source = str(app_source)
        limmit_num = int(limmit_num)
        if app_source == "all" and limmit_num == 0:
            if app_name == "Lensi" or app_name == "lensi":
                print("? You have installed it ,haven't you ?")
                return 
            if app_name == "Lensit":
                print("QEIE1284213AAUEUUQQ")
                print("I don't know what it means. It is probably a BUG.")
            thread_360 = myThread_search("360", app_name,baoku_num)
            thread_qq = myThread_search("qq", app_name,qq_num)
            thread_H = myThread_search("Hippo", app_name,1)
            #多线程
            search_result = []
            # 开启新线程
            thread_360.setDaemon(True)
            thread_qq.setDaemon(True)
            thread_H.setDaemon(True)
            thread_360.start()
            thread_qq.start()
            thread_H.start()
            if WT>0:
                thread_360.join(timeout=WT)
                thread_qq.join(timeout=WT)
                thread_H.join(timeout=WT)
            else:
                thread_360.join()
                thread_qq.join()
                thread_H.join()

            if ES == "True":
                thread_S = myThread_search( "Scoop", app_name,scoop_num,SIP)
                thread_S.setDaemon(True)
                thread_S.start()
                if WT>0:
                    thread_S.join(timeout=WT)
                else:
                    thread_S.join()
            if EC == "True":
                thread_C = myThread_search( "Choco", app_name,choco_num)
                thread_C.setDaemon(True)
                thread_C.start()
                if WT>0:
                    thread_C.join(timeout=WT)
                else:
                    thread_C.join()

            if EW == "True":
                thread_W = myThread_search( "Winget", app_name,winget_num)
                thread_W.setDaemon(True)
                thread_W.start()
                if WT>0:
                    thread_W.join(timeout=WT)
                else:
                    thread_W.join()   
            #等待进程
            # print ("退出主线程")
            #判断结果是否为空
            if thread_360.get_result() != None :
                search_result.extend(thread_360.get_result())
            if thread_qq.get_result() != None :
                search_result.extend(thread_qq.get_result())  
            if thread_H.get_result() != None :  
                search_result.extend(thread_H.get_result())
            try:
                if thread_S.get_result() != None :  
                    search_result.extend(thread_S.get_result())
            except:
                pass
            try:
                if thread_W.get_result() != None :  
                    search_result.extend(thread_W.get_result())
            except:
                pass
            try:
                if thread_C.get_result() != None :  
                    search_result.extend(thread_C.get_result())
            except:
                pass
            # pprint_easy(search_result)
            search_result.sort(key=app_name_cmp,reverse=True)
            for i in search_result:
                pprint_easy(i,SIP)
            print("That's all! o(*￣▽￣*)ブ")
        elif app_source == "360"or app_source == "b":
            if limmit_num == 0:
                search_result = web_360_search(app_name,baoku_num)
                for i in search_result:
                    pprint_easy(i)
                print("That's all! o(*￣▽￣*)ブ")
            else:
                search_result = web_360_search(app_name,limmit_num)
                for i in search_result:
                    pprint_easy(i)
                print("That's all! o(*￣▽￣*)ブ")
        elif app_source == "qq"or app_source == "q":
            if limmit_num == 0:
                search_result = web_qq_search(app_name,qq_num)
                for i in search_result:
                    pprint_easy(i)
                print("That's all! o(*￣▽￣*)ブ")
            else:
                search_result = web_qq_search(app_name,limmit_num)
                for i in search_result:
                    pprint_easy(i)
                print("That's all! o(*￣▽￣*)ブ")
        elif app_source == "hippo"or app_source == "h":
            search_result = hippo_search_easy(app_name)
            for i in search_result:
                pprint_easy(i)
            print("That's all! o(*￣▽￣*)ブ")
        elif app_source == "scoop" or  app_source == "s":
            if limmit_num == 0:
                search_result = Scoop_search_lensi(app_name,buckets_list_install,scoop_num,SIP)
                for i in search_result:
                    pprint_easy(i,SIP)
                print("That's all! o(*￣▽￣*)ブ")
            else:
                search_result = Scoop_search_lensi(app_name,buckets_list_install,limmit_num,SIP)
                for i in search_result:
                    pprint_easy(i,SIP)
                print("That's all! o(*￣▽￣*)ブ")
        elif app_source == "choco" or  app_source == "c":
            if limmit_num == 0:
                search_result = choco_search(app_name,choco_num)
                for i in search_result:
                    pprint_easy(i)
                print("That's all! o(*￣▽￣*)ブ")
            else:
                search_result = choco_search(app_name,limmit_num)
                for i in search_result:
                    pprint_easy(i)
                print("That's all! o(*￣▽￣*)ブ")
        elif app_source == "winget" or  app_source == "w":
            if limmit_num == 0:
                search_result = winget_search(app_name,winget_num)
                for i in search_result:
                    pprint_easy(i)
                print("That's all! o(*￣▽￣*)ブ")
            else:
                search_result = winget_search(app_name,limmit_num)
                for i in search_result:
                    pprint_easy(i)
                print("That's all! o(*￣▽￣*)ブ")
        else:
            print("Sorry. Lensi doesn't support this source now. /(ㄒoㄒ)/~~")

    def upgrade(self,app_name="all"):
        if app_name == "all":
            real_app_update = load_list_app_installed()
            for i in real_app_update:
                search_list = lensi_search_all(i[2],i[0],1,SIP)
                if search_list != None:
                    if fuzz.partial_ratio(search_list[0][0],i[0]) >= HAF:
                        if search_list[0][1] != i[1]:
                            DownloadandInstallFile(search_list[0][5],search_list[0][8],DAI,search_list[0][0],SO,search_list[0][1])
                        else:
                            pass
        else:
            app_installed = load_list_app_installed()
            app_installed_name = []
            for i in app_installed:
                app_installed_name.append(i[0])
            app_name_real = process.extractOne(app_name,app_installed_name)[0]
            has_yes = 0
            real_app_update = []
            for i in app_installed:
                if i[0] == app_name_real:
                    real_app_update = i 
                    break
            search_list = lensi_search_all(real_app_update[2],app_name,1,SIP)
            if search_list != None:
                if fuzz.partial_ratio(search_list[0][0],real_app_update[0]) >= HAF:
                    if search_list[0][1] != real_app_update[1]:
                        DownloadandInstallFile(search_list[0][5],search_list[0][8],DAI,search_list[0][0],SO,search_list[0][1])
                    else:
                        print("It is the latest version! ")
                    has_yes = 1
            if has_yes == 0:
                print("You probably didn't install this app.")
                print("Use lensi install",app_name,"to install")

    def clean(self):
        shutil.rmtree(lensi_path + "\Download")
        os.mkdir(lensi_path + "\Download")
        print("Has cleaned D:\Lensi\Download")
    
    def set(self,options="help",le_set=0):
        le_set =str(le_set)
        if options == "init":
            try:
                os.mkdir(lensi_path)
            except:
                pass
            try:
                os.mkdir(lensi_path + "\Download")
            except:
                    pass
            try:
                os.mkdir(lensi_path + "\APP_Installed")
            except:
                    pass
            try:
                os.mkdir(lensi_path + "\APP_Portable")
            except:
                    pass
            # try:
            #     os.mkdir(winshell.startup().replace("Startup","Lensi Apps"))
            # except:
            #         pass
            os.chdir(lensi_path)
            f = open("config.ini","w",encoding="utf-8")
            f.write(init_text)
            f.close()
        else:
            Lensi_config = configparser.ConfigParser()
            os.chdir(lensi_path)
            Lensi_config.read("config.ini", encoding="utf-8")
            if options == "qq_num" or options =="qq" or options =="q":
                Lensi_config.set("Lensi","qq_num",le_set)
            elif options == "baoku_num" or options =="360_num" or options =="b":
                Lensi_config.set("Lensi","360_num",le_set)
            elif options == "DAI" or options == "DeletedAfterInstalled" or options =="dai":
                Lensi_config.set("Lensi", "DAI(DeletedAfterInstalled)",le_set)
            elif options == "SO" or options == "SimplyOpen" or options =="so":
                Lensi_config.set("Lensi", "SO(SimplyOpen)",le_set)
            elif options == "ES" or options == "EnableScoop" or options =="es":
                Lensi_config.set("Lensi", "ES(EnableScoop)",le_set)
            elif options == "EC" or options == "EnableChoco" or options =="ec":
                Lensi_config.set("Lensi", "EC(EnableChoco)",le_set)
            elif options == "EW" or options == "EnableWinget" or options == "ew":
                Lensi_config.set("Lensi", "EW(EnableWinget)",le_set)
            elif options == "choco_num" or options =="c" or options =="choco":
                Lensi_config.set("Lensi", "choco_num",le_set)
            elif options == "winget_num" or options =="w" or options =="winget":
                Lensi_config.set("Lensi", "winget_num",le_set)
            elif options == "scoop_num" or options =="s" or options =="scoop":
                Lensi_config.set("Lensi", "scoop_num",le_set)
            elif options == "NI" or options =="ni":
                Lensi_config.set("Lensi", "NI(NormalInstall)",le_set)
            elif options == "WT" or options =="wt":
                Lensi_config.set("Lensi", "WT(WaitTime)",le_set)
            elif options == "HAF" or options =="haf":
                Lensi_config.set("Lensi", "HAF(HowAccurateFuzzywuzzy)",le_set)    
            elif options == "EAD" or options =="ead":
                Lensi_config.set("Lensi", "EAD(EnableAria2Download)",le_set)    
            elif options == "AP" or options =="ap":
                Lensi_config.set("Lensi", "AP(Aria2Path)",le_set)    
            elif options == "CDS" or options =="cds":
                Lensi_config.set("Lensi", "CDS(CreateDesktopShotcut)",le_set) 
            elif options == "CSS" or options =="css":
                Lensi_config.set("Lensi", "CSS(CreateStartmenuShotcut)",le_set)
            elif options == "TR" or options =="tr":
                Lensi_config.set("Lensi", "TR(ToReplace)",le_set)
            elif options == "RT" or options =="rt":
                Lensi_config.set("Lensi", "RT(ReplaceTo)",le_set) 
            elif options == "help":
                os.chdir(lensi_path)
                f = open("config.ini","r")
                print(f.read())
                f.close()
                print("The available source is : qq(q) 360(b) scoop(s) hippo(h) choco(c) winget(w)")
            else:
                print("Sorry, Lensi didn't have this setting.")
            Lensi_config.write(open("config.ini", "w"))

    def uninstall(self,app_name,app_source="web"):
        if app_name == "lensi" or app_name == "Lensi":
            try:
                shutil.rmtree(lensi_path)
            except:
                pass
            os.system("pip uninstall lensi")
        if app_source == "web":
            print("Using util.")
            softwares=get_software()
            # print(softwares)
            app_name_real = process.extractOne(app_name,softwares)[0]
            print("Please check it carefully.")
            out_put = "Uninstalling " + app_name_real + " (Y/N)"
            result = input(out_put)
            if result == "Y" or result == "y":
                uninstall_software(app_name_real)
                add_uninstall_app(app_name)
                try:
                    portable_list = os.listdir(lensi_path + "\APP_Portable")
                    install_list =  os.listdir(lensi_path + "\APP_Installed")
                    if portable_list != []:
                        app_name_chose_p = process.extractOne(app_name,portable_list)[0]
                        if fuzz.partial_ratio(app_name,app_name_chose_p) >= HAF:
                            app_path = lensi_path + "\APP_Portable\\" + app_name_chose_p
                            output = "Move " + app_path + "?(Y/N)"
                            choice = input(output)
                            if choice == "Y" or choice == "y":
                                shutil.rmtree(app_path)
                    if install_list != []:
                        app_name_chose_i = process.extractOne(app_name,install_list)[0]
                        if fuzz.partial_ratio(app_name,app_name_chose_i) >= HAF:
                            app_path = lensi_path + "\APP_Installed\\" + app_name_chose_i
                            output = "Move " + app_path + "?(Y/N)"
                            choice = input(output)
                            if choice == "Y" or choice == "y":
                                shutil.rmtree(app_path)
                except:
                    pass
            else:
                try:
                    portable_list = os.listdir(lensi_path + "\APP_Portable")
                    install_list =  os.listdir(lensi_path + "\APP_Installed")
                    if portable_list != []:
                        app_name_chose_p = process.extractOne(app_name,portable_list)[0]
                        if fuzz.partial_ratio(app_name,app_name_chose_p) >= HAF:
                            app_path = lensi_path + "\APP_Portable\\" + app_name_chose_p
                            output = "Move " + app_path + "?(Y/N)"
                            choice = input(output)
                            if choice == "Y" or choice == "y":
                                shutil.rmtree(app_path)
                                add_uninstall_app(app_name)
                    if install_list != []:
                        app_name_chose_i = process.extractOne(app_name,install_list)[0]
                        if fuzz.partial_ratio(app_name,app_name_chose_i) >= HAF:
                            app_path = lensi_path + "\APP_Installed\\" + app_name_chose_i
                            output = "Move " + app_path + "?(Y/N)"
                            choice = input(output)
                            if choice == "Y" or choice == "y":
                                shutil.rmtree(app_path)
                                add_uninstall_app(app_name)
                except:
                    pass 
        elif app_source == "S" or "scoop" or "s":
            Scoop_uninstall_app(app_name)
        elif app_source == "C" or "choco" or "c":
            choco_uninstall_app(app_name)
        elif app_source == "W" or "winget" or "w":
            winget_uninstall_app(app_name)
        else:
            print("Sorry. Lensi doesn't support this source now. /(ㄒoㄒ)/~~")

    def list(self,options="list"):
        if options=="out":
            out_put_list()
        else: 
            os.chdir(lensi_path)
            f = open("app_list.txt","r")
            print(f.read())
            f.close()
            print("In",lensi_path,"\APP_Portable")
            print(os.listdir(lensi_path + "\APP_Portable"))
            print("In",lensi_path,"\APP_Installed")
            print(os.listdir(lensi_path + "\APP_Installed"))
    
    def init(self):
        choice = input("Do you really want to clean everything?(Y/N)")
        if choice == "y" or choice =="Y":
            try:
                shutil.rmtree(lensi_path)
            except:
                pass
            print("Has cleaned",lensi_path)
    
    # def replace(self,to_replace="TR",replace_to="RT"):
    #     if to_replace=="TR" or replace_to=="RT":
    #         to_replace = TR
    #         replace_to = RT
    #     cnt = Scoop_buckets_replace(SIP,to_replace,replace_to)
    #     print("Has replace",cnt,to_replace,"to",replace_to)


def main():
    fire.Fire(Lensi)

if __name__ == '__main__':
    fire.Fire(Lensi)