'''
Author: your name
Date: 2022-02-14 10:27:42
LastEditTime: 2022-03-14 13:01:29
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
qq_search_url = 'https://s.pcmgr.qq.com/tapi/web/searchcgi.php?type=search&callback=searchCallback&keyword='+ app_name +'&page=1&pernum=1&more=0'
qq_html_req = request.Request(url=qq_search_url,headers=headers)
qq_html = urlopen(qq_html_req)
qq_soup = BeautifulSoup(qq_html.read(),"html.parser")
qq_str = str(qq_soup)

'''
TODO 未使用正则表达式 待优化
'''
print(qq_str)
qq_name = qq_str[int(qq_str.find('<![CDATA[')):int(qq_str.find("]",qq_str.find("<![CDATA[")))].strip("<![CDATA[")
qq_version = qq_str[int(qq_str.find('<versionname>')):int(qq_str.find("&lt",qq_str.find("<versionname>")))].strip("<versionname>")
qq_download = qq_str[int(qq_str.find('[CDATA[http:')):int(qq_str.find("]",qq_str.find("[CDATA[http:")))].strip("![CDATA[")
qq_id = qq_str[int(qq_str.find('{"SoftID":"')):int(qq_str.find(',',qq_str.find('{"SoftID":"')))].strip('{"SoftID":"')
qq_id_int = int(qq_id)
print(qq_id)

qq_info_url = 'https://pc.qq.com/detail/'+ qq_id_int%20 + '/detail_' + qq_id + '.html' 
qq_info_html_req = request.Request(url=qq_info_url,headers=headers)
qq_info_html = urlopen(qq_html_req)
qq_info_soup = BeautifulSoup(qq_html.read(),"html.parser")
qq_info_data = qq_info_soup.select('body > div.category-wrap > div.container_16 > div > div > div.detail-wrap > div.detail-desc > div.cont-content > p:nth-child(1)')
for item in qq_info_data:
    qq_info = item.get_text()
print(qq_info)

qq_download_url = qq_download.replace('\\',"")
print (qq_name,"\n","Version:",qq_version,"\n",qq_download_url,"\n")
choice_continue = input("Do you want to continue?:Y/N      ")
if choice_continue == "Y" or choice_continue == "y":
    qq_download_name = qq_download_url[qq_download_url.rfind("/"):].strip("/")
    print("Downloading to",qq_download_name)
    urlretrieve(qq_download_url,qq_download_name)
    print("下载完成,即将打开")
    os.system(qq_download_name)
