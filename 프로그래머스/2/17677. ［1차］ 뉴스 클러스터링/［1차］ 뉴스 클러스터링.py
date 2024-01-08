from collections import Counter

def get_pair(string):
    pair = []
    for i in range(len(string)-1): 
        if string[i].isalpha():
            if string[i+1].isalpha():
                pair.append(string[i]+string[i+1])
    return pair

def solution(str1, str2):
    answer = 1
    str1 = str1.upper()
    str2 = str2.upper()
    pair1 = get_pair(str1)
    pair2 = get_pair(str2)
    counter1 = Counter(pair1)
    counter2 = Counter(pair2)
    inter = list((counter1&counter2).elements())
    union = list((counter1|counter2).elements())
    
    if union:
        answer = len(inter) / len(union)
    return int(answer * 65536)
