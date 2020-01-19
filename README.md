# wechatBot

项目地址:[https://github.com/Campanulata/wechatBot](https://github.com/Campanulata/wechatBot)
单击 clone or download——download zip 即可下载

微信机器人 私聊发送消息 无延迟。
微信接口:[可爱猫官网](http://www.keaimao.com/)

## 一、安装

* 安装vscode[https://code.visualstudio.com/docs/?dv=win64user](https://code.visualstudio.com/docs/?dv=win64user)
* 安装Python[https://www.liaoxuefeng.com/wiki/1016959663602400/1016959856222624](https://www.liaoxuefeng.com/wiki/1016959663602400/**1016959856222624**)

## 二、打开可爱猫微信

1. 退出所有微信
2. 打开 可爱猫.exe
3. 此时会自动弹出微信 登录(可能会提示安装指定版本微信)
4. 设置——关闭自动更新——关闭开机自启

## 三、其他文件说明

1. friendList.xlsx(微信好友列表)
    表格结构如下

    | note   | wxid                |
    | ------ | ------------------- |
    | 梅冬旭 | wxid_n47rlybduhx822 |
    | 刘心怡 | wxid_grsqn2eqlknb22 |

    第一列是微信好友的备注，已经去除了非中文字符和后缀，只保留姓名，去除方法在下一个文件中。
    第二列是微信好友的唯一识别id，接口通过这个wxid识别发送对象。
2. getFriendListWithWin10.py
    本文件用来生成刚才的表格，直接生成得到的备注为**小班id-姓名-身份**的格式，为了方便使用vlookup，已经去除了非中文字符和['母亲','父亲','自己','其他','本人']五个词语。如有需要，在第10行代码中按格式添加即可。

    ```python
    replaceList=['母亲','父亲','自己','其他','本人']
    ```

3. sendMsg.xlsx——数据库
    表格结构如下

    | 课程id | 小班id | 学员uin            | 姓名   | wxid                |
    | ------ | ------ | ------------------ | ------ | ------------------- |
    | 131163 | 40401  | 144115213635331595 | 陈九洲 | wxid_m3qo6txxs6g322 |
    | 131163 | 40401  | 144115213592531328 | 兰欣悦 | wxid_vrboab5zmymo21 |

    这张表格用来存放所有学员的wxid，以便之后使用，前4列从工作台中导出，第5列wxid已经写好了vlookup函数，向下填充即可。
4. sendMsg.xlsx——textMsg
    表格结构如下

    | uid                | name | msg     | wxid                |
    | ------------------ | ---- | ------- | ------------------- |
    | 144115213635331595 | 张三 | 家长··· | wxid_m3qo6txxs6g322 |
    | 144115213592531328 | 李思 | 家长··· | wxid_vrboab5zmymo21 |

    前三列由学情反馈生成，最后一列用vlookup在数据库中查找出来。
5. sendTextMsg.py
    这个文件可以直接运行，运行后会把textMsg中的所有消息发送出去，把第三列msg的内容发送给第四列wxid的用户。目前没有设置延迟。

## 四、准备工作

第一次使用还需要安装一些依

1. 打开vscode
2. Ctrl+k
3. Ctrl+o
4. 选择wechatBot文件夹
5. 此时程序应该如图所示
  ![](https://raw.githubusercontent.com/Campanulata/pic/master/temp/QQ截图20200106114205.png)

6. 复制这行代码

    ```python
    pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
    ```

7. Ctrl+`(在Tab上方)
8. Ctrl+v
9. 回车
10. 等待2min左右，代码不再刷新即可

## 五、开始使用

这一节将介绍自动发送如何和学情反馈一起使用
之前教学反馈的表格已经可以生成2列，姓名和反馈。为了搭配自动发送，需要在姓名列前增加一列uid，直接用公式
=基本信息!A2
然后向下填充即可

1. 首先我们把学情反馈的数据粘贴到sendMsg.xlsx的textMsg中，此时第四列应该都是空值
2. 打开vscode——单击getFriendListWithWin10.py——F5运行——此时可以得到friendList.xlsx
3. 工作台导出学员信息粘贴到数据库表中，此时wxid列会自动生成，没有生成的可能有以下原因

   * 未添加微信好友
   * 微信好友未改备注
   * friendList.xlsx中的学生姓名有多余字符
   把多余字符按格式添加到getFriendListWithWin10.py的第10行，然后重新F5运行
   * 如果还未全部生成可自行排查或者直接手动从friendList中粘贴到数据库

4. 打开textMsg——确保每条数据都有wxid——F5运行——即可全部发送完成
