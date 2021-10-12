# @Time : 2021/9/16 16:22 
# @Author : lina
# @File : test_project.py 
# @Software: PyCharm
'''
我的-项目功能用例
'''
from api.managementProject import ManagementProject
import pytest
import os


@pytest.fixture(scope='module', autouse=True)
def fixture_prepare(fixture_createproject):
    # 用例执行前的数据准备projectid、projectname、projecticon
    global projectname
    global projectid
    global projecticon
    projectname = fixture_createproject[0]
    projectid = fixture_createproject[1]
    projecticon = fixture_createproject[2]

#用例case
class Test_mine:
    # 模块类执行之前先执行初始化，打印执行的文件信息
    def setup_class(self):
        info = "\n开始执行文件：%s" % os.path.split(os.path.realpath(__file__))[1]
        print(info)

    def teardown_class(self):
        info = "\n退出 文件: %s " % os.path.split(os.path.realpath(__file__))[1]
        print(info)

    # 用例执行之前先进行方法初始化，打印执行的用例信息
    def setup_method(self, method):
        info = "\n开始执行类：%s 中的用例:%s" % (type(self).__name__, method.__name__)
        print(info)

    def teardown_method(self, method):
        info = "\n结束执行类：%s 中的用例:%s" % (type(self).__name__, method.__name__)
        print(info)

    # 编辑项目
    def test_EditProject(self):
        body = {
            "id": projectid,
            "projectName": projectname,
            "isPublic": "0",
            "projectDesc": "自动化测试编辑操作",
            "icon": projecticon,
            "tags": []
        }
        response = ManagementProject.edit_Project(body=body)
        assert response['code'] == 1000
    # #查看项目详情
    # def test_ProDetail(self):
    #     pass
    #项目列表
    def test_ProjectList(self):
        body={
            "key":"",
            "tagId":"",
            "pageSize":15,
            "pageNum":1,
            "role":"3",
            "sortField":"last_modify",
            "sortType":"desc"
        }
        response=ManagementProject.search_projectlist(body=body)
        assert response['code'] == 1000
    # #通过用户id查找项目
    # def test_SearchProByGuid(self):
    #     pass
    # #删除项目
    # def test_DeletePro(self):
    #     pass
    #复制项目
    def test_CopyProject(self):
        body={
            "id":projectid,
            "projectName":projectname,
            "isPublic":"0"
        }
        response = ManagementProject.copy_project(body=body)
        assert response['code'] == 1000
    # #导出项目
    # def test_ExporPro(self):
    #     pass
    # #导出项目后下载到本地
    # def test_ExporProTolocal(self):
    #     pass
    # #分享项目
    # def test_SharePro(self):
    #     pass
