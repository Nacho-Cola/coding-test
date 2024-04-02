import sys
input = sys.stdin.readline

N = int(input())
meeting = [list(map(int, input().split())) for _ in range(N)]

meeting.sort(key=lambda x: (x[1], x[0]))

result = 0 
meet_end = 0  

for start, end in meeting:
    if start >= meet_end:
        result += 1
        meet_end = end 
        
print(result)