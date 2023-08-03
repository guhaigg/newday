def generatePoker():
    """
    :param :
    :return: 生成完整地扑克牌
    """
    color = ['♥', '♠', '♣', '♦']
    size = [[2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], ['J', 11], ['Q', 12], ['K', 13],
            ['A', 14]]
    poker = []
    for poker_color in color:
        for poker_size in size:
            poker.append([f'{poker_color}{poker_size[0]}', poker_size[1]])
    return poker


# print(generatePoker())
def distributePoker(poker, peopleList):
    """
    :param poker: 一副不带王的完整地牌
    :param num:
    :param peopleList: 人名列表
    :return: 按照人数，每人发三张牌
    """
    import random
    p_cards = {}
    if len(peopleList) > 14:
        return '人数最多为14人'
    if len(peopleList) < 1:
        return '人数不符合规范'
    for name in peopleList:
        cards = random.sample(poker, 3)
        p_cards[name] = cards
        for Poker in cards:
            poker.remove(Poker)
    return p_cards


# print(distributePoker(generatePoker(), ['张三', '李四', '王五', '赵六', '田七', '王八', '刘九', '李十', '张十一', '张十二', '张十三', '张十四']))
def calculationSingle(p_cards, score):
    """
    计算单张牌点数大小
    :param p_cards: 一人三张牌
    :param score:   该人的分数
    :return:    score
    """
    card_val = [card[1] for card in p_cards]
    card_val.sort()
    score += card_val[2] * 10 + card_val[1] * 1 + card_val[0] * 0.1
    return score


# print(calculationSingle([['♥2', 2], ['♠2', 2], ['♣
def calculationDouble(p_cards, score):
    '''
    计算对子的点数大小
    :param p_cards:
    :param score:
    :return:
    '''
    card_val = [card[1] for card in p_cards]
    card_val.sort()
    if len(set(card_val)) == 2:
        score *= 100
    return score


def calculationAlong(p_cards, score):
    '''
    计算顺子的点数大小
    :param p_cards:
    :param score:
    :return:
    '''
    card_val = [card[1] for card in p_cards]
    card_val.sort()
    if card_val[0] + 1 == card_val[1] and card_val[1] + 1 == card_val[2]:
        score *= 1000
    return score


def calculationAlongSame(p_cards, score):
    '''
    计算同花顺的点数大小
    :param p_cards:
    :param score:
    :return:
    '''
    color_val = [card[0][0] for card in p_cards]
    if len(set(color_val)) == 1:
        card_val = [card[1] for card in p_cards]
        card_val.sort()
        if card_val[0] + 1 == card_val[1] and card_val[1] + 1 == card_val[2]:
            score *= 10000
    return score


def calculationPanther(p_cards, score):
    '''
    计算豹子的点数大小
    :param p_cards:
    :param score:
    :return:
    '''
    card_val = {card[1] for card in p_cards}
    if len(card_val) == 1:
        score *= 100000000
    return score


def main(customer, calculation_poker_func=None):
    '''
    :param customer:    玩家列表
    :param calculation_poker_func:  计算牌型的函数列表
    :return:
    '''
    if calculation_poker_func is None:
        calculation_poker_func = [
            calculationSingle,
            calculationDouble,
            calculationAlong,
            calculationAlongSame,
            calculationPanther
        ]
    poker = generatePoker()
    player_poker = distributePoker(poker=poker, peopleList=customer)
    player_score = []
    for name, cards in player_poker.items():
        score = 0
        for calc_func in calculation_poker_func:
            score = calc_func(p_cards=cards, score=score)
        player_score.append([name, score])
    player_score.sort(key=lambda player_score: player_score[1])
    winner = player_score[-1]
    winner_poker = []
    for poker in player_poker[winner[0]]:
        winner_poker.append(poker[0])
    print("玩家及所获取的牌如下：\n", player_poker)
    print(f'恭喜玩家 {winner[0]} 获得胜利,他的牌是{winner_poker},他的分数为：{winner[1]}分')


if __name__ == '__main__':
    '''  '''
    customer = ["王五", "李三", '国王', "丞相", "首辅"]
    main(customer=customer)
