'''
Author: your name
Date: 2022-03-20 13:18:44
LastEditTime: 2022-03-20 13:18:45
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \Lensi\choco\choco_install_app.py
'''
import os
def choco_update_all(app_name):
    os.system("choco install"+app_name)