def DiffValue(fraction):
    molecule = fraction.split('/')[0]
    denominator = fraction.split('/')[1]
    molecule = int(molecule)
    denominator = int(denominator)
    return denominator - molecule

def leftOfSlash(fraction):
    molecule = fraction.split('/')[0]
    molecule = int(molecule)
    return molecule

def feedback(time_live, grade, name):
    if time_live > 100:
        str1 = '一共听了' + str(time_live) + '分钟的直播课程，非常好/:strong~'
    elif time_live > 0:
        str1 = '没有坚持听完，只听了' + str(time_live) + '分钟的直播课程，剩下的尽快补一下回放，千万不要影响明天的课程~'
    elif time_live == 0:
        str1 = '孩子由于时间原因没有参加今天的直播课，'

    if grade > 100:
        str2 = '但是作业还没完成，及时在APP内提交一下，我帮孩子批改/:moon'
    elif grade < 50:
        str2 = '然后作业已经改完了，但是错的比较多，明天课前15min按时来听习题讲解[Smart]'
    else:
        str2 = '然后作业已经改完了，今天的内容都吸收了，得了' + str(grade) + '分[Yeah!]'

    str0 = '家长你好，今天' + str(name) + '的物理课学习的重点是平抛运动，孩子中午'
    str3 = ' '

    str_all = str0 + str1 + str2 + str3

    return str_all


def salary(name, times):
    if times > 0:
        return '家长你好，' + str(name) + '目前还有' + str(times) + '次作业没有提交。临近月考，麻烦家长督促孩子完成作业，便于发现孩子目前物理存在的问题'
    else:
        return

