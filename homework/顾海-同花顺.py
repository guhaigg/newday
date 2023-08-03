import random

leat = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
color = ['红桃', '黑桃', '方块', '梅花']
poker = set()

for i in color:
    for j in leat:
        poker.add(i + str(j))
pokers = list(poker)
poker_all = []

for j in range(1, 6):
    pokes_end = []
    for i in range(3):
        pokes_end.append(pokers.pop(i))
    print(f'第{j}位玩家的扑克牌是{pokes_end}')
    poker_all.append({j: pokes_end})
print(poker_all)


# #   每人抽到的牌存字典里，key是玩家序号
# # 如果是集合是不是就不用洗牌了
# for i in range(1, 6):
#     thepoke = random.sample(pokers, 3)
#     pokes_end.append({i, thepoke})

