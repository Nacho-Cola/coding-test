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
        

for c in sorted(S):
    for _ in range(S[c]//2):
        print(c,end='')
print(even_w, end='')
for c in sorted(S)[::-1]:
    for _ in range(S[c]//2):
        print(c,end='')