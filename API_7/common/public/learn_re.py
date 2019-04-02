# -*- coding: utf-8 -*-
# @Time   : 2019/3/27 9:45
# @Author : Tammy
# @Email  : 18585053@qq.com
# @File   : learn_re.py
"""
1.什么是正则表达式？编写一些规范查找需要的字符串
2.正则表达式的一个组成；原义字符和元字符
3.如何用Python来解析？
4.正则表达式的场景
----参数化
----查找一些特殊的字符：邮箱，手机号码，身份证号码
"""
import re
from API_7.common.public.get_data import GetData
# re模块常用的函数是 match() 从字符串开头位置开始匹配  search()对字符串的任意位置进行匹配
# findall() 返回字符串中所有匹配的子串，组成列表， finditer() 返回一个包含了所有匹配对象的

target = "{'mobilephone':'#mobile_phone#','memberid':'#member_id#'}"
p = 'mobile_phone' # 原义字符查找
p2 = '#(.*?)#' # 圆括号代表正则表达式里面组的概念
#m = re.match(p2, target)
#m = re.search(p2, target)  # 在目标字符串里面根据正则表达式来查找，有匹配的字符串，只查找一次
#key = m.group(1)
#value = getattr(GetData, key)
#target = re.sub(p2,value,target,count=1)
match_result = re.findall(p2, target)  #找到所有匹配的字符串，返回的是一个列表
print(match_result)
while re.search(p2, target):
    m = re.search(p2, target)
    key = m.group(1)
    value = getattr(GetData, key)
    target = re.sub(p2,value,target,count=1)
print(target)


