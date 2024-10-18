from collections import defaultdict
def solution(msg):
    dic = { alpha:i for alpha, i in zip(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'),range(1,27))}
    msg = list(msg)
    answer = []
    idx = 27
    p1 = 0
    p2 = 1
    while p2 != len(msg)+1:
        if ''.join(msg[p1:p2]) in dic:
            p2+=1
        else:
            dic[''.join(msg[p1:p2])] = idx
            answer.append(dic[''.join(msg[p1:p2-1])])
            idx += 1
            p1 = p2-1
            
    answer.append(dic[''.join(msg[p1:p2-1])])
        
    
    return answer