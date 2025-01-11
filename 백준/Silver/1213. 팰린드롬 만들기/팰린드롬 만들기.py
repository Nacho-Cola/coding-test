import sys
from collections import Counter
input = sys.stdin.readline

S = Counter(list(input().strip()))

even = 0
even_w = ''
for c,i in S.items():
    if i % 2:
        if even :
            print("I'm Sorry Hansoo")
            exit()
        even += 1
        even_w = c
        
result = ''
for c in sorted(S):
    for _ in range(S[c]//2):
        result += c
result =  result + even_w + result[::-1]
print(result)