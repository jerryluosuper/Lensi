'''
Author: your name
Date: 2022-02-14 10:27:42
LastEditTime: 2022-03-13 13:50:51
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \Work\Lensi\web.py
'''
import os
from urllib import request
from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup

headers = {'User-Agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763'}

app_name = input("软件名称：")
# app_name = "geek"
baoku_search_url = 'https://bapi.safe.360.cn/soft/search?keyword='+ app_name + '&page=1'
baoku_html_req = request.Request(url=baoku_search_url,headers=headers)
baoku_html = urlopen(baoku_html_req)
baoku_soup = BeautifulSoup(baoku_html.read(),"html.parser")
baoku_str = str(baoku_soup)

'''
TODO 未使用正则表达式 待优化
'''
# print(baoku_str)
baoku_name = baoku_str[int(baoku_str.find('"softname":"')):int(baoku_str.find(',',baoku_str.find('"softname":"')))].strip('"softname":"')
baoku_version = baoku_str[int(baoku_str.find('"version":"')):int(baoku_str.find(',',baoku_str.find('"version":"')))].strip('"version":"')
baoku_download = baoku_str[int(baoku_str.find('"soft_download":"')):int(baoku_str.find(',',baoku_str.find('"soft_download":"')))].strip('"soft_download":"')

baoku_download_url = baoku_download.replace('\\',"")
print (baoku_name.strip(","),"\n","Versions:",baoku_version.strip(","),"\n",baoku_download_url.strip(","),"\n")
choice_continue = input("Do you want to continue?:Y/N      ")
if choice_continue == "Y" or choice_continue == "y":
    baoku_download_name = baoku_download_url[baoku_download_url.rfind("/"):].strip("/")
    print("Downloading to",baoku_download_name)
    urlretrieve(baoku_download_url,baoku_download_name)
    print("下载完成,即将打开")
    os.system(baoku_download_name)
