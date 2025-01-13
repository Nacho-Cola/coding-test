import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def dfs(maps, y, x, visited, h):
    visited[y][x] = 1
    dx=[0,0,1,-1]
    dy=[1,-1,0,0]
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        
        if 0<=nx<N and 0<=ny<N and not visited[ny][nx] and maps[ny][nx] > h:
            dfs(maps, ny, nx, visited, h)


N = int(input())
maps = [list(map(int, input().split())) for _ in range(N)]

result  = 1 
for h in range(1,101):
    visited = [[0]*N for _ in range(N)]
    peek = 0
    for i in range(N):
        for j in range(N):
            if maps[i][j] > h  and visited[i][j] == 0:
                dfs(maps, i, j, visited, h)
                peek += 1
    result = max(result, peek)
print(result)
    