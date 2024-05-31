from collections import Counter
def solution(lottos, win_nums):
    point = 0
    cnt = Counter(lottos)
    for i in lottos:
        if i in win_nums:
            point += 1
    tar = {0:6,1:6,2:5,3:4,4:3,5:2,6:1}
    return tar[cnt[0]+point], tar[point] if point else 6