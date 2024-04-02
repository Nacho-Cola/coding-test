import sys
input = sys.stdin.readline

N = int(input())
row = list(map(int, input().split())) 
count, result = 0, 0
row.sort()
for i in row:
    count += i
    result += count
print(result)