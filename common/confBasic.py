# @Time : 2021/9/16 16:50 
# @Author : lina
# @File : confBasic.py 
# @Software: PyCharm
'''
存放公共的基本信息
'''
class Confbasic:
    #测试环境
    host="https://testhb.turingtopia.com"
    headers={
        'content-type':'application/json;charset=UTF-8'
    }
    #控制requests的post请求的body是传给data还是json
    content_type='application/json;charset=UTF-8'
    username='lina01'
    password='lina01'
