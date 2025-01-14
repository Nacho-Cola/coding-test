import sys
from collections import Counter
input = sys.stdin.readline

N, C = map(int, input().split())
password = sorted(Counter(list(input().split())).items(),key=lambda x:-x[1])

for n, v in password:
    print((n+' ')*v, end= "")