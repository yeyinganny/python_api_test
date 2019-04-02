# -*- coding: utf-8 -*-
# @Time   : 2019/2/27 16:17
# @Author : Tammy
# @Email  : 18585053@qq.com
# @File   : configuration.py
#写一个配置类 有以下几个函数：
#1：读取整数
#2：读取浮点数
#3：读取布尔值
#4：读取其他类型的数据 list tuple dict eval（）
#5：读取字符串

from openpyxl import load_workbook
from configparser import ConfigParser
from API_7.common.public.input_log import InputLog


class ReadConfiguration:
    '''创建一个配置类'''

    def __init__(self,filename):
        self.cf = ConfigParser()
        # 打开文件
        self.cf.read(filename, encoding='utf-8')

    def read_int(self,section,option):
        # 获取整数类型
        try:
            data = self.cf.getint(section, option)
            return data
        except Exception as e:
            print('option的值不是int型,错误是{}'.format(e))
            InputLog().error(e)


    def read_float(self,section, option):
        # 获取float类型
        try:
            data = self.cf.getfloat(section, option)
            return data
        except Exception as e:
            print('option的值不是float型,错误是{}'.format(e))
            InputLog().error(e)

    def read_boolean(self,section, option):
        # 获取boolean类型
        try:
            data = self.cf.getboolean(section, option)
            return data
        except Exception as e:
            print('option的值不是boolean型,错误是{}'.format(e))
            InputLog().error(e)

    def read_other(self,section, option):
        # 读取是字典、列表、元组类型
        try:
            data = self.cf.get(section, option)
            return eval(data) #把括号里的数据变成原来的数据类型,可用于除字符串以外的类型
        except Exception as e:
            print('错误是{}'.format(e))
            InputLog().error(e)


    def read_str(self,section, option):
        #  获取字符串类型
        try:
            data = self.cf.get(section, option)
            return data
        except Exception as e:
            print('错误是{}'.format(e))
            InputLog().error(e)


if __name__ == '__main__':
    rcf = ReadConfiguration('E:\\Python Project\\test\API_2\\common\\conf\\configuration.conf')
    data = rcf.read_int('TestCase', 'case_id')
    print(data)








