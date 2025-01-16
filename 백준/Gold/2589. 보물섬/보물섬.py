from collections import deque

def bfs(start, grid, h, w):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = [[False] * w for _ in range(h)]
    queue = deque([(start[0], start[1], 0)])
    visited[start[0]][start[1]] = True
    max_distance = 0

    while queue:
        x, y, dist = queue.popleft()
        max_distance = max(max_distance, dist)
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and grid[nx][ny] == 'L':
                visited[nx][ny] = True
                queue.append((nx, ny, dist + 1))
    
    return max_distance


h, w = map(int, input().split())
grid = [input().strip() for _ in range(h)]
longest = 0
for i in range(h):
    for j in range(w):
        if grid[i][j] == 'L': 
            longest = max(longest, bfs((i, j), grid, h, w))

print(longest)
