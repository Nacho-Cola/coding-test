
def solution(clothes):
    H = {}   
    answer = 1
    for _,c in clothes:
        if c in H:
            H[c] += 1
        if c not in H:
            H[c] = 2
    for i in H.items():
        answer *= i[1]
        
    return answer - 1