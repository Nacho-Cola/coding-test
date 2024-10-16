from collections import Counter
def solution(participant, completion):
    participant = Counter(participant)
    completion = Counter(completion)
    for p in list(participant):
        if participant[p] != completion[p]:
            return p

        