from collections import Counter
def solution(a):
    
    answer = 0
    arr = Counter(a)
    for key in arr:
        if arr[key] <= answer: # 최대 값보다 작은 값은 스킵
            continue
        i = 0
        temp = 0
        
        while i < len(a) - 1:
            if (a[i] != key) and (a[i+1] != key): 
                i += 1  #가장 많은 수와 같은 숫자가 없음 -> 자리 수 이동
                continue
            if (a[i] == a[i + 1]):
                i += 1  #가장 많은 수 한쌍 부분수열 -> 자리 수 이동
                continue
            # 문제 없으면 2칸 이동
            temp += 1
            i += 2
        
        answer = max(answer,temp)
        
    return 0 if answer == -1 else answer * 2