import sys
input = sys.stdin.readline

T = int(input().strip())
for _ in range(T):
    n = int(input().strip())
    closet = {}
    for _ in range(n):
        clothes = input().split()
        category = clothes[1]
        
        if category in closet:
            closet[category] += 1
        else:
            closet[category] = 1
    
    result = 1
    for count in closet.values():
        result *= (count + 1) 
    
    print(result - 1)
