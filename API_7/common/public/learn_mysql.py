# -*- coding: utf-8 -*-
# @Time   : 2019/3/21 10:53
# @Author : Tammy
# @Email  : 18585053@qq.com
# @File   : learn_mysql.py

# 操作mysql
# 可以用pymysql  或 mysql-connector-python
# 在cmd里直接安装 pip install pymysql   pip install mysql-connector-python

from mysql import connector

# 第一步：连接数据库, 提供数据库的连接信息
db_config = {'host': '47.107.168.87',
             'user': 'python',
             'password': 'python666',
             'port': '3306',
             'database': 'future'}
cnn = connector.connect(**db_config)  # 建立一个连接，参数中传入字典

# 第二步：获取游标，即获取操作数据库的权限
cursor = cnn.cursor()

# 第三步：操作数据表
query = 'select * from member where ID<23537'
cursor.execute(query)

# 第四部：打印结果
print(cursor.fetchone())  # 获取一条数据, 如果只有一条数据用fetchone
# print(cursor.fetchall())  # 获取所有查询的数据，  如果有多条数据用fetchone

