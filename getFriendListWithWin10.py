# -*-coding:utf-8 -*-
import requests
import json
from api import *
import pandas as pd
import os
import xlsxwriter

# 需要替换的前后缀按实例格式补充
replaceList=['-','21848','54525','母亲','父亲','本人','其他','40401','40405','34740','21788','21841','24702','34753']

# 获取好友列表；存储为json文件
friendList = get_friend_list()
with open ('friendList.json','w', encoding="utf-8") as file:
    file.write(json.dumps(friendList,indent=2,ensure_ascii=False))
# 读取json
df = pd.read_json("friendList.json",encoding='utf-8')
df = df.drop(['robot_wxid','nickname'],axis=1)
df = df[['note','wxid']]
dft = df
for i in replaceList:
  df['note']=dft['note'].str.replace(i,'')
# 存储为xlsx文件
path = os.path.dirname(os.path.abspath(__file__))
output_file = os.path.join(path, 'friendList.xlsx')
df.to_excel(output_file,index=False,engine="xlsxwriter")