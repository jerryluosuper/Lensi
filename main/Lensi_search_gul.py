'''
Author: your name
Date: 2022-03-14 20:43:31
LastEditTime: 2022-03-16 14:27:28
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \Lensi\Lensi_search.py
'''
# -*- coding: utf-8 -*-
import json
import pprint
import threading
import os
import urllib
from urllib import request
from urllib.parse import quote 
from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
import subprocess
import codecs
from fuzzywuzzy import process
from xpinyin import Pinyin 

# 输出格式 ：[app_name,version,home_url,(description,)info_ID,(download_ID,source)can't see]
# TODO 添加description

exitFlag = 0

class myThread (threading.Thread):
    def __init__(self, source, app_name,limit_num=3):
        threading.Thread.__init__(self)
        self.source = source
        self.app_name = app_name
        self.limit_num = limit_num
    def run(self):
        # print ("开始线程：" + self.app_name)
        self.result = lensi_search_all(self.source,self.app_name,self.limit_num)
        # print ("退出线程：" + self.app_name)
    def get_result(self):  
        try:  
            return self.result  
        except Exception as e:  
            return None  

def web_360_search(app_name,limmit_num):
    headers = {'User-Agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763'}
    # app_name = app_name.encode('unicode_escape').decode('utf-8')
    app_name_search = quote(app_name)
    # app_name = "geek"
    baoku_search_url = 'https://bapi.safe.360.cn/soft/search?keyword='+ app_name_search + '&page=1'
    baoku_html_req = request.Request(url=baoku_search_url,headers=headers)
    baoku_html = urlopen(baoku_html_req)
    baoku_soup = BeautifulSoup(baoku_html.read(),"html.parser")
    baoku_str = str(baoku_soup)
    # print(baoku_str)
    '''
    TODO 未使用正则表达式 待优化
    '''
    # print(baoku_str)
    baoku_name_search_1 = 0
    baoku_version_search_1 = 0
    baoku_download_search_1 =0 
    baoku_id_search_1 = 0 
    '''
    TODO 未使用正则表达式 待优化
    '''
    baoku_search_all_list = []
    # print(baoku_str)
    limmit_num_search = baoku_str.count('{"softid":')
    limmit_num_real = min(limmit_num,limmit_num_search)
    for i in range(0,limmit_num_real):
        baoku_name_search = baoku_str.find('"softname":"',baoku_name_search_1)
        baoku_name_search_1 = baoku_name_search + 1
        baoku_name = baoku_str[baoku_name_search:int(baoku_str.find(',',baoku_name_search))].strip('"softname":"')
        if baoku_name == '':
            return baoku_search_all_list
        baoku_version_search = baoku_str.find('"version":"',baoku_version_search_1)
        baoku_version_search_1 = baoku_version_search + 1
        baoku_download_search = baoku_str.find('"soft_download":"',baoku_download_search_1)
        baoku_download_search_1 = baoku_download_search + 1
        baoku_id_search = baoku_str.find('[{"softid":',baoku_id_search_1)
        baoku_id_search_1 = baoku_id_search + 1
        baoku_version= baoku_str[baoku_version_search:int(baoku_str.find(',',baoku_version_search))].strip('"version":"')
        baoku_download = baoku_str[baoku_download_search:int(baoku_str.find(',',baoku_download_search))].strip('"soft_download":"')
        baoku_id = baoku_str[baoku_id_search :int(baoku_str.find(',',baoku_id_search ))].strip('[{"softid":')
        baoku_download_url = baoku_download.replace('\\',"")
        baoku_search_all = [baoku_name.strip(",").encode('ascii').decode('unicode_escape'),baoku_version.strip(","),baoku_id,baoku_download_url.strip(","),"360"]
        baoku_search_all_list.append(baoku_search_all)
    return baoku_search_all_list

# def web_qq_search(app_name):
#     headers = {'User-Agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763'}
#     # app_name = "geek"
#     app_name = app_name.encode('unicode_escape').decode('ascii')
#     qq_search_url = 'https://s.pcmgr.qq.com/tapi/web/searchcgi.php?type=search&callback=searchCallback&keyword='+ app_name +'&page=1&pernum=1&more=0'
#     qq_html_req = request.Request(url=qq_search_url,headers=headers)
#     qq_html = urlopen(qq_html_req)
#     qq_soup = BeautifulSoup(qq_html.read(),"html.parser")
#     qq_str = str(qq_soup)
#     '''
#     TODO 未使用正则表达式 待优化
#     '''
#     # print(qq_str)
#     qq_name = qq_str[int(qq_str.find('<![CDATA[')):int(qq_str.find("]",qq_str.find("<![CDATA[")))].strip("<![CDATA[")
#     if qq_name == '':
#         qq_search_all = None
#         return qq_search_all
#     qq_version = qq_str[int(qq_str.find('<versionname>')):int(qq_str.find("&lt",qq_str.find("<versionname>")))].strip("<versionname>")
#     qq_download = qq_str[int(qq_str.find('[CDATA[http:')):int(qq_str.find("]",qq_str.find("[CDATA[http:")))].strip("![CDATA[")
#     qq_id = qq_str[int(qq_str.find('{"SoftID":"')):int(qq_str.find(',',qq_str.find('{"SoftID":"')))].strip('{"SoftID":"')
#     qq_download_url = qq_download.replace('\\',"")
        # qq_search_all = [[qq_name.encode('ascii').decode('unicode_escape'),qq_version,qq_id,qq_download_url],"qq"]
        # return qq_search_all
#     # print (qq_name,"\n","Version:",qq_version,"\n",qq_download_url,"\n")

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
    limmit_num_real = min(limmit_num,qq_str.count('<versionname>'))
    for i in range(0,limmit_num_real):
        if i == 0:
            qq_name_find = qq_str.find('<![CDATA[',qq_name_find_1)
            qq_name_find_1 = qq_name_find + 1
        else:
            for j in range(0,7):
                qq_name_find = qq_str.find('<![CDATA[',qq_name_find_1)
                qq_name_find_1 = qq_name_find + 1
            # print(qq_name_find)
        qq_version_find = int(qq_str.find('<versionname>',qq_version_find_1))
        qq_version_find_1 = qq_version_find + 1
        # print(qq_name_find)
        qq_download_find = qq_str.find('[CDATA[http:',qq_download_find_1)
        qq_download_find_1 = qq_download_find + 1
        # print(qq_name_find)
        qq_id_find = qq_str.find('{"SoftID":"',qq_id_find_1)
        qq_id_find_1 = qq_id_find + 1 
        # print(qq_name_find)
        qq_name = qq_str[qq_name_find:int(qq_str.find("]",qq_name_find))].strip("<![CDATA[")
        if qq_name == '':
            return qq_search_list
        qq_version = qq_str[qq_version_find:int(qq_str.find("&lt",qq_version_find))].strip("<versionname>")
        qq_download = qq_str[qq_download_find:int(qq_str.find("]",qq_download_find))].strip("![CDATA[")
        qq_id = qq_str[int(qq_id_find):int(qq_str.find(',',qq_id_find))].strip('{"SoftID":"')
        qq_download_url = qq_download.replace('\\',"")
        qq_search_all = [qq_name.encode('ascii').decode('unicode_escape'),qq_version,qq_id,qq_download_url,"qq"]
        qq_search_list.append(qq_search_all)
    return qq_search_list
    # print (qq_name,"\n","Version:",qq_version,"\n",qq_download_url,"\n")

def Scoop_search_lensi(name,buckets_list_install,search_limit,Scoop_install_place ):
    for ch in name:
        if '\u4e00' <= ch <= '\u9fff':
            p = Pinyin() 
            name = p.get_pinyin(name,'')
            break
    # print(name)
    search_list = process.extract(name,buckets_list_install, limit=search_limit)
    # print(search_list)
    app_name_all = []
    for i in range(0,search_limit):
        app_name = search_list[i][0][0][0][search_list[i][0][0][0].find('\\'):].strip("\\")
        app_name_install = search_list[i][0][0][0]
        app_json = []
        # print(app_name_install,app_name)
        app_name_json = Scoop_install_place + "\\Scoop\\buckets\\" + app_name_install[:app_name_install.find('\\')] + "\\bucket\\" + app_name + ".json"
        try:
            with open(app_name_json, 'r') as f:
                app_json = json.load(f)
            app_detail = [app_json["shortcuts"][0][1],app_json["version"],app_json["homepage"],app_name,"Scoop"]
            app_name_all.append(app_detail) 
            # TODO The missing 'n' and other ----BUG 放弃！！！ (╯▔皿▔)╯
        except:
            pass
    # app_name_1 = search_list[0][0][0][0][search_list[0][0][0][0].find('\\'):].strip("\\")
    # app_name_2 = search_list[1][0][0][0][search_list[1][0][0][0].find('\\'):].strip("\\")
    # app_name_3 = search_list[2][0][0][0][search_list[2][0][0][0].find('\\'):].strip("\\")
    # app_name_search1 = search_list[0][0][0][0]
    # app_name_search2 = search_list[1][0][0][0]
    # app_name_search3 = search_list[2][0][0][0]
    # app_name_all = [[app_name_1,app_name_search1],[app_name_2,app_name_search2],[app_name_3,app_name_search3]]
    if app_name_all == None:
        return app_name_all
    else:
        return app_name_all

def Scoop_buckets_save(Scoop_install_place):
    buckets_list_install = []
    os.chdir("D:\\Scoop\\buckets")
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
        writer.writerow(list_data)

def Scoop_buckets_load():
    buckets_list_install = []
    os.chdir("D:\\")
    with open("buckets_list_install.csv", "r", encoding='UTF-8') as file:
        data = csv.reader(file)
        for row in data:
            row_l = [row]
            buckets_list_install.append(row_l)
    return buckets_list_install

def choco_search(app_name,limmit_num):
    for ch in app_name:
        if '\u4e00' <= ch <= '\u9fff':
            p = Pinyin() 
            app_name = p.get_pinyin(app_name,'')
            break
    # print(app_name)
    try:
        search_result = subprocess.getoutput('choco search '+ app_name + ' --limitoutput --page=1 --page-size=' + str(limmit_num))
    except:
        search_result = subprocess.getoutput('choco search '+ app_name + ' --limitoutput')
    # print(search_result.replace("Directory 'C:\ProgramData\chocolatey\lib' does not exist.",""))
    search_list = []
    search_list_all = search_result.split()
    search_list_all_a = []
    for name in search_list_all:
        search_list.append(name.split("|"))
    if search_list[0] == ['Directory']:
        del(search_list[0:5])
    if search_list == []:
        search_list = None
        return search_list
    else:
        # print(search_list)
        for i in search_list:
            app_name_true = i[0]
            app_detail = subprocess.getoutput('choco info '+ app_name_true)
            app_detail_url = app_detail[int(app_detail.find('Software Site:')):int(app_detail.find("\n",app_detail.find("Software Site:")))].strip("Software Site:")
            # print(i[0],i[1],app_detail_url,app_name_true)
            search_list_all_a.append([i[0],i[1],app_detail_url.strip("\n"),app_name_true,"Choco"])
        # search_list_all_a.append("Choco")
        return search_list_all_a

def winget_search(app_name,limmit_num):
    search_result_list_all = []
    app_name = app_name.replace(" ","")
    # print(app_name)
    cmd = "winget search " + app_name + " -n " + str(limmit_num)
    f = open("search_result.txt","w", encoding='UTF-8')
    pipe = subprocess.Popen(cmd, shell=True, stdout=f)
    pipe.communicate()
    f.close()
    f = open("search_result.txt","r", encoding='UTF-8')
    search_result_txt = f.read()
    #print(search_result_txt)
    if search_result_txt.find("找不到与输入条件匹配的程序包。") != -1:
        return search_result_list_all
    search_result_list = f.readlines()[3:]
    if search_result_list[len(search_result_list)-1] == "<由于结果限制而截断了其他条目>":
        search_result_list = search_result_list[:len(search_result_list)-1]
    if search_result_list[len(search_result_list)-1] == "\n":
        search_result_list = search_result_list[:len(search_result_list)-1]
    if search_result_list[0].find("▒") != -1 or search_result_list[0].find("█") != -1:
        for i in range(0,len(search_result_list)):
            if search_result_list[i] == "--------------------------------------------" :
                cnt_cut = i
                break
        search_result_list = search_result_list[cnt_cut:]
    search_result = []
    for i in search_result_list:
        search_result.append(i.split())
    for j in search_result:
        name = "".join(j[:len(j)-3])
        del(j[:len(j)-3])
        j.insert(0,name)
        # print(name)
    f.close()
    # print (search_result)
    if search_result == []:
        search_result_list_all = None
        return search_result_list_all
    else:
        # print(search_result)
        if len(search_result) == 1:
            cmd = "winget show --id " + search_result[0][1]
            f = open("info_result.txt","w", encoding='UTF-8')
            pipe = subprocess.Popen(cmd, shell=True, stdout=f)
            pipe.communicate()
            f.close()
            f = open("info_result.txt","r", encoding='UTF-8')
            info_result = f.read()
            f.close()
            info_result_url = info_result[int(info_result.find('URL:')):int(info_result.find("\n",info_result.find("URL:")))].strip("URL:")
            # print(info_result_url)
            search_result_app = [search_result[0][0],search_result[0][2],info_result_url,search_result[0][1],"Winget"]
            # print(search_result_app)
            search_result_list_all.append(search_result_app)
            # search_result.append("Winget")
            return search_result_list_all
        else:
            # print(search_result)
            for i in range(0,len(search_result)-1):
                cmd = "winget show --id " + search_result[i][1]
                f = open("info_result.txt","w", encoding='UTF-8')
                pipe = subprocess.Popen(cmd, shell=True, stdout=f)
                pipe.communicate()
                f.close()
                f = open("info_result.txt","r", encoding='UTF-8')
                info_result = f.read()
                f.close()
                info_result_url = info_result[int(info_result.find('URL:')):int(info_result.find("\n",info_result.find("URL:")))].strip("URL:")
                # print(info_result_url)
                search_result_app = [search_result[i][0],search_result[i][2],info_result_url,search_result[i][1],"Winget"]
                # print(search_result_app)
                search_result_list_all.append(search_result_app)
            # search_result.append("Winget")
            return search_result_list_all

def lensi_search_all(source,app_name,limmit_num):
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
    

Scoop_buckets_save("D:")
# 创建新线程

app_name = input("input app name : ")
app_num = int(input("how many (不要有bug啊啊啊(╯▔皿▔)╯): "))
# app_name = "notepad"

thread_360 = myThread( "360", app_name,app_num)
thread_qq = myThread("qq", app_name,app_num)
thread_S = myThread( "Scoop", app_name,app_num)
thread_C = myThread( "Choco", app_name,app_num)
thread_W = myThread( "Winget", app_name,app_num)

result = []

# 开启新线程
thread_360.start()
thread_qq.start()
thread_S .start()
thread_C.start()
thread_W.start()
thread_360.join()
thread_qq.join()
thread_S.join()
thread_C.join()
thread_W.join()
# print ("退出主线程")
if thread_360.get_result() != None :
    result.extend(thread_360.get_result())
if thread_qq.get_result() != None :
    result.extend(thread_qq.get_result())  
if thread_S.get_result() != None :
    result.extend(thread_S.get_result())
if thread_C.get_result() != None :  
    result.extend(thread_C.get_result())
if thread_W.get_result() != None :  
    result.extend(thread_W.get_result())  

pprint.pprint(result)