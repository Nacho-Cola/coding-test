def solution(n, s):
    if n > s:
        return [-1]
    mod = s % n
    answer = [s//n] * n
    
    if mod == 0:
        return answer
        
    else :
        for i in range(mod):
            answer[i] += 1
    return sorted(answer)