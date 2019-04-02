# -*- coding: utf-8 -*-
# @Time   : 2019/3/21 15:46
# @Author : Tammy
# @Email  : 18585053@qq.com
# @File   : do_mysql.py
from mysql import connector
from API_7.common.public.configuration import ReadConfiguration
from API_7.common.public import data_path

class DoMysql:

    '''操作数据库，读取数据库里的数据  '''

    def do_mysql(self,query,flag):
        '''
        :query  sql查询语句
        :flag 标志位 1 获取一条数据，2 获取多条数据
        '''
        db_config = ReadConfiguration(data_path.config_path).read_other('DB','db_config')

        cnn = connector.connect(**db_config)  # 建立一个连接，参数中传入字典
        cursor = cnn.cursor()
        cursor.execute(query)
        #cursor.execute('commit')
        if flag == 1:
            res = cursor.fetchone()  # 获取一条数据, 如果只有一条数据用fetchone
        else:
            res = cursor.fetchall() # 获取所有查询的数据，  如果有多条数据用fetchall
        return res

if __name__ == '__main__':
    query = 'select Id from loan where MemberID = 1123931'
    res = DoMysql().do_mysql(query, 1)
    print('数据库的查询结果是{}'.format(res))