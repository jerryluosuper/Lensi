'''
Author: your name
Date: 2022-03-21 11:39:01
LastEditTime: 2022-03-24 08:56:15
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \Lensi\Lensi_all.py
'''
import os
from urllib import request
from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup
import threading
from urllib.parse import quote 
from fuzzywuzzy import fuzz

def web_qq_info(qq_id):
    headers = {'User-Agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763'}
    qq_id_int = int(qq_id)
    # print(qq_id)
    qq_info_url = 'https://pc.qq.com/detail/'+ str(qq_id_int%20) + '/detail_' + qq_id + '.html' 
    # print(qq_info_url)
    qq_info_html_req = request.Request(url=qq_info_url,headers=headers)
    qq_info_html = urlopen(qq_info_html_req)
    qq_info_soup = BeautifulSoup(qq_info_html.read(),"html.parser")
    try:
        qq_info_data = qq_info_soup.select('body > div.category-wrap > div.container_16 > div > div > div.detail-wrap > div.detail-desc > div.cont-content > p:nth-child(1)')
        for item in qq_info_data:
            qq_info_main = item.get_text()
        qq_info_data_home = qq_info_soup.select('body > div.category-wrap > div.container_16 > div > div > div.detail-wrap > div.detail-desc > div.cont-content > p:nth-child(3) > a')
        for item in qq_info_data_home:
            qq_info_home = item.get('href')
        qq_info = [qq_info_home,qq_info_main,qq_info_url]
        return qq_info
    except:
        qq_info_data = qq_info_soup.select('body > div.category-wrap > div.container_16 > div > div.part1')
        for item in qq_info_data:
            qq_info_image = item.get('style')
        qq_info_image_url = qq_info_image[int(qq_info_image.find('url(')):int(qq_info_image.find(')',qq_info_image.find('{url(')))].strip('url(')
        qq_info_image_url = qq_info_image_url.rstrip(")!important")
        if qq_info_image_url[0] == "/":
            qq_info_image_url = "https:" + qq_info_image_url
        # print(qq_info_image_url)
        urlretrieve(url=qq_info_image_url,filename="qq_info.png")
        return qq_info_image_url
    # print(qq_info_main,"\n",qq_info_home)

def web_baoku_info(baoku_id):
    headers = {'User-Agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763'}
    # print(baoku_id)
    baoku_info_url = 'https://baoku.360.cn/soft/show/appid/' + baoku_id
    print(baoku_info_url)
    baoku_info_html_req = request.Request(url=baoku_info_url,headers=headers)
    baoku_info_html = urlopen(baoku_info_html_req)
    baoku_info_soup = BeautifulSoup(baoku_info_html.read(),"html.parser")
    baoku_info_data = baoku_info_soup.select('body > div.app-container > div:nth-child(2) > div.dashboard-container.pic-container > div > img')
    for item in baoku_info_data:
        baoku_info_image_url = item.get('src')
    baoku_info_image_url = "https:" +baoku_info_image_url
    # print(baoku_info_image_url)
    urlretrieve(url=baoku_info_image_url,filename="baoku_info.png")
    baoku_icon_data = baoku_info_soup.select('body > div.app-container > div:nth-child(2) > div:nth-child(2) > h1 > img')
    for item in baoku_icon_data:
        baoku_icon_image_url = item.get('src')
    baoku_icon_image_url = "https:" +baoku_icon_image_url
    print(baoku_icon_image_url)
    urlretrieve(url=baoku_icon_image_url,filename="baoku_icon.png")
    baoku_info_url = 'https://baoku.360.cn/soft/show/appid/' + baoku_id + 'd'
    # print(baoku_info_url)
    baoku_info_html_req = request.Request(url=baoku_info_url,headers=headers)
    baoku_info_html = urlopen(baoku_info_html_req)
    baoku_info_soup = BeautifulSoup(baoku_info_html.read(),"html.parser")
    baoku_detail = baoku_info_soup.select('body > div.wrap.clearfix > div.main-list.fr > div.app-info > div.app-introduce > div.introduce-txt1 > p')
    for item in baoku_detail:
        baoku_detail_text = item.get_text
    # print(baoku_detail_text)
    baoku_info = [baoku_detail_text,baoku_info_image_url]
    return baoku_info
    # print(baoku_info_main,"\n",baoku_info_home)

def web_hippo_info(app_name):
    headers = {'User-Agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763'}
    hippo_information_html_url = "https://filehippo.com/download_" + app_name + "/"
    hippo_information_html_req = request.Request(url=hippo_information_html_url,headers=headers)
    hippo_information_html = urlopen(hippo_information_html_req)
    hippo_information_soup = BeautifulSoup(hippo_information_html.read(),"html.parser")
    hippo_information_data = hippo_information_soup.select('body > div.page > div:nth-child(2) > div > div > div > section.mb-l > article')
    for item1 in hippo_information_data:
        hippo_information = item1.get_text()
    return hippo_information

def Lensi_info(app_name,app_source):
    if app_source == "qq":
        web_qq_info(app_name)
    elif app_source == "360":
        web_baoku_info(app_name)
    elif app_source == "Hippo":
        web_hippo_info(app_name)

def web_install_normal(web_download_url):
    web_download_name = web_download_url[web_download_url.rfind("/"):]
    web_download_name = web_download_name.strip("/")
    print("Downloading to",web_download_name)
    urlretrieve(web_download_url,web_download_name)
    os.system(web_download_name)
    print("下载完成")

def web_install_hippo(web_download_url):
    web_download_name = web_download_url[web_download_url.rfind("="):]
    web_download_name = web_download_name.strip("=")
    print("Downloading to",web_download_name)
    urlretrieve(web_download_url,web_download_name)
    os.system(web_download_name)
    print("下载完成")

def Lensi_install(app_name,app_source):
    if app_source == "qq" or app_source == "360":
        web_install_normal(app_name)
    elif app_source == "hippo":
        web_install_hippo(app_name)

def get_yiju():
    headers = {'User-Agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763'}
    url = 'https://yijuzhan.com/api/word.php'
    req = request.Request(url=url,headers=headers)
    html = urlopen(req)
    html_text = bytes.decode(html.read())
    return html_text

class myThread (threading.Thread):
    def __init__(self, source, app_name,limit_num=3):
        threading.Thread.__init__(self)
        self.source = source
        self.app_name = app_name
        self.limit_num = limit_num
    def run(self):
        # print ("开始线程：" + self.app_name)
        self.result = lensi_search_all(self.source,self.app_name,self.limit_num) #多线程大函数
        # print ("退出线程：" + self.app_name)
    def get_result(self):  #获取return结果
        try:  
            return self.result  
        except Exception:  
            return None  

def web_360_search(app_name,limmit_num):
    headers = {'User-Agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763'}
    # 伪装标头
    app_name_search = quote(app_name)#输入转换成相应格式
    # app_name = "geek"
    baoku_search_url = 'https://bapi.safe.360.cn/soft/search?keyword='+ app_name_search + '&page=1'
    baoku_html_req = request.Request(url=baoku_search_url,headers=headers)
    baoku_html = urlopen(baoku_html_req)#使用标头获取html
    baoku_soup = BeautifulSoup(baoku_html.read(),"html.parser")
    baoku_str = str(baoku_soup)#字符串化 便于查找
    # print(baoku_str)
    '''
    TODO 未使用正则表达式 待优化
    '''
    baoku_name_search_1 = 0
    baoku_version_search_1 = 0
    baoku_download_search_1 =0 
    baoku_id_search_1 = 0 
    baoku_detail_search_1 = 0
    baoku_icon_search_1 = 0
    # 定义上一次查找结果
    baoku_search_all_list = []
    limmit_num_search = baoku_str.count('{"softid":')
    limmit_num_real = min(limmit_num,limmit_num_search)
    #防止找不到更多程序
    for i in range(0,limmit_num_real):
        baoku_name_search = baoku_str.find('"softname":"',baoku_name_search_1)
        baoku_name_search_1 = baoku_name_search + 1
        baoku_name = baoku_str[baoku_name_search:int(baoku_str.find(',',baoku_name_search))].strip('"softname":"')
        if baoku_name == '':
            return baoku_search_all_list #判断是否还有软件
        baoku_version_search = baoku_str.find('"version":"',baoku_version_search_1)
        baoku_version_search_1 = baoku_version_search + 1
        baoku_download_search = baoku_str.find('"soft_download":"',baoku_download_search_1)
        baoku_download_search_1 = baoku_download_search + 1
        baoku_id_search = baoku_str.find('[{"softid":',baoku_id_search_1)
        baoku_detail_search = baoku_str.find('"desc":"',baoku_detail_search_1)
        baoku_detail_search_1 = baoku_detail_search + 1
        baoku_id_search_1 = baoku_id_search + 1
        baoku_icon_search = baoku_str.find('"logo":"',baoku_icon_search_1)
        baoku_icon_search_1 = baoku_icon_search + 1
        #从上一次查找结果后开始查找，实现识别多个软件
        baoku_version= baoku_str[baoku_version_search:int(baoku_str.find(',',baoku_version_search))].strip('"version":"')
        baoku_download = baoku_str[baoku_download_search:int(baoku_str.find(',',baoku_download_search))].strip('"soft_download":"')
        baoku_id = baoku_str[baoku_id_search :int(baoku_str.find(',',baoku_id_search ))].strip('[{"softid":')
        baoku_detail_text = baoku_str[baoku_detail_search :int(baoku_str.find(',',baoku_detail_search ))].strip('"desc":"')
        baoku_icon = baoku_str[baoku_icon_search :int(baoku_str.find(',',baoku_icon_search ))].strip('"logo":"')
        #截获字符串
        baoku_download_url = baoku_download.replace('\\',"")
        baoku_icon_url = "https:" + baoku_icon.replace('\\',"") + "g"
        baoku_info_url = 'https://baoku.360.cn/soft/show/appid/' + baoku_id + 'd'
        #网址处理
        baoku_search_all = [baoku_name.strip(",").encode('ascii').decode('unicode_escape'),baoku_version.strip(","),baoku_detail_text.strip(",").encode('ascii').decode('unicode_escape'),baoku_info_url,baoku_download_url.strip(","),baoku_icon_url,fuzz.partial_ratio(app_name,baoku_name.strip(",").encode('ascii').decode('unicode_escape')),"360"]
        #整理格式
        baoku_search_all_list.append(baoku_search_all)
    return baoku_search_all_list

def web_qq_search(app_name,limmit_num):
    headers = {'User-Agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763'}
    # app_name = "geek"
    # app_name = app_name.encode('unicode_escape').decode('utf-8')
    # app_name_search = app_name.replace("\\","%")
    app_name_search = quote(app_name)
    # print(app_name_search)
    qq_search_url = 'https://s.pcmgr.qq.com/tapi/web/searchcgi.php?type=search&callback=searchCallback&keyword='+ app_name_search +'&page=1&pernum=' +str(limmit_num)+'&more=0'
    qq_html_req = request.Request(url=qq_search_url,headers=headers)
    qq_html = urlopen(qq_html_req)
    qq_soup = BeautifulSoup(qq_html.read(),"html.parser")
    qq_str = str(qq_soup)
    '''
    TODO 未使用正则表达式 待优化
    '''
    qq_search_all=[]
    qq_search_list=[]
    # print(qq_str)
    qq_name_find_1 = 0
    qq_version_find_1 = 0
    qq_download_find_1 = 0
    qq_id_find_1 = 0
    qq_detail_find_1 = 0  
    qq_icon_find_1 = 0
    limmit_num_real = min(limmit_num,qq_str.count('<versionname>'))
    #防止找不到更多程序
    for i in range(0,limmit_num_real):
        if i == 0:
            qq_name_find = qq_str.find('<![CDATA[',qq_name_find_1)
            qq_name_find_1 = qq_name_find + 1
        else:
            for j in range(0,7):
                qq_name_find = qq_str.find('<![CDATA[',qq_name_find_1)
                qq_name_find_1 = qq_name_find + 1
            # print(qq_name_find)
            #有7个“<![CDATA[”！！！ 之后才能找到正确软件名称
        qq_version_find = int(qq_str.find('<versionname>',qq_version_find_1))
        qq_version_find_1 = qq_version_find + 1
        # print(qq_name_find)
        qq_download_find = qq_str.find('[CDATA[http:',qq_download_find_1)
        qq_download_find_1 = qq_download_find + 1
        # print(qq_name_find)
        qq_id_find = qq_str.find('{"SoftID":"',qq_id_find_1)
        qq_id_find_1 = qq_id_find + 1 
        qq_detail_find = qq_str.find(r'<feature>\n                <![CDATA[',qq_detail_find_1) + 20
        qq_detail_find_1 = qq_detail_find + 1 
        qq_icon_find = qq_str.find('<logo48>',qq_icon_find_1) 
        qq_icon_find_1 = qq_icon_find + 1 
        # print(qq_name_find)
        #从上一次查找结果后开始查找，实现识别多个软件
        qq_name = qq_str[qq_name_find:int(qq_str.find("]",qq_name_find))].strip("<![CDATA[")
        if qq_name == '':
            return qq_search_list #判断是否还有软件
        qq_version = qq_str[qq_version_find:int(qq_str.find("&lt",qq_version_find))].strip("<versionname>")
        qq_download = qq_str[qq_download_find:int(qq_str.find("]",qq_download_find))].strip("![CDATA[")
        qq_id = qq_str[int(qq_id_find):int(qq_str.find(',',qq_id_find))].strip('{"SoftID":"')
        qq_detail = qq_str[qq_detail_find:int(qq_str.find(']',qq_detail_find))].strip(r"<feature>\n                <![CDATA[")
        qq_icon = qq_str[qq_icon_find:int(qq_str.find('&lt',qq_icon_find))].strip(' <logo48>')
        qq_icon_url = "https://pc3.gtimg.com/softmgr/logo/48/" + qq_icon + "g"
        qq_id_int = int(qq_id)
    # print(qq_id)
        qq_info_url = 'https://pc.qq.com/detail/'+ str(qq_id_int%20) + '/detail_' + qq_id + '.html' 
        # print(qq_detail)
        #截获字符串
        qq_download_url = qq_download.replace('\\',"")
        #网址处理
        qq_search_all = [qq_name.encode('ascii').decode('unicode_escape'),qq_version,qq_detail.encode('ascii').decode('unicode_escape'),qq_info_url,qq_download_url,qq_icon_url,fuzz.partial_ratio(app_name,qq_name.encode('ascii').decode('unicode_escape')),"qq"]
        #整理格式
        qq_search_list.append(qq_search_all)
    return qq_search_list
    # print (qq_name,"\n","Version:",qq_version,"\n",qq_download_url,"\n")

def hippo_search_easy(app_name):
    headers = {'User-Agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763'}
    hippo_download_html_url = "https://filehippo.com/download_" + app_name + "/post_download/"
    hippo_information_html_url = "https://filehippo.com/download_" + app_name + "/"
    hippo_search_result = []
    try:
        hippo_information_html_req = request.Request(url=hippo_information_html_url,headers=headers)
        hippo_information_html = urlopen(hippo_information_html_req)
    except:
        # print("!")
        return None
    else:
        # print("From",hippo_download_html_url,"\n","And also from",hippo_information_html_url,"\n")
        hippo_information_soup = BeautifulSoup(hippo_information_html.read(),"html.parser")
        hippo_information_data = hippo_information_soup.select('body > div.page > div:nth-child(2) > div > div > div > section.mb-l > article > p:nth-child(3)')
        hippo_information_data_name = hippo_information_soup.select('body > div.page > div:nth-child(2) > div > div > div > section.program-header-content > div.program-header-content__main > div > div.media__body > h1')
        hippo_icon_url_detail = hippo_information_soup.select('body > div.page > div:nth-child(2) > div > div > div > section.program-header-content > div.program-header-content__main > div > div.media__image > img')
        hippo_version_detail = hippo_information_soup.select('body > div.page > div:nth-child(2) > div > div > div > section.program-header-content > div.program-header-content__main > div > div.media__body > p.program-header__version')
        for item in hippo_information_data_name:
            hippo_information_name = item.get_text()
        # print (hippo_information_name,"\n")
        for item1 in hippo_information_data:
            hippo_information = item1.get_text()
        for item2 in hippo_version_detail:
            hippo_version = item2.get_text()
        for item3 in hippo_icon_url_detail:
            hippo_icon_url = item3.get('src')
        # hippo_information = str(hippo_information)
        # print (hippo_information)
        try:
            hippo_download_html_req = request.Request(url=hippo_download_html_url,headers=headers)
            hippo_download_html = urlopen(hippo_download_html_req)
            hippo_download_soup = BeautifulSoup(hippo_download_html.read(),"html.parser")
            hippo_download_data = hippo_download_soup.select('body > div.page > script:nth-child(2)')
            for item2 in hippo_download_data:
                    hippo_download_url = item2.get('data-qa-download-url')
            # print (hippo_download_url)
        except:
            hippo_search_result_list = [hippo_information_name,hippo_version,hippo_information,hippo_information_html_url,None,hippo_icon_url,fuzz.partial_ratio(app_name,hippo_information_name),"hippo"]
            hippo_search_result.append(hippo_search_result_list)
            return hippo_search_result
        else:
            hippo_search_result_list = [hippo_information_name,hippo_version,hippo_information,hippo_information_html_url,hippo_download_url,hippo_icon_url,fuzz.partial_ratio(app_name,hippo_information_name),"hippo"]
            hippo_search_result.append(hippo_search_result_list)
            # print(hippo_search_result)
            return hippo_search_result

def lensi_search_all(source,app_name,limmit_num):#搜索大函数
        if source == "360":
            return web_360_search(app_name,limmit_num)
        elif source == "qq":
            return web_qq_search(app_name,limmit_num)
        elif source == "Hippo":
            return hippo_search_easy(app_name)

def app_name_cmp(e):
    return e[6]

def Lensi_search(app_name):
    thread_360 = myThread( "360", app_name,1)
    thread_qq = myThread("qq", app_name,1)
    thread_H = myThread( "Hippo", app_name,1)
    #多线程
    search_result = []
    # 开启新线程
    thread_360.start()
    thread_qq.start()
    thread_H.start()
    #等待进程
    thread_360.join()
    thread_qq.join()
    thread_H.join()
    # print ("退出主线程")
    #判断结果是否为空
    if thread_360.get_result() != None :
        search_result.extend(thread_360.get_result())
    if thread_qq.get_result() != None :
        search_result.extend(thread_qq.get_result())  
    if thread_H.get_result() != None :  
        search_result.extend(thread_H.get_result())  
    # print(search_result)
    search_result.sort(key=app_name_cmp,reverse=True)
    return search_result
