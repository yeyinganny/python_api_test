# -*- coding: utf-8 -*-
# @Time   : 2019/3/11 9:46
# @Author : Tammy
# @Email  : 18585053@qq.com
# @File   : http_request.py
'''1）http请求类（可以根据传递的method--get/post完成不同的请求），要求有返回值。'''
import requests
from API_7.common.public.input_log import InputLog

class HttpRequest:
    '''编写一个http请求类，可根据传递的参数完成不同的请求，要求有返回值'''

    @staticmethod
    def request_method(url, params, method, cookie):
        '''请求方法'''
        if method.lower() == 'get':
            try:
                resp = requests.get(url, params=params,cookies=cookie)
                return resp
            except Exception as e:
                print('请求报错：错误是{}'.format(e))
                InputLog().error(e)
        elif method.lower() == 'post':
            try:
                resp = requests.post(url, data=params,cookies=cookie)
                return resp
            except Exception as e:
                print('请求报错：错误是{}'.format(e))
                InputLog().error(e)


if __name__ == '__main__':
    url_1 = 'http://47.107.168.87:8080/futureloan/mvc/api/member/login'
    param_1 = {'mobilephone': '18813989009', 'pwd': '123456'}
    cookie =None
    resp_1 = HttpRequest().request_method(url_1, param_1, 'Get',cookie)
    print(resp_1.json())
    cookie = resp_1.cookies
    print(cookie)
    url_2 = 'http://47.107.168.87:8080/futureloan/mvc/api/member/recharge'
    param_2 = {'mobilephone': '18813989009', 'amount': '1000.00'}
    text_2 = HttpRequest().request_method(url_2, param_2, 'Get',cookie)
    print(text_2.text)






