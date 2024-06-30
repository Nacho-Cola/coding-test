def solution(topping):
    from collections import Counter

    total_count = Counter(topping)    
    left_types = set()
    left_count = Counter()
    
    num_ways = 0
    
    for i in range(len(topping) - 1):
        left_count[topping[i]] += 1
        left_types.add(topping[i])
        
        total_count[topping[i]] -= 1
        if total_count[topping[i]] == 0:
            del total_count[topping[i]]
        
        if len(left_types) == len(total_count):
            num_ways += 1
    
    return num_ways
