import random


def poks():
    """
    生成一副扑克牌
    :return pokes: 一副扑克牌
    :rtype pokes: list
    """
    po = [[2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], ['J', 11], ['Q', 12],
          ['K', 13], ['A', 14]]
    huase = ['红桃', '黑桃', '方块', '梅花']
    pokes = []
    for i in huase:
        for j in po:
            pokes.append([i + str(j[0]), j[1]])

    return pokes


pokes = poks()


def pok_shuff():
    """
    洗牌
    :param pokes: 一副扑克牌
    :type pokes: list
    :return pokes: 洗好的扑克牌
    :rtype pokes: list
    """
    pokes1 = poks()
    random.shuffle(pokes1)
    return pokes1


def poker():
    """
    发牌
    :param pokes: 洗好的扑克牌
    :type pokes: list
    :return pokes_end: 发好的牌
    :rtype pokes_end: list
    """
    pokes2 = pok_shuff()
    pok1 = []
    pok2 = []
    for pokq in pokes2:
        pok1.append(pokq[0])
        pok2.append(pokq[1])
    pokeall = []
    pokes_end = []
    pokes_datall = []

    for i in range(1, 6):
        pokes_end = pok1[3 * (i - 1):3 * i]
        print(f'第{i}位玩家的扑克牌是{pokes_end}')
        pokeall.append({i: pokes_end})
        pokes_datall.append(pok2[3 * (i - 1):3 * i])
    thedata = []
    for numall in pokes_datall:
        numall.sort()
        thedata.append(numall[0]*100 + numall[1]*10 + numall[2])
    return pokes_end, pokeall, thedata


print(poker()[2])
