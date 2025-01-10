from itertools import combinations

tall = []
for _ in range(9):
    tall.append(int(input()))

target = sum(tall) - 100

for i in combinations(tall, 2):
    if sum(i) == target:
        tall.remove(i[0])
        tall.remove(i[1])
        break
for i in sorted(tall):
    print(i)