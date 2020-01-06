# -*-coding:utf-8 -*-
import requests
import json
from api import *
import pandas as pd
import os
import xlsxwriter

replaceList=['母亲','父亲','自己','其他','本人']


df = pd.read_json("friendList.json",encoding='utf-8')
df = df.drop(['robot_wxid','nickname'],axis=1)
df = df[['note','wxid']]

for i in replaceList:
  df['note']=df['note'].str.replace(i,'')

df['note']=df['note'].str.replace('[^\u4e00-\u9fa5]','',regex=True)

# 存储为xlsx文件
path = os.path.dirname(os.path.abspath(__file__))
output_file = os.path.join(path, 'friendList.xlsx')
df.to_excel(output_file,index=False,engine="xlsxwriter")