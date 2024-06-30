def solution(word):
    vowels = ['A', 'E', 'I', 'O', 'U']
    weights = [781, 156, 31, 6, 1] 
    
    result = 0
    for i, char in enumerate(word):
        index = vowels.index(char)
        result += index * weights[i] + 1
    
    return result

