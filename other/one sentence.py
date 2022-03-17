'''
Author: Lensit
Date: 2021-08-13 20:31:37
LastEditTime: 2022-03-12 11:09:24
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \RSS\一句.py
'''
from urllib import request
from urllib.request import urlopen 
headers = {'User-Agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763'}
url = 'https://yijuzhan.com/api/word.php'
req = request.Request(url=url,headers=headers)
html = urlopen(req)
html_text = bytes.decode(html.read())
print(html_text)