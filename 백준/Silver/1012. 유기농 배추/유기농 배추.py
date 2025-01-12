import sys 
sys.setrecursionlimit(10000)

input = sys.stdin.readline

def dfs(farm, y, x, visited):
    visited[y][x] = 1
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        
        if 0<=nx<M and 0<=ny<N and visited[ny][nx]==0 and farm[ny][nx] == 1:
            dfs(farm, ny, nx, visited)

T = int(input())
for _ in range(T):
    N, M, C = map(int, input().split())
    farm = [[0] * M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    result = 0
    for _ in range(C):
        y, x = map(int, input().split())
        farm[y][x] = 1
    for i in range(N):
        for j in range(M):
            if visited[i][j] == 0 and farm[i][j] == 1:
                dfs(farm, i, j, visited)
                result += 1
    print(result)
    
