def solution(cacheSize, cities):
    for i, ch in enumerate(cities):
        cities[i] = ch.upper()
        
    answer = 0
    ls = []
    
    for i in cities:
        if i in ls:
            answer +=1
            ls.remove(i)
            ls.append(i)
        else:
            answer +=5
            ls.append(i)
            if len(ls)>cacheSize:
                ls.pop(0)
            
    return answer