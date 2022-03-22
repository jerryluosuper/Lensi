'''
Author: your name
Date: 2022-03-06 09:42:07
LastEditTime: 2022-03-06 10:20:08
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \Work\Lensi\other\getnumber.py
'''
import re
from urllib import request
from urllib.request import urlopen
from bs4 import BeautifulSoup

headers = {'User-Agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763'}

url = 'https://community.chocolatey.org/packages'
req = request.Request(url=url,headers=headers)
html = urlopen(req)
soup = BeautifulSoup(html.read(),"html.parser")
data = soup.select('#package > div > div.col-md-8.col-xl-9.col-xxl-8.py-3.py-xl-5.pe-xxl-5 > div.d-lg-flex.align-items-lg-center.justify-content-lg-between > div:nth-child(1) > h3')
for item in data:
    name = str(item.get_text())
number_list = re.findall(r"\d+\.?\d*",name)
number = number_list[0]
print(number)
