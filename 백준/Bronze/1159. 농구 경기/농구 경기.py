from collections import Counter

T = int(input())

names = Counter()
for _ in range(T) :
    names[list(input())[0]] += 1
    
result = ''
for name, cnt in sorted(names.items()):
    if cnt >=5 :
        result += name

if result :
    print(result)
else:
    print('PREDAJA')