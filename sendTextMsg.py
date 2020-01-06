# -*- coding: UTF-8 -*-
import pandas as pd
import os
import xlsxwriter
from api import *
from flask import Flask, request, jsonify
# 读取test文件
df = pd.read_excel('sendMsg.xlsx')


# 获取自己的微信id
friendList = get_friend_list()
id = friendList[000]["robot_wxid"]

# 使用sendTextMsg发送微信消息
df.apply(lambda row: send_text_msg(id,row["wxid"],row["msg"]),axis=1)