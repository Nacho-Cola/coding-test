import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
result  = 0
for _ in range(N):
    S = list(input().strip())
    stack = deque()
    for c in S:
        if stack:
            end = stack.pop()
            if end == c :
                continue
            else :
                stack.append(end)
                stack.append(c)
        else:
            stack.append(c)
    
    if not stack:
        result += 1
print(result)