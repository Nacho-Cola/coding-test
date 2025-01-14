import sys 

input = sys.stdin.readline

N, M = map(int, input().split()) 
J = int(input())
result = 0

apples = [int(input()) for _ in range(J)]
basket = range(1,M+1)


for apple in apples:
    if apple in basket:
        continue
    elif apple > basket[-1]:
        move = apple - basket[-1]
        result += move
        basket = range(apple - M + 1, apple+1)
    else :
        move = basket[0] - apple
        result += move
        basket = range(apple, apple + M)

print(result)