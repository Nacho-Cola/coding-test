def solution(numbers):
    
    n = len(numbers)
    result = [-1] * n
    stack = [] 

    for i in range(n):
        while stack and numbers[stack[-1]] < numbers[i]:
            index = stack.pop() 
            result[index] = numbers[i]
        stack.append(i)
        
    return result