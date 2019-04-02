# -*- coding: utf-8 -*-
# @Time   : 2019/2/28 15:05
# @Author : Tammy
# @Email  : 18585053@qq.com
# @File   : homework1.py
'''1：编写一个日志类，能够实现输出文件到指定文件和console
'''
import logging
from API_7.common.public import data_path

class InputLog:
    '''写一个日志类，实现输出日志到指定文件和console'''
    def __init__(self):
        self.log_file = data_path.log_path

    def set_logger(self,level,msg):
        '''设置日志收集器'''
        mylogger = logging.getLogger('mylogger')
        mylogger.setLevel(level)#定义日志收集级别

        formatter = logging.Formatter(
            '%(asctime)s-%(levelname)s-%(filename)s-%(name)s-%(lineno)d行-日志信息:%(message)s')
        '''设置日志输出到控制台'''
        ch = logging.StreamHandler()
        ch.setLevel('INFO')#定义日志输出级别
        ch.setFormatter(formatter) #设置输出格式
        mylogger.addHandler(ch)
        '''设置日志输出到指定文件'''
        fh = logging.FileHandler(self.log_file, encoding='utf-8')
        fh.setLevel(level)  # 定义日志输出级别
        fh.setFormatter(formatter)  # 设置输出格式
        mylogger.addHandler(fh)

        if level == 'DEBUG':
            mylogger.debug(msg)
        elif level == 'INFO':
            mylogger.info(msg)
        elif level == 'WARNING':
            mylogger.warning(msg)
        elif level == 'ERROR':
            mylogger.error(msg)
        elif level == 'CRITICAL':
            mylogger.critical(msg)

        mylogger.removeHandler(ch)
        mylogger.removeHandler(fh)

        # 如果是描述型的信息用debug或info，
        # 如果是错误信息用error
    def debug(self,msg):
        self.set_logger('DEBUG',msg)

    def info(self,msg):
        self.set_logger('INFO',msg)

    def warning(self, msg):
        self.set_logger('WARNING',msg)

    def error(self, msg):
        self.set_logger('ERROR',msg)

    def critical(self, msg):
        self.set_logger('CRITICAL',msg)


if __name__ == '__main__':

    InputLog().info('程序出错了')






