# @Time : 2021/9/17 11:42 
# @Author : lina
# @File : tool.py 
# @Software: PyCharm
'''
存放公共的数据处理
'''
import time
import datetime
#时间格式处理
def time_tostr(format="%Y-%m-%d %H:%M:%S"):
    """
    @param format:把时间戳按照format的样式进行格式化
    @return:
    """
    return datetime.datetime.now().strftime(format)

