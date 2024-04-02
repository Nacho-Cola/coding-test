import sys
input = sys.stdin.readline

N, K = map(int,input().split())
coins = [int(input()) for i in range(N)]
result = 0

for i in coins[::-1]:
    result += K // i 
    K %= i
    
print(result)