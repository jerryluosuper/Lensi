'''
Author: your name
Date: 2022-03-16 13:05:46
LastEditTime: 2022-03-21 10:46:43
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \Lensi\bug_test.py
'''
# for i in range(0,0):
#     print(i)
# import os
# from fuzzywuzzy import fuzz

# # os.system("asdfaffdfa")

# # os.chdir("D:\\")#想不到其他地方了
# # f = open("search_result.txt","r", encoding='UTF-8')
# # search_result_list = f.readlines()#去除前三行干扰 有bug
# # search_result_txt = f.read()#等等，这个有啥用
# # # print(search_result_txt)
# # print(search_result_txt)
# # print(search_result_list)
# # f.close()
# print(fuzz.ratio("geek", "Geek Uninstaller"))

# import os
# from pickle import TRUE
# import subprocess

# cmd = "winget search blender -n 2"
# pipe = subprocess.Popen(cmd, shell=True,stdout=subprocess.PIPE)#subprocess 将输出保存到search_result.txt中
# f = pipe.stdout.readlines()
# pipe.communicate()#
# pipe = subprocess.Popen(cmd, shell=True,stdout=subprocess.PIPE)#subprocess 将输出保存到search_result.txt中
# s = pipe.stdout.read().decode("utf-8")
# pipe.communicate()#等待？
# # f.close()#关闭文件 后面立刻又开了又必要吗？
# # os.chdir("D:")#想不到其他地方了
# # f = open("search_result.txt","r", encoding='UTF-8')
# print(f,s)

test = ['Blender for Windows', '2.93.5', "Blender is an integrated application that enables the creation of a broad range of 2D and 3D content. Blender provides a broad spectrum of modeling, texturing, lighting, animation and video post-processing functionality in one package. Through it's open architecture, Blender provides cross-platform interoperability, extensibility, an incredibly small footprint, and a tightly integrated workflow. Blender is one of the most popular Open Source 3D graphics application in the world.", 'https://filehippo.com/download_blender/', 'https://dl5.filehippo.com/ede/450/3943412b18ef32ae9ee80d5b3f025cdb5c/blender-2.93.5-windows-x64.msi?Expires=1647867282&Signature=3c1c723630bf1f49be15460e0b23e063aa50dc19&url=https://filehippo.com/download_blender/&Filename=blender-2.93.5-windows-x64.msi', 'https://sc.filehippo.net/images/t_app-logo-l,f_auto,dpr_auto/p/dfc9dea4-96d1-11e6-97bc-00163ed833e7/3780019931/blender-logo', 86, 'hippo']
print(test[6])