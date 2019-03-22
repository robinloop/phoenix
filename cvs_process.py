# -*- coding:utf-8 -*-

"""
@author:bairubin
@file:cvs_process.py
@description:
@time:2019/3/18
"""
import pandas as pd
import eel

csv = pd.read_csv('F:/data/test.csv', encoding='gbk')


@eel.expose
def get_header():
    title = []
    [title.append(i) for i in csv.columns]
    return title


header = get_header()
[print(i) for i in header]
print(header)
