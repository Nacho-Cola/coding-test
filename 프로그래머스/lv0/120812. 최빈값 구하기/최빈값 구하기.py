def solution(array):
    temp =set(array)
    answer=[]
    dic={}
    
    for j in temp :
        counts=array.count(j)
        answer.append(counts)
        dic[counts] = j
    answer=sorted(answer)
    if len(answer)==1:
        return dic[answer[0]]
    if answer[-1] ==answer[-2] :
        return -1
    return dic[answer[-1]]