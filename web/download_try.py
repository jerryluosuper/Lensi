'''
Author: your name
Date: 2022-02-14 11:41:47
LastEditTime: 2022-02-14 12:10:52
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \Work\Lensi\download_try.py
'''
from urllib.request import urlretrieve

url = "https://dl5.filehippo.com/970/a88/349cf04cf44eeb26171a12b3c423b95ce3/geek.zip?Expires=1644851477&Signature=688ecc6881adcafce3b34e2b86b5df2cab0d7bb4&url=https://filehippo.com/download_geek-uninstaller/&Filename=geek.zip"
url_name = "app" + url[url.rfind("."):]
urlretrieve(url,url_name)

