'''
Author: your name
Date: 2022-03-19 11:21:04
LastEditTime: 2022-03-19 11:58:16
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \Lensi\winget\winget_search_new.py
'''
import os
import subprocess
def winget_search(app_name,limmit_num):#winget 搜索解析
    '''
    大致输出格式：
    -\|/ 
    名称          ID           版本    源
    -------------------------------------------
    xx xx xx xx
    <由于结果限制而截断了其他条目>
    '''
    search_result_list_all = []
    app_name = app_name.replace(" ","") #winget search 软件名中不能有空格
    # print(app_name)
    cmd = "winget search " + app_name + " -n " + str(limmit_num)
    # 一个非常非常非常又烂又低效的方法——存储到文件再读取
    # TODO 优化！！！
    os.chdir("D:")#想不到其他地方了
    pipe = subprocess.Popen(cmd, shell=True,stdout=subprocess.PIPE)#subprocess 将输出保存到search_result.txt中
    search_result_list_un = pipe.stdout.readlines()[2:]#去除前三行干扰 有bug
    search_result_list = []
    pipe.communicate()
    for i in search_result_list_un:
        search_result_list.append(i.decode("utf-8"))
    # print(search_result_list)
    pipe = subprocess.Popen(cmd, shell=True,stdout=subprocess.PIPE)#subprocess 将输出保存到search_result.txt中
    search_result_txt = pipe.stdout.read().decode("utf-8")
    pipe.communicate()#等待
    # print(search_result_txt)
    if search_result_txt.find("找不到与输入条件匹配的程序包。") != -1:
        return search_result_list_all #异常处理——找不到或根本不存在？
    if  search_result_txt.find("<由于结果限制而截断了其他条目>") != -1:
        search_result_list = search_result_list[:len(search_result_list)-1] # 去除末行干扰
    cnt_cut = 0
    for i in range(0,len(search_result_list)):
        if search_result_list[i] == "--------------------------------------------" : #为啥我觉得只要这一句就好了
            cnt_cut = i
            break
    search_result_list = search_result_list[cnt_cut:] #顺带解决开机第一次100%加载的bug
    search_result = [] #这又在干嘛？ 以空行分隔后的软件列表
    # print(search_result_list)
    for i in search_result_list:
        search_result.append(i.split())#以空行分隔
    for j in search_result:
        name = "".join(j[:len(j)-3]) #因为id version source 是连续的 不带空格的，所以确定这三个把前面的连起来
        del(j[:len(j)-3])
        j.insert(0,name)
        # print(name)
    # print (search_result)
    if search_result == []:#判断是否为空，防止报错
        search_result_list_all = None
        return search_result_list_all
    else:
        # print(search_result)
        if len(search_result) == 1: #防止range（0，0）的错误
            cmd = "winget show --id " + search_result[0][1]
            #换汤不换药
            f = open("info_result.txt","w", encoding='UTF-8')
            pipe = subprocess.Popen(cmd, shell=True, stdout=f)
            pipe.communicate()
            f.close()
            f = open("info_result.txt","r", encoding='UTF-8')
            info_result = f.read()
            f.close()
            info_result_url = info_result[int(info_result.find('URL:')):int(info_result.find("\n",info_result.find("URL:")))].strip("URL:")
            info_detail = info_result[int(info_result.find('描述: ')):int(info_result.find("\n",info_result.find("描述: ")))].strip("描述: ")
            #解析官网url
            # print(info_result_url)
            search_result_app = [search_result[0][0],search_result[0][2],info_detail,info_result_url,search_result[0][1],"Winget"]
            #统一格式
            # print(search_result_app)
            search_result_list_all.append(search_result_app)
            # search_result.append("Winget")
            return search_result_list_all
        else:
            # print(search_result)
            for i in range(0,len(search_result)-1):#除len = 1的情况 其余同上
                        # print(search_result)
                if len(search_result) == 1: #防止range（0，0）的错误
                    cmd = "winget show --id " + search_result[0][1]
                    #换汤不换药
                    pipe = subprocess.Popen(cmd, shell=True,stdout=subprocess.PIPE)#subprocess 将输出保存到search_result.txt中
                    info_result = pipe.stdout.read().decode("utf-8")
                    pipe.communicate()#等待？
                    info_result_url = info_result[int(info_result.find('URL:')):int(info_result.find("\n",info_result.find("URL:")))].strip("URL:")
                    info_detail = info_result[int(info_result.find('描述: ')):int(info_result.find("\n",info_result.find("描述: ")))].strip("描述: ")
                    #解析官网url
                    # print(info_result_url)
                    search_result_app = [search_result[0][0],search_result[0][2],info_detail,info_result_url,search_result[0][1],"Winget"]
                    #统一格式
                    # print(search_result_app)
                    search_result_list_all.append(search_result_app)
                    # search_result.append("Winget")
            # search_result.append("Winget")
    return search_result_list_all
print(winget_search("blender",1))