'''
Author: your name
Date: 2022-03-13 12:53:52
LastEditTime: 2022-03-14 11:39:58
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \Lensi\Scoop\Scoop_update.py
'''
import os


def choco_update_app(app_name):
    os.system("choco upgrade " + app_name)
choco_update_app("")
