def solution(arr1, arr2):
    arr2 = [list(raw) for raw in zip(*arr2)]
    answer = []
    for i in arr1:
        sub=[]
        for j in arr2:
            mul = 0
            for k in range(len(i)):
                mul += i[k] * j[k]
            sub.append(mul)
        answer.append(sub)
    return answer


