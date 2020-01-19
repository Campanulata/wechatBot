import pandas as pd
import os
import xlsxwriter
from fun import *

# 作业表uid+真实姓名+sum
dfWork = pd.read_excel('./学情反馈解决方案/work.xls')
dfLive = pd.read_excel('./学情反馈解决方案/live.xlsx')
dfLive.rename(columns={'学员姓名':'真实姓名'},inplace=True)
# 分数表=>sum
dfGrade = pd.read_excel('./学情反馈解决方案/work.xls', usecols=[7, 8, 9, 10, 11, 12])
dfGrade = dfGrade.replace('未提交', 1000)
dfGrade = dfGrade.astype(int)
dfWork['sum'] = dfGrade.apply(lambda x: x.sum(), axis=1)
dfWork.rename(columns={'学生uin':'学员uid'},inplace=True)
print(dfWork)
# 写入
path = os.path.dirname(os.path.abspath(__file__))
output_file = os.path.join(path, 'dataWork.xlsx')
dfWork.to_excel(output_file, index=False, engine="xlsxwriter")

dfLive['live'] = dfLive.apply(lambda row: leftOfSlash(row['本节直播']), axis=1)

dfAll = pd.merge(dfLive,dfWork.loc[:,['真实姓名','sum']])
output_file = os.path.join(path, 'dfAll.xlsx')
dfAll.to_excel(output_file, index=False, engine="xlsxwriter")

######
#file0 = input("1.请确保学生基本信息表与本程序在同一目录下2.输入工作簿的文件名（不用输入.xlsx）然后按Enter进入下一步")
# file_name = file0 + '.xlsx'
# times = input("3.请问反馈第几次的学习情况？输入阿拉伯数字后按Enter")
print('打开该目录下的文件：feedback.xlsx')

# 读取 pd.read_excel(r'D:/source.xlsx', usecols='A:D,H')
df = pd.read_excel('./学情反馈解决方案/dfAll.xlsx')          # 读取数据源表
df[['live', 'sum']] = df[['live', 'sum']].astype(int)
# df['未提交作业次数'] = df.apply(lambda row: DiffValue(row['作业提交']), axis=1)


print(df)

# df_time = pd.read_excel('df_time.xlsx')     # 读取时间表
# df_grade = pd.read_excel('df_grade.xlsx')   # 读取分数表
# df = pd.merge(df,df_time.loc[:,['学号','核心课程第1节直播','核心课程第1节回放']],how='left',on = '学号') # vlookup 直播，回放时间
df['live'].astype('int')
# dfi = pd.merge(df, dfWork.loc[:, ['学员uid', 'sum']], how='left', on='学员uid')
df['反馈'] = df.apply(lambda row:feedback(row['live'],row['sum'],row['真实姓名']),axis=1)
# dfi['反馈1'] = dfi.apply(lambda row: salary(row['姓名'], row['未提交作业次数']), axis=1)

df2 = df[['学员uid', '真实姓名', '反馈']]


# 写入
path = os.path.dirname(os.path.abspath(__file__))
output_file = os.path.join(path, 'feedback.xlsx')
df2.to_excel(output_file, index=False, engine="xlsxwriter")
work_sum = os.path.join(path, 'work_sum.xlsx')
df.to_excel(work_sum, index=False,)
# df2.to_excel(output_file,index=False)
