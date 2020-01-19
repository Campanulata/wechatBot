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

