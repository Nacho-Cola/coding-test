from collections import Counter

def solution(s):
    tuples = Counter(list(map(int,s.replace('{', '').replace('}', '').split(','))))
    
    return list(zip(*tuples.most_common()))[0]