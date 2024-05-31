from collections import Counter
def solution(lottos, win_nums):
    point = 0
    cnt = Counter(lottos)
    for i in lottos:
        if i in win_nums:
            point += 1
    tar = [6,6,5,4,3,2,1]
    return tar[cnt[0]+point], tar[point]