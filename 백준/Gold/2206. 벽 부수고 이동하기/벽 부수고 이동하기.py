from collections import deque

N, M = map(int, input().split())
grid = [list(input().strip()) for _ in range(N)]
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]

dy = [0, 0, 1, -1]
dx = [-1, 1, 0, 0]

que = deque([(0, 0, 0, 1)]) 
visited[0][0][0] = 1

while que:
    y, x, wall, dist = que.popleft()

    if y == N - 1 and x == M - 1:
        print(dist)
        exit()

    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < N and 0 <= nx < M:

            if grid[ny][nx] == '0' and not visited[ny][nx][wall]:
                visited[ny][nx][wall] = 1
                que.append((ny, nx, wall, dist + 1))

            elif grid[ny][nx] == '1' and wall == 0 and not visited[ny][nx][1]:
                visited[ny][nx][1] = 1
                que.append((ny, nx, 1, dist + 1))

print(-1)
