import pandas as pd
import os
import xlsxwriter


def DiffValue(fraction):
    molecule = fraction.split('/')[0]
    denominator = fraction.split('/')[1]
    molecule = int(molecule)
    denominator = int(denominator)
    return denominator - molecule


def feedback(time_live, grade, name):
    if time_live > 100:
        str1 = '一共听了' + str(time_live) + '分钟的直播课程，继续保持~'
    elif time_live > 0:
        str1 = '昨天中午可能来晚了，只听了' + str(time_live) + '分钟的直播课程，剩下的可以看一下回放~'
    elif time_live == 0:
        str1 = '孩子由于时间原因没有参加今天的直播课，'

    if grade > 100:
        str2 = '但是作业还没有提交，尽量在今天完成，避免影响今天的课程'
    elif grade < 60:
        str2 = '然后作业已经改完了，但是没有及格，因为前两节知识是连贯的，所以如果有知识盲区一定要解决'
    else:
        str2 = '然后作业已经改完了，掌握的很不错，得了' + str(grade) + '分，加油~'

    str0 = '家长你好，和您反馈一下' + str(name) + '的物理学习情况：昨天学习的是功和功率，'
    str3 = '^_^'

    str_all = str0 + str1 + str2 + str3

    return str_all


def salary(name, times):
    if times > 0:
        return '家长你好，' + str(name) + '目前还有' + str(times) + '次作业没有提交。临近月考，麻烦家长督促孩子完成作业，便于发现孩子目前物理存在的问题'
    else:
        return


# 作业表uid+真实姓名+sum
dfWork = pd.read_excel('./学情反馈解决方案/work.xls')
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

######
#file0 = input("1.请确保学生基本信息表与本程序在同一目录下2.输入工作簿的文件名（不用输入.xlsx）然后按Enter进入下一步")
# file_name = file0 + '.xlsx'
# times = input("3.请问反馈第几次的学习情况？输入阿拉伯数字后按Enter")
print('打开该目录下的文件：feedback.xlsx')

# 读取 pd.read_excel(r'D:/source.xlsx', usecols='A:D,H')
df = pd.read_excel('./学情反馈解决方案/data.xlsx')          # 读取数据源表
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
