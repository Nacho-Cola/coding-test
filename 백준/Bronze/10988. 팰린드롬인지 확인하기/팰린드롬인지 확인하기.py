S = list(input())

n = len(S)

if n % 2 :
    for i in range(n//2):
        if S[i] != S[-(i+1)]:
            print(0)
            exit()
else :
    for i in range(n//2):
        if S[i] != S[-(i+1)]:
            print(0)
            exit()

print(1)