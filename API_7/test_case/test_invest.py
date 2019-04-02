# -*- coding: utf-8 -*-
# @Time   : 2019/3/20 11:55
# @Author : Tammy
# @Email  : 18585053@qq.com
# @File   : test_addload.py

from API_7.common.public.input_log import InputLog
from API_7.common.public.http_request import HttpRequest
from API_7.common.public import data_path
from API_7.common.public.read_write_case import Read_Write_Case
import unittest
from ddt import ddt, data
from API_7.common.public.get_data import GetData
from API_7.common.public.do_mysql import DoMysql
from API_7.common.public import get_data

# 测试投资
params = Read_Write_Case(data_path.data_path, 'invest').read_data('AddCase')
TestResult = None
leave_amount_init = 0 # 定义初始余额为0
invest_amount = 0


@ddt
class TestApi(unittest.TestCase):
    '''自动执行用例'''
    def setUp(self):
        InputLog().info('开始执行用例')

    def tearDown(self):
        InputLog().info('用例执行完毕')

    @data(*params)
    def test_001(self, case):
        # 执行充值用例
        global TestResult
        global leave_amount_init
        global invest_amount
        #global COOKIES
        InputLog().info('正在执行{}模块第{}条测试用例:{}---'.format(case['Module'], case['CaseId'], case['Title']))
        InputLog().info('测试数据是：{}'.format(case))
        url = case['Url']
        method = case['Method']

        if case['sql'] is not None:  # 判断用例表中sql是否为空,不为空，就是要进行数据库查询操作
            case['sql'] = get_data.replace(case['sql'])
            # 投资之前查询用户余额
            loan_id = DoMysql().do_mysql(eval(case['sql'])['sql_1'], 1)[0]  # 从数据库获取标ID
            setattr(GetData, 'LOAN_ID', loan_id)  # 利用反射,修改全局变量LOAN_ID的值,
            leave_amount_init = DoMysql().do_mysql(eval(case['sql'])['sql'], 1)[0]
            InputLog().info('投资之前用户可用余额是{}'.format(leave_amount_init))
        #从get_data.py模块获取标ID的值
        param = eval(get_data.replace(case['Param']))
        # 发送请求
        resp = HttpRequest().request_method(url, param, method, getattr(GetData,'COOKIE'))
        # 发送请求后查询leave_amount的值
        if case['sql'] is not None:  # 判断用例表中sql是否为空,不为空，就是要进行数据库查询操作
            leave_amount = DoMysql().do_mysql(eval(case['sql'])['sql'], 1)[0]
            InputLog().info('投资之后用户可用余额是{}'.format(leave_amount))
            invest_amount = leave_amount_init - leave_amount  # invest_amount 是投资的金额
        if resp.cookies:  # http请求发生之后加一个判断，判断请求的cookies是否为空, 利用反射获取cookie值
            setattr(GetData,'COOKIE',resp.cookies)
        # 对比结果
        try:
            self.assertEqual(eval(case['ExpectedResult']), resp.json())
            # 加一个断言，判断param里面的amount是否等于投资前后余额的差
            if case['sql'] is not None: # 判断Param中是否有amount，有的话增加一个判断
                #print('param中amount的数据类型',type(param['amount']))
                self.assertEqual(float(param['amount']), invest_amount)
                case['sql'] = case['sql'].replace('loan_id', str(getattr(GetData, 'LOAN_ID')))
                # 另外一种方法查询数据库中该次竞标的投资金额，然后写回数据库
                amount = DoMysql().do_mysql(eval(case['sql'])['sql_2'], 1)[1]
                t = Read_Write_Case(data_path.data_path, 'invest')
                t.write_back(case['CaseId'] + 1, 11, amount)
                print('amount', amount)
            TestResult = 'Pass'
            InputLog().info('{}模块第{}条用例{}测试通过'.format(case['Module'],case['CaseId'],case['Title']))
        except AssertionError as e:
            TestResult = 'Failed'
            InputLog().info('{}模块第{}条用例{}测试不通过，不通过原因：{}'.format(case['Module'],case['CaseId'],case['Title'], e))
            raise e
        finally:
            # 回写实际结果和测试结果
            t = Read_Write_Case(data_path.data_path, 'invest')
            t.write_back(case['CaseId'] + 1, 9, resp.text)
            t.write_back(case['CaseId'] + 1, 10, TestResult)

        InputLog().info('实际结果：{}'.format(resp.json()))

