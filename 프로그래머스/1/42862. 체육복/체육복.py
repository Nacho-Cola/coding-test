def solution(n, lost, reserve):
    
    reserve = sorted(reserve)
    lost = sorted(lost)
    lost_copy = lost.copy() 
    
    for i in lost:
        print(i)
        if i in reserve:
            reserve.remove(i)
            lost_copy.remove(i)    
    bur = 0
    for i in lost_copy: 
        flag = 1
        
        if i-1 in reserve :
            bur += 1
            reserve.remove(i-1)
            flag = 0
            
        if i+1 in reserve and flag :
            bur += 1
            reserve.remove(i+1)
            
    return n - len(lost_copy) + bur
