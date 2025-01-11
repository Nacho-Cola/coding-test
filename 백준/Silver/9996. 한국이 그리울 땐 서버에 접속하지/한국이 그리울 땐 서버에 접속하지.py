import re

N = int(input())
pattern = input().strip()
files = [input().strip() for _ in range(N)]

regex_pattern = '^' + pattern.replace('*', '.*') + '$'

for file in files:
    if re.match(regex_pattern, file):
        print("DA")
    else:
        print("NE")
