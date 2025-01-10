import re

T = int(input())

pattern = re.compile(r'^(100+1+|01)+$')

for _ in range(T):
    signal = input().strip()
    if pattern.fullmatch(signal):
        print("YES")
    else:
        print("NO")
