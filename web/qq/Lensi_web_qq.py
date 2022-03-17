'''
Author: your name
Date: 2022-03-14 15:18:54
LastEditTime: 2022-03-14 15:20:02
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \Lensi\web\qq\Lensi_web_qq.py
'''
from urllib import request
from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup
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

def web_qq_search(app_name):
    headers = {'User-Agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763'}
    # app_name = "geek"
    qq_search_url = 'https://s.pcmgr.qq.com/tapi/web/searchcgi.php?type=search&callback=searchCallback&keyword='+ app_name +'&page=1&pernum=1&more=0'
    qq_html_req = request.Request(url=qq_search_url,headers=headers)
    qq_html = urlopen(qq_html_req)
    qq_soup = BeautifulSoup(qq_html.read(),"html.parser")
    qq_str = str(qq_soup)
    '''
    TODO 未使用正则表达式 待优化
    '''
    # print(qq_str)
    qq_name = qq_str[int(qq_str.find('<![CDATA[')):int(qq_str.find("]",qq_str.find("<![CDATA[")))].strip("<![CDATA[")
    qq_version = qq_str[int(qq_str.find('<versionname>')):int(qq_str.find("&lt",qq_str.find("<versionname>")))].strip("<versionname>")
    qq_download = qq_str[int(qq_str.find('[CDATA[http:')):int(qq_str.find("]",qq_str.find("[CDATA[http:")))].strip("![CDATA[")
    qq_id = qq_str[int(qq_str.find('{"SoftID":"')):int(qq_str.find(',',qq_str.find('{"SoftID":"')))].strip('{"SoftID":"')
    qq_download_url = qq_download.replace('\\',"")
    qq_search_all = [qq_name,qq_id,qq_version,qq_download_url]
    return qq_search_all
    # print (qq_name,"\n","Version:",qq_version,"\n",qq_download_url,"\n")

def web_qq_number():
    headers = {'User-Agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763'}
    url = 'https://pc.qq.com/category/c0.html'
    req = request.Request(url=url,headers=headers)
    html = urlopen(req)
    soup = BeautifulSoup(html.read(),"html.parser")
    data = soup.select('body > div.category-wrap > div.category-siderbar.J_category_siderbar > div > ul > li.cat-item.J_select_class_li.cat-curr > a')
    for item in data:
        name = str(item.get_text())
    number_list = re.findall(r"\d+\.?\d*",name)
    number = number_list[0]
    print(number)