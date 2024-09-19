def solution(land):
    for idx in range(1,len(land)):
        for i in range(4):
            land[idx][i] += max(land[idx-1][:i]+land[idx-1][i+1:])
        

    return max(land[-1])