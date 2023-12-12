def solution(citations):
    answer = 0
    citations = sorted(citations)
    for i, time in enumerate(citations):
        if time >= len(citations) - i:
            answer+=1
    return answer