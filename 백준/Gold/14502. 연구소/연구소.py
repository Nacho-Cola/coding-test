from itertools import combinations
from collections import deque
import copy

N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

empty = []
virus = []

for i in range(N):
    for j in range(M):
        if lab[i][j] == 0:
            empty.append((i, j))
        elif lab[i][j] == 2:
            virus.append((i, j))

def spread_virus(lab):
    queue = deque(virus)
    temp_lab = copy.deepcopy(lab)
    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and temp_lab[nx][ny] == 0:
                temp_lab[nx][ny] = 2
                queue.append((nx, ny))
    return temp_lab

def get_safe_area(lab):
    return sum(row.count(0) for row in lab)

max_safe_area = 0
for walls in combinations(empty, 3):
    for x, y in walls:
        lab[x][y] = 1
    spreaded_lab = spread_virus(lab)
    max_safe_area = max(max_safe_area, get_safe_area(spreaded_lab))
    for x, y in walls:
        lab[x][y] = 0

print(max_safe_area)
