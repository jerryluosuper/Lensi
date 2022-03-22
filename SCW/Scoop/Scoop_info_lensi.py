'''
Author: your name
Date: 2022-03-06 13:41:56
LastEditTime: 2022-03-09 19:53:38
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \Work\Lensi\Scoop\Scoop_search.py
'''
import json
import os


def Scoop_search_info(app_name_install):
    app_json = []
    app_name_json = "D:\\App\\Scoop\\buckets\\" + app_name_install[:app_name_install.find('\\')] + "\\bucket\\" + app_name_install[app_name_install.find('\\'):].strip("\\") + ".json"
    with open(app_name_json, 'r') as f:
        app_json = json.load(f)
    app_detail = [app_json["shortcuts"][0][1],app_json["version"],app_json["description"],app_json["homepage"]]
    # app_name_detail = app_json["shortcuts"][0][1]
    # app_version = app_json["version"]
    # app_description = app_json["description"]
    # app_homepage = app_json["homepage"]
    return app_detail
