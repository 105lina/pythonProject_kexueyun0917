# @Time : 2021/9/17 16:07 
# @Author : lina
# @File : api_basic.py 
# @Software: PyCharm
'''
登陆成功，生成guid、token
'''
from common.confBasic import Confbasic
from util.request_handle import Request_handle
def login():
    requests=Request_handle(guid=None,token=None)
    host = Confbasic.host
    path = '/datasience/management/login'
    method = 'post'
    url = host+path
    print(url)
    body={'username':Confbasic.username,'password':Confbasic.password}
    response=requests.request_deal(method=method,url=url,data=body)
    res=response.json()
    if res['code']==1000:
        guid=res['data']['guid']
        token=res['data']['token']
        return guid,token
def logout():
    pass
class apiBasic:
    guid,token=login()
    #这块是为了所有执行request的请求的操作，都有guid、token
    http=Request_handle(guid,token)




