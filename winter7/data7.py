import pandas as pd
import numpy as np
import os
import xlsxwriter

def leftOfSlash(fraction):
    molecule = fraction.split('/')[0]
    molecule = int(molecule)
    return molecule

for i in range(4):
  i=str(i+1)
  dfi = 'df' + i
  sheet = 'Sheet' + i
  live = 'live' + i
  back = 'back' + i

  df = pd.read_excel('./winter7/data7.xlsx',dtype={'学员uid':str},sheet_name=sheet)
  df[['本节直播','本节回放']]=df[['本节直播','本节回放']].astype(str)
  df=df.dropna()
  df[live] = df.apply(lambda row: leftOfSlash(row['本节直播']), axis=1)
  df[back] = df.apply(lambda row: leftOfSlash(row['本节回放']), axis=1)

  fileName = 'df' + str(i) + '.xlsx'
  path = os.path.dirname(os.path.abspath(__file__))
  output_file = os.path.join(path, fileName)
  df.to_excel(output_file, index=False, engine="xlsxwriter")

df1 = pd.read_excel('./winter7/df1.xlsx',dtype={'学员uid':str},sheet_name='Sheet1')
df2 = pd.read_excel('./winter7/df2.xlsx',dtype={'学员uid':str},sheet_name='Sheet1')
df3 = pd.read_excel('./winter7/df3.xlsx',dtype={'学员uid':str},sheet_name='Sheet1')
df4 = pd.read_excel('./winter7/df4.xlsx',dtype={'学员uid':str},sheet_name='Sheet1')


df = pd.merge(df1,df2.loc[:,['学员uid','live2','back2']],on='学员uid')
df = pd.merge(df,df3.loc[:,['学员uid','live3','back3']],on='学员uid')
df = pd.merge(df,df4.loc[:,['学员uid','live4','back4']],on='学员uid')

df.sort_index(axis=1,inplace = True)

path = os.path.dirname(os.path.abspath(__file__))
output_file = os.path.join(path, '学员直播回放数据.xlsx')
df.to_excel(output_file, index=False, engine="xlsxwriter")
