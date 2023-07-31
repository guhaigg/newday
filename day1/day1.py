# 语法串讲
# day1
# 信创工程
# 信息技术应用创新产业  国产化
# 年会抽奖作业
# 一等奖3个 二等奖6个 三等奖30个
# 共抽三次，第一次抽三等奖 30个
# 第二次抽二等奖   6个
# 第三次抽一等奖   3个
# 每个员工只能中奖一次，不能重复中奖
# 1. 生成一个员工列表   300个员工      0-299    range(300)
# 员工列表 listYG = [i for i in range(300)]
import random as r
listYG = [i for i in range(300)]
listYG3 = []
listYG2 = []
listYG1 = []
for i in range(30):
    listYG3.append(listYG.pop(r.randint(0, len(listYG)-1)))
for i in range(6):
    listYG2.append(listYG.pop(r.randint(0, len(listYG)-1)))
for i in range(3):
    listYG1.append(listYG.pop(r.randint(0, len(listYG)-1)))
print(len(listYG))
print(f'获得三等奖的员工有{listYG3}')
print(f'获得二等奖的员工有{listYG2}')
print(f'获得一等奖的员工有{listYG1}')





