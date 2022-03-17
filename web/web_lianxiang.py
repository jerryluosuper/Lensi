'''
Author: your name
Date: 2022-02-20 21:28:15
LastEditTime: 2022-03-01 20:45:06
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \Work\Lensi\web_lianxiang.py
'''
import requests        #导入requests包
import json

'''
TODO 未使用完成post失败 待优化
'''

url = 'https://lestore.lenovo.com/api/webstorecontents/download/getDownloadUrl'
headers = {'content-encoding': 'gzip',
'content-type':'application/json;charset=UTF-8',
'date': 'Tue, 01 Mar 2022 11:56:37 GMT',
'strict-transport-security': 'max-age=15724800;includeSubDomains',
'vary': 'Accept-Encoding',
'x-powered-by': 'Express'}
From_data={
'authority': 'lestore.lenovo.com',
'method': 'POST',
'path': '/api/webstorecontents/download/getDownloadUrl',
'scheme': 'https',
'accept': 'application/json,text/plain, */*',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
'content-length': '99',
'content-type': 'application/json;charset=UTF-8',
'cookie': 'avatar_name=41209ab9-acf3-400c-bcb9-cd0814b3ad5c; avt_v=vid%3D%3E17edec244ac605b%7C%7C%7Cfsts%3D%3E1644414780586%7C%7C%7Cdsfs%3D%3E19919%7C%7C%7Cnps%3D%3E11; avt_s=lsts%3D%3E1646135804140%7C%7C%7Csid%3D%3E7999688612%7C%7C%7Cvs%3D%3E3%7C%7C%7Csource%3D%3Edirect%7C%7C%7Cpref%3D%3Ehttps%3A//lestore.lenovo.com/%7C%7C%7Cref%3D%3Ehttps%3A//lestore.lenovo.com/search%3Fk%3Dgeek',
'dnt': '1',
'origin': 'https://lestore.lenovo.com',
'referer': 'https://lestore.lenovo.com/detail/23258',
'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Microsoft Edge";v="98"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Windows"',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-origin',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.56'}
response = requests.post(url,data=From_data,headers=headers)
content = json.loads(response.text)
print(response.text)
print(content)
