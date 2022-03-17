'''
Author: your name
Date: 2022-02-14 10:27:42
LastEditTime: 2022-02-21 22:51:55
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \Work\Lensi\web.py
'''
import os
from urllib import request
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlretrieve

headers = {'User-Agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763'}

app_name = input("软件名称：")
filehippo_search_url = 'https://filehippo.com/search/?q=' + app_name
hippo_html_req = request.Request(url=filehippo_search_url,headers=headers)
hippo_html = urlopen(hippo_html_req)
hippo_search_soup = BeautifulSoup(hippo_html.read(),"html.parser")
hippo_search_data = hippo_search_soup.select('body > div.page > div.page__row > div > div > div.main > section > ul > li:nth-child(2) > a')
for item in hippo_search_data:
    hippo_search_name = item.get_text()
    hippo_search_result = item.get('href')
print(hippo_search_name,hippo_search_result)
choice_continue = input("Do you want to continue?:Y/N      ")
if choice_continue == "Y" or choice_continue == "y":
    hippo_search_result = hippo_search_result + "post_download/"
    hippo_download_html_req = request.Request(url=hippo_search_result,headers=headers)
    hippo_download_html = urlopen(hippo_download_html_req)
    hippo_download_soup = BeautifulSoup(hippo_download_html.read(),"html.parser")
    hippo_download_data = hippo_download_soup.select('body > div.page > script:nth-child(2)')
    for item in hippo_download_data:
        hippo_download_url = item.get('data-qa-download-url')
    print (hippo_download_url)
    choice_download = input("Still want to continue?:Y/N      ")
    if choice_download == "Y" or choice_download == "y":
        hippo_download_name = hippo_download_url[hippo_download_url.rfind("="):]
        hippo_download_name = hippo_download_name.strip("=")
        print("Downloading to",hippo_download_name)
        urlretrieve(hippo_download_url,hippo_download_name)
        # aira2_download = "aira2" + hippo_download_url
        os.system(hippo_download_name)
        print("下载完成")