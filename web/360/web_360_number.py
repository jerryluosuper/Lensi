'''
Author: your name
Date: 2022-03-06 10:29:21
LastEditTime: 2022-03-06 11:10:33
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \Work\Lensi\web\web_360_number.py
'''
import re
from urllib import request
from urllib.request import urlopen
from bs4 import BeautifulSoup

headers = {'User-Agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763'}

url = 'https://baoku.360.cn/soft/list?cid=0&order=1&page=1'
req = request.Request(url=url,headers=headers)
html = urlopen(req)
soup = BeautifulSoup(html.read(),"html.parser")
data = soup.select('body > div.container > div.midArea > div.main > ul > li:nth-child(1)')
print(soup)
# TODO:unable to get o(╥﹏╥)o