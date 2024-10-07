from collections import deque

def solution(sequence):
    seq = [num * (-1)**(i%2) for i,num in enumerate(sequence)]
    
    for i in range(len(sequence)-1):
        seq[i+1] += seq[i]
        
    return max( abs(min(seq)), abs(max(seq)) ,max(seq)-min(seq))