# -*-coding:utf-8 -*-
import requests
import json
from api import *
import pandas as pd
import os
import xlsxwriter

# 需要替换的前后缀按实例格式补充(仅中文)
replaceList=['母亲','父亲','自己','其他','本人']
# 获取好友列表；存储为json文件
friendList = get_friend_list()
with open ('friendList.json','w', encoding="utf-8") as file:
    file.write(json.dumps(friendList,indent=2,ensure_ascii=False))
# 读取json
df = pd.read_json("friendList.json",encoding='utf-8')
df = df.drop(['robot_wxid','nickname'],axis=1)
df = df[['note','wxid']]
# 删除非中文字符
df['note']=df['note'].str.replace('[^\u4e00-\u9fa5]','',regex=True)
# 删除不需要的中文
for i in replaceList:
  df['note']=dft['note'].str.replace(i,'')
# 存储为xlsx文件
path = os.path.dirname(os.path.abspath(__file__))
output_file = os.path.join(path, 'friendList.xlsx')
df.to_excel(output_file,index=False,engine="xlsxwriter")