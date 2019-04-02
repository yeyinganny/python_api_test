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
from API_7.common.public import get_data
from API_7.common.public.do_mysql import DoMysql

# 测试加标，审核到4状态
params = Read_Write_Case(data_path.data_path, 'add').read_data('AddCase')
TestResult = None


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
        #global COOKIES
        InputLog().info('正在执行{}模块第{}条测试用例:{}---'.format(case['Module'], case['CaseId'], case['Title']))
        InputLog().info('测试数据是：{}'.format(case))
        url = case['Url']
        method = case['Method']
        # 替换loanId
        #if case['Param'].find('loanId') != -1:# 如果请求参数中有loan_id,获取全局变量LOAN_ID的值
        #    case['Param'] = case['Param'].replace('loanId',str(getattr(GetData,'LOAN_ID'))) # 因为数据库里拿到的id值是int类型，replace只能用在字符串之间的替换
        #param = eval(case['Param'])
        param = eval(get_data.replace(case['Param']))
        resp = HttpRequest().request_method(url, param, method, cookie = getattr(get_data.GetData,'COOKIE'))
        # 判断是否要查询数据库
        if case['sql'] is not None:  # 判断用例表中sql是否为空,不为空，就是要进行数据库查询操作
            case['sql'] = get_data.replace(case['sql'])
            loan_id = DoMysql().do_mysql(eval(case['sql'])['sql'], 1)[0] # 数据库查询结果是元组类型的
            setattr(get_data.GetData, 'loan_id',str(loan_id)) # 利用反射,修改全局变量LOAN_ID的值
        if resp.cookies:  # http请求发生之后加一个判断，判断请求的cookies是否为空, 利用反射获取cookie值
            setattr(get_data.GetData,'COOKIE',resp.cookies)
        # 对比结果
        try:
            self.assertEqual(eval(case['ExpectedResult']), resp.json())
            TestResult = 'Pass'
            InputLog().info('{}模块第{}条用例{}测试通过'.format(case['Module'],case['CaseId'],case['Title']))
        except AssertionError as e:
            TestResult = 'Failed'
            InputLog().info('{}模块第{}条用例{}测试不通过，不通过原因：{}'.format(case['Module'],case['CaseId'],case['Title'], e))
            raise e
        finally:
            # 回写实际结果和测试结果
            t = Read_Write_Case(data_path.data_path, 'add')
            t.write_back(case['CaseId'] + 1, 9, resp.text)
            t.write_back(case['CaseId'] + 1, 10, TestResult)
        InputLog().info('实际结果：{}'.format(resp.json()))

