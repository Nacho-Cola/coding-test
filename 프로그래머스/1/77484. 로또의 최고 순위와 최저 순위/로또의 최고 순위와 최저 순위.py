from collections import Counter
def solution(lottos, win_nums):
    lottos = Counter(lottos)
    lottos_num = Counter([i for i in lottos if i])
    win_nums = Counter(win_nums)
    rank = [6,6,5,4,3,2,1]
    return rank[len(lottos_num&win_nums) + lottos[0]] ,rank[len(lottos_num&win_nums)]