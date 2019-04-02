# -*- coding: utf-8 -*-
# @Time   : 2019/3/12 19:10
# @Author : Tammy
# @Email  : 18585053@qq.com
# @File   : test_api.py

from API_7.common.public.input_log import InputLog
from API_7.common.public.http_request import HttpRequest
from API_7.common.public import data_path
from API_7.common.public.read_write_case import Read_Write_Case
import unittest
from ddt import ddt,data
from API_7.common.public.get_data import GetData
from API_7.common.public.do_mysql import DoMysql
from API_7.common.public import get_data

# 测试充值
params = Read_Write_Case(data_path.data_path, 'recharge').read_data('RechargeCase')
TestResult = None
before_leave_amount = None
expect_amount = None
#COOKIES = None # 设定COOKIES 的初始值
@ddt
class TestApi(unittest.TestCase):
    '''自动执行用例'''
    def setUp(self):
        InputLog().info('开始执行用例')

    def tearDown(self):
        InputLog().info('用例执行完毕')

    @data(*params)
    def test_002(self,case):
        # 执行充值用例
        global TestResult
        global before_leave_amount
        global expect_amount
        #global COOKIES
        url = case['Url']
        param = eval(get_data.replace(case['Param']))
        method = case['Method']
        case['ExpectedResult'] = get_data.replace(case['ExpectedResult'])
        InputLog().info('正在执行{}模块第{}条测试用例:{}---'.format(case['Module'], case['CaseId'], case['Title']))
        InputLog().info('测试数据是：{}'.format(case))
        # 查询充值之前的余额
        if case['sql'] is not None:  # 判断用例表中sql是否为空,不为空，就是要进行数据库查询操作
            # 充值请求之后查询余额
            before_leave_amount = DoMysql().do_mysql(eval(case['sql'])['sql'], 1)[0]
            InputLog().info('充值之前用户可用余额是{}'.format(before_leave_amount))
        # 发送请求
        # resp = HttpRequest().request_method(url, param, method,cookies = COOKIES)
        resp = HttpRequest().request_method(url, param, method, getattr(GetData,'COOKIE'))
        if resp.cookies:  # 判断请求的cookies是否为空，不为空其实就是True，将cookies获取传给全局变量
            # COOKIES = resp.cookies # 更新全局变量的值
            setattr(GetData,'COOKIE',resp.cookies)
        # 对比结果
        try:
            if case['sql'] is not None:  # 判断用例表中sql是否为空,不为空，就是要进行数据库查询操作
                # 充值请求之后查询余额
                after_leave_amount = DoMysql().do_mysql(eval(case['sql'])['sql'], 1)[0]
                InputLog().info('充值之后用户可用余额是{}'.format(after_leave_amount))
                expect_amount = int(param['amount']) + before_leave_amount
                self.assertEqual(after_leave_amount, expect_amount)
                TestResult = 'Pass'
                InputLog().info('{}模块第{}条用例{}测试通过'.format(case['Module'],case['CaseId'],case['Title']))
            if case['ExpectedResult'].find('leave_amount') != -1:
                case['ExpectedResult'] = case['ExpectedResult'].replace('leave_amount', str(expect_amount))
                t = Read_Write_Case(data_path.data_path, 'recharge')
                t.write_back(case['CaseId'] + 1, 11, expect_amount)
                self.assertEqual(eval(case['ExpectedResult']), resp.json())
        except AssertionError as e:
            TestResult = 'Failed'
            InputLog().info('{}模块第{}条用例{}测试不通过，不通过原因：{}'.format(case['Module'],case['CaseId'],case['Title'], e))
            raise e
        finally:
            # 回写实际结果和测试结果
            t = Read_Write_Case(data_path.data_path, 'recharge')
            t.write_back(case['CaseId'] + 1, 9, resp.text)
            t.write_back(case['CaseId'] + 1, 10, TestResult)
        InputLog().info('实际结果：{}'.format(resp.json()))

