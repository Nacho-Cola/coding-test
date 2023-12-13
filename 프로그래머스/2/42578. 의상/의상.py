def solution(clothes):
    dic = {}
    for ch in clothes:
        if ch[1] in dic:
            dic[ch[1]] += 1
        else:
            dic[ch[1]] = 1
            
    ls = dic.values()
    answer = 0
    sums = 0
    for i in ls:
        answer = (sums+1) * i
        sums += answer
        print(sums)
    return sums