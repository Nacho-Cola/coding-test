def solution(want, number, discount):
    answer = 0
    for i in range(len(discount)-9):
        corr = 0
        day_10 = []
        dic = {}
        for k in discount[i:10+i]:
            day_10.append(k)
            
        for name in day_10:
            if name in dic:
                dic[name] += 1
            else:
                dic[name] = 1
            
        for p, name in enumerate(want):
            if name in dic:
                if number[p] == dic[name]:
                    corr+=1
        answer += corr // len(want)
    return answer

