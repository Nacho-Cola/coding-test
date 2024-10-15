from collections import deque

def check_crr(arr):
    stack = deque([])
    for i in arr:
        if i == '(':
            stack.append(i)
        else :
            if stack: 
                stack.pop()
            else: return 0
    return 0 if stack else 1

def solution(p):
    if not p: return ''
    opens = 0
    close = 0
    for i, b in enumerate(p):
        
        if b=='(': opens += 1
        else: close += 1
        
        if opens == close :
            if check_crr(p[:i+1]):
                return p[:i+1] + solution(p[i+1:])
            else:
                arr = list(p[:i+1])
                for j,_ in enumerate(arr):
                    if arr[j] == '(' : arr[j] = ')'
                    else :  arr[j] = '('
                    
                return '(' + solution(p[i+1:])  + ')' + ''.join([i for i in arr[1:i]])
            
        