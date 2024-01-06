import numpy as np

def solution(friends, gifts):
    dic = {name: i for i, name in enumerate(friends)}
    table = [[0] * len(friends) for _ in range(len(friends)) ]
    presents = [0] * len(friends)

    for gift in gifts:
        i, j = gift.split(" ")
        table[dic[i]][dic[j]] += 1 
    
    array = np.array(table)
    giv_num = array.sum(axis=1)
    get_num = array.sum(axis=0)
    index = list(giv_num - get_num)
    
    for i in range(len(friends)):
        for j in range(i+1, len(friends)):
            if table[i][j] > table[j][i]: 
                presents[i] += 1
            elif table[j][i] > table[i][j]: 
                presents[j] += 1
            else: # 같으면
                if index[i] > index[j]:
                    presents[i] += 1
                if index[j] > index[i]:
                    presents[j] += 1
    
    return max(presents)