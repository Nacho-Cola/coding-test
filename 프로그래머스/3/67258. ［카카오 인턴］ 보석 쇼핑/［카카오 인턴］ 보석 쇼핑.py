from collections import defaultdict, Counter

def solution(gems):
    gem_count = Counter(gems)
    total_unique = len(gem_count)
    
    left = 0
    right = 0
    current_count = defaultdict(int)
    min_length = float('inf')
    result = []

    while right < len(gems):
        current_count[gems[right]] += 1
        right += 1
        
        while len(current_count) == total_unique:
            if right - left < min_length:
                min_length = right - left
                result = [left + 1, right]  
            
            current_count[gems[left]] -= 1
            if current_count[gems[left]] == 0:
                del current_count[gems[left]]
            left += 1

    return result
