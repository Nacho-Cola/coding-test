import sys
input = sys.stdin.readline

T = int(input())
point = {'1': 0, '2': 0}
team_1 = 0
team_2 = 0
prev_time = 0

for _ in range(T):
    team, time = input().split()
    h, m = map(int, time.split(':'))
    time = h * 60 + m

    if point['1'] > point['2']:
        team_1 += time - prev_time
    elif point['2'] > point['1']:
        team_2 += time - prev_time
    prev_time = time

    point[team] += 1

end_time = 48 * 60
if point['1'] > point['2']:
    team_1 += end_time - prev_time
elif point['2'] > point['1']:
    team_2 += end_time - prev_time

print(f'{team_1 // 60:02}:{team_1 % 60:02}')
print(f'{team_2 // 60:02}:{team_2 % 60:02}')
