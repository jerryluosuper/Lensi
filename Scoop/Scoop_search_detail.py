'''
Author: your name
Date: 2022-03-15 13:08:14
LastEditTime: 2022-03-15 13:08:15
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \Lensi\Scoop\Scoop_search_detail.py
'''
from fuzzywuzzy import process
from xpinyin import Pinyin
import json

def Scoop_search_lensi(name,buckets_list_install,search_limit,Scoop_install_place ):
    for ch in name:
        if '\u4e00' <= ch <= '\u9fff':
            p = Pinyin() 
            name = p.get_pinyin(name,'')
            break
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
            app_detail = [app_json["shortcuts"][0][1],app_json["version"],app_json["homepage"],app_name]
            app_name_all.append(app_detail) 
            # TODO The missing 'n' ----BUG
        except:
            app_name_all.append("error")
    # app_name_1 = search_list[0][0][0][0][search_list[0][0][0][0].find('\\'):].strip("\\")
    # app_name_2 = search_list[1][0][0][0][search_list[1][0][0][0].find('\\'):].strip("\\")
    # app_name_3 = search_list[2][0][0][0][search_list[2][0][0][0].find('\\'):].strip("\\")
    # app_name_search1 = search_list[0][0][0][0]
    # app_name_search2 = search_list[1][0][0][0]
    # app_name_search3 = search_list[2][0][0][0]
    # app_name_all = [[app_name_1,app_name_search1],[app_name_2,app_name_search2],[app_name_3,app_name_search3]]
    app_name_all.append("S")
    return app_name_all
