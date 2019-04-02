# -*- coding: utf-8 -*-
# @Time   : 2019/3/12 14:37
# @Author : Tammy
# @Email  : 18585053@qq.com
# @File   : data_path.py
import os


# 通过切割后再拼接获取测试用例test_api.xlsx 的路径
path = os.path.split(os.path.split(os.path.split(os.path.realpath(__file__))[0])[0])[0]

# 测试数据的路径
data_path = os.path.join(path,'test_case','test_api.xlsx')

# 配置文件的路径
config_path = os.path.join(path,'common','conf','configuration.conf')

# 日志文件的路径
log_path = os.path.join(path,'test_result','test_log','test.log')

# 测试报告的路径
report_path = os.path.join(path,'test_result','test_report','0319_test_report.html')
