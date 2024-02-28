from collections import Counter
def solution(participant, completion):
    participant, completion = Counter(participant), Counter(completion)
    for i in participant:
        if participant[i] != completion[i]:
            return i