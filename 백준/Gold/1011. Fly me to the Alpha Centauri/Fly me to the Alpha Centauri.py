import math

T = int(input())
for _ in range(T):
    x, y = map(int, input().split())
    d = y - x  
    
    n = int(math.sqrt(d))  
    
    if d == n**2:
        print(2 * n - 1)
    elif n**2 < d <= n**2 + n:
        print(2 * n)
    else:
        print(2 * n + 1)