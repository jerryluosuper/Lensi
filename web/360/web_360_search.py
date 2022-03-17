'''
Author: your name
Date: 2022-02-14 10:27:42
LastEditTime: 2022-03-14 15:39:02
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \Work\Lensi\web.py
'''
import os
from urllib import request
from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup
def web_360_search(app_name):
    headers = {'User-Agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763'}

    # app_name = "geek"
    baoku_search_url = 'https://bapi.safe.360.cn/soft/search?keyword='+ app_name + '&page=1'
    baoku_html_req = request.Request(url=baoku_search_url,headers=headers)
    baoku_html = urlopen(baoku_html_req)
    baoku_soup = BeautifulSoup(baoku_html.read(),"html.parser")
    baoku_str = str(baoku_soup)

    '''
    TODO 未使用正则表达式 待优化
    '''
    print(baoku_str)
    baoku_name = baoku_str[int(baoku_str.find('"softname":"')):int(baoku_str.find(',',baoku_str.find('"softname":"')))].strip('"softname":"')
    baoku_version = baoku_str[int(baoku_str.find('"version":"')):int(baoku_str.find(',',baoku_str.find('"version":"')))].strip('"version":"')
    baoku_download = baoku_str[int(baoku_str.find('"soft_download":"')):int(baoku_str.find(',',baoku_str.find('"soft_download":"')))].strip('"soft_download":"')
    baoku_id = baoku_str[int(baoku_str.find('[{"softid":')):int(baoku_str.find(',',baoku_str.find('[{"softid":')))].strip('[{"softid":')
    baoku_download_url = baoku_download.replace('\\',"")
    baoku_search_all = [baoku_name.strip(","),baoku_id,baoku_version.strip(","),baoku_download_url.strip(",")]
    return baoku_search_all
print(web_360_search("geek"))
