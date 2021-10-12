# @Time : 2021/9/17 11:01 
# @Author : lina
# @File : managementProject.py 
# @Software: PyCharm
'''
项目模块，真正的功能处理在这里
'''
from common.confBasic import Confbasic
from util.request_handle import Request_handle
from api.api_basic import apiBasic
class ManagementProject(apiBasic):
    @classmethod
    def create_Project(cls,body):
        host = Confbasic.host
        path = '/datasience/management/project/saveProject'
        method='post'
        url = host+path
        #使用with as总是报错AttributeError: __enter__
        # with cls.http.request_deal(method=method,url=url,data=body,param=None) as response:
        #     if response['code']==1000:
        #         return response
        response=cls.http.request_deal(method=method,url=url,data=body,param=None)
        res = response.json()
        print("\n创建项目create_Project:{0}".format(url))
        if res['code'] == 1000:
             return res
    @classmethod
    def del_Project(cls,body):
        host = Confbasic.host
        path = '/datasience/management/project/delProject'
        method = 'post'
        url = host+path
        # with Request_handle.request_deal(method=method, url=url, data=body, param=None) as response:
        #     if response.status_code == 200:
        #         return response
        response= cls.http.request_deal(method=method, url=url, data=body, param=None)
        print("\n删除项目del_Project:{0}".format(url))
        if response.status_code == 200:
            res = response.json()
            return res
    @classmethod
    def edit_Project(cls,body):
        host = Confbasic.host
        path = '/datasience/management/project/saveProject'
        method = 'post'
        url = host+path
        # with Request_handle.request_deal(method=method, url=url, data=body, param=None) as response:
        #     if response.status_code == 200:
        #         return response
        response = cls.http.request_deal(method=method, url=url, data=body, param=None)
        print("\n编辑项目edit_Project:{0}".format(url))
        if response.status_code == 200:
            res = response.json()
            return res
    @classmethod
    def search_projectlist(cls,body):
        host = Confbasic.host
        path = '/datasience/management/project/searchProject'
        method = 'post'
        url = host + path
        response = cls.http.request_deal(method=method, url=url, data=body, param=None)
        print("\n查找项目列表search_projectlist:{0}".format(url))
        if response.status_code == 200:
            res = response.json()
            return res
    @classmethod
    def copy_project(cls,body):
        host = Confbasic.host
        path = '/datasience/xquery/project/copy'
        method = 'post'
        url = host + path
        response = cls.http.request_deal(method=method, url=url, data=body, param=None)
        print("\n复制项目copy_project:{0}".format(url))
        if response.status_code == 200:
            res = response.json()
            return res