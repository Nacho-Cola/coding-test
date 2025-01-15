import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
dish = [list(map(int, input().split())) for _ in range(N)]

def melt_cheese():
    visited = [[0] * M for _ in range(N)]
    que = deque([(0, 0)])
    visited[0][0] = 1
    melt_positions = []  

    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    while que:
        y, x = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < M and 0 <= ny < N and not visited[ny][nx]:
                visited[ny][nx] = 1
                if dish[ny][nx] == 1:
                    melt_positions.append((ny, nx))
                elif dish[ny][nx] == 0:
                    que.append((ny, nx))

    for y, x in melt_positions:
        dish[y][x] = 0

    return len(melt_positions)

result = 0
last_melt_count = 0

while True:
    melt_count = melt_cheese()
    if melt_count == 0:
        break
    last_melt_count = melt_count
    result += 1

print(result)  
print(last_melt_count) 
