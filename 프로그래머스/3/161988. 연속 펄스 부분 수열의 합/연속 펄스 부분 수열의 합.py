from collections import deque

def solution(sequence):
    seq = [num * (-1)**(i%2) for i,num in enumerate(sequence)]
    seq.append(0)
    for i in range(len(sequence)-1):
        seq[i+1] += seq[i]
        
    return max(seq)-min(seq)