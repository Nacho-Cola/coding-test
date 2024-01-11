import math
def solution(n, stations, w):
    answer = 0
    s = 1
    for sta in stations:
        apt = sta - w
        total = apt - s
        if apt > 1 and total > 0 :
            answer += math.ceil(total/((2 * w) + 1))
        
        s = sta + w + 1
        
    if s <= n:
        total = (n + 1) - s
        answer += math.ceil(total / ((2 * w) + 1))
        
    return answer
