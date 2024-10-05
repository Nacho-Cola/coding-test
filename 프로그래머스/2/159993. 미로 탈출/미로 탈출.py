from collections import deque

def bfs(maps, start, end):
    visited = [[0] * len(maps[0]) for _ in range(len(maps))]
    que = deque([(*start, 0)])
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
    
    while que:
        x, y, count = que.popleft()
        
        if (x, y) == end:
            return count
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and visited[nx][ny] == 0:
                if maps[nx][ny] != 'X':
                    visited[nx][ny] = 1
                    que.append((nx, ny, count + 1))
    
    return -1

def solution(maps):
    s, l, e = None, None, None
    
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'S':
                s = (i, j)
            elif maps[i][j] == 'E':
                e = (i, j)
            elif maps[i][j] == 'L':
                l = (i, j)

    to_l = bfs(maps, s, l)
    to_e = bfs(maps, l, e)
    
    if to_l >= 0 and to_e >= 0:
        return to_l + to_e
    else:
        return -1
