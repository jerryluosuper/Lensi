'''
Author: your name
Date: 2022-02-14 10:27:42
LastEditTime: 2022-02-21 22:49:47
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

hippo_download_html_url = "https://filehippo.com/download_" + app_name + "/post_download/"

hippo_information_html_url = "https://filehippo.com/download_" + app_name + "/"

try:
    hippo_information_html_req = request.Request(url=hippo_information_html_url,headers=headers)
    hippo_information_html = urlopen(hippo_information_html_req)
except:
    print ("Warning: Can't find any information of",app_name)
else:
    print("From",hippo_download_html_url,"\n","And also from",hippo_information_html_url,"\n")
    hippo_information_soup = BeautifulSoup(hippo_information_html.read(),"html.parser")
    hippo_information_data = hippo_information_soup.select('body > div.page > div:nth-child(2) > div > div > div > section.mb-l > article')
    hippo_information_data_name = hippo_information_soup.select('body > div.page > div:nth-child(2) > div > div > div > section.program-header-content > div.program-header-content__main > div > div.media__body > h1')
    for item in hippo_information_data_name:
        hippo_information_name = item.get_text()
    print (hippo_information_name,"\n")
    for item1 in hippo_information_data:
        hippo_information = item1.get_text()
    print (hippo_information)
    choice_continue = input("Do you want to continue?:Y/N      ")
    if choice_continue == "Y" or choice_continue == "y":
        try:
            hippo_download_html_req = request.Request(url=hippo_download_html_url,headers=headers)
            hippo_download_html = urlopen(hippo_download_html_req)
            hippo_download_soup = BeautifulSoup(hippo_download_html.read(),"html.parser")
            hippo_download_data = hippo_download_soup.select('body > div.page > script:nth-child(2)')
            for item2 in hippo_download_data:
                    hippo_download_url = item2.get('data-qa-download-url')
            print (hippo_download_url)
        except NameError:
            print ("Warning: Can't find any downloading information of",app_name)
        else:
            choice_download = input("Still want to continue?:Y/N      ")
            if choice_download == "Y" or choice_download == "y":
                hippo_download_name = hippo_download_url[hippo_download_url.rfind("="):]
                hippo_download_name = hippo_download_name.strip("=")
                print("Downloading to",hippo_download_name)
                urlretrieve(hippo_download_url,hippo_download_name)
                # aira2_download = "aira2" + hippo_download_url
                print("下载完成,即将打开")
                os.system(hippo_download_name)