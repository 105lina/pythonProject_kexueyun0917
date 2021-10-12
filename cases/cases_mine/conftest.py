# @Time : 2021/9/16 17:08
# @Author : lina
# @File : conftest.py
# @Software: PyCharm
'''
模块的初始化
'''
import pytest
from util.tool import time_tostr
from api.managementProject import ManagementProject

@pytest.fixture(scope='module')
def fixture_createproject():
    #创建项目
    projectName="接口自动化新项目"+time_tostr(format='%Y%m%d%H%M%S')
    body={
        "projectName":projectName,
        "projectDesc":"",
        "icon":"",
        "isPublic":"0","tags":[]
    }
    res=ManagementProject.create_Project(body)
    projectid=res['data']['project']['id']
    projecticon = res['data']['project']['icon']
    yield list((projectName,projectid,projecticon))
    del_body={"id":projectid}
    response=ManagementProject.del_Project(del_body)
    assert response['code']==1000



