# -*- coding: utf-8 -*-
# @Time   : 2019/3/14 14:23
# @Author : Tammy
# @Email  : 18585053@qq.com
# @File   : run.py

import sys
sys.path.append('./')
print(sys.path)
# 执行用例，生成测试报告
import unittest
import HTMLTestRunnerNew
from API_7.common.public import data_path
from API_7.test_case import test_addloan
from API_7.test_case import test_invest

# 新建一个测试集
suite = unittest.TestSuite()

# 添加用例
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(test_addloan.TestApi)) #参数是类名
suite.addTest(loader.loadTestsFromTestCase(test_invest.TestApi))

# 执行用例 生成测试报告
with open(data_path.report_path,'wb') as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file,verbosity=2,title='0329测试报告',description='0329测试报告',tester='Tammy')
    runner.run(suite) # 执行用例， 传入suite，suite 收集了我们的测试用例
