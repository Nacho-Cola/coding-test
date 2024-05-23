from collections import Counter

def solution(N, stages):
    per_fault = { i:0 for i in range(1, N+1)}
    people = len(stages)
    stage = Counter(stages)
    
    for s, p in sorted(stage.items()):
        per_fault[s] = p / (people)
        people = people - p
        
    return [i for i,_ in sorted(per_fault.items(), reverse=True, key=lambda x : x[1]) if i<=N]