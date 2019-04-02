# -*- coding: utf-8 -*-
# @Time   : 2019/3/20 10:49
# @Author : Tammy
# @Email  : 18585053@qq.com
# @File   : get_data.py
import re
from API_7.common.public.configuration import ReadConfiguration
from API_7.common.public.data_path import config_path


class GetData:
    '''类的反射可以动态的查看、更改、删除、获取类的属性'''
    COOKIE = None  # 类属性
    #LOAN_ID = None  # 设置标id
    config = ReadConfiguration(config_path)  # 创建一个对象
    mobile_phone = config.read_str('data','mobile_phone')
    pass_word = config.read_str('data','pass_word')
    member_id = config.read_str('data','member_id') # 用户ID


def replace(target):
    p2 = '#(.*?)#'  # 正则表达式
    while re.search(p2, target):
        m = re.search(p2, target)
        key = m.group(1)
        value = getattr(GetData, key) # 拿到我们需要去替换的值
        target = re.sub(p2, value, target, count=1)
    return target

#print(GetData.COOKIE)
#print(GetData().COOKIE)

if __name__ == '__main__':
    # 利用反射的方法拿值
    # 获取属性值
    print(getattr(GetData, 'COOKIE'))  # 第一个参数是类名，第二个参数是属性名
    # 判断是否存在这个属性
    print(hasattr(GetData, 'COOKIE'))  # 第一个参数是类名，第二个参数是属性名，返回布尔值
    # 设置属性值,或增加属性
    setattr(GetData, 'COOKIE', '123456')  # 第一个参数是类名，第二个参数是属性名，第三个参数是要设置的新属性值
    print(getattr(GetData, 'COOKIE'))
    # 删除类的属性
    # delattr(GetData, 'COOKIE')
    # print(getattr(GetData, 'COOKIE'))



