# @Time : 2021/9/16 15:52 
# @Author : lina
# @File : request_handle.py 
# @Software: PyCharm
'''
request请求处理
'''
import requests
from common.confBasic import Confbasic
class Request_handle:
    def __init__(self,guid,token):
        #初始化赋值guid,token
        self.guid=guid
        self.token=token
        self.authentication={'guid': self.guid, 'token': self.token}
    headers=Confbasic.headers
    content_type=Confbasic.content_type
    #requests处理web请求
    def request_deal(self,method,url,data,param=None):
        #param为None，把guid、token放到param中
        if param is  None:
            param=self.authentication
        if method=='get':
            try:
                response=requests.get(url=url,params=param,headers=self.headers)
                res=response.json()
                return res
            except Exception as e:
                print(e)
        elif method=='post':
            try:
                #根据content_type判断提交方式
                if self.content_type=='application/json;charset=UTF-8':
                    response=requests.post(url=url,json=data,headers=self.headers,params=param)
                    return response
                elif self.content_type=='application/x-www-form-urlencoded;charset=utf-8':
                    response = requests.post(url=url, data=data, headers=self.headers, params=param)
                    res = response.json()
                    return res
            except Exception as e:
                print(e)
        else:
            print("不支持的请求方法{0}：{1}".format(method,url))
