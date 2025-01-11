from collections import Counter


fee = list(map(int, input().split()))
trucks = [list(map(int, input().split())) for _ in range(3)]

parking_time = Counter()
for start, end in trucks:
    for time in range(start, end):
        parking_time[time] += 1

result = 0
for count in parking_time.values():
    result += fee[count - 1] * count

print(result)