import sys 
input = sys.stdin.readline
sys.setrecursionlimit(10**5)


N, M, K = map(int, input().split())
maps = [[0] * M for _ in range(N)]
visited = [[0] * M for _ in range(N)]

def dfs(maps, y, x, visited):
    visited[y][x] = 1
    size = 1
    dx, dy = [0,0,-1,1], [1,-1,0,0]
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if 0<=nx<M and 0<=ny<N and not visited[ny][nx] and maps[ny][nx] == 0:
            size += dfs(maps, ny, nx, visited)
    return size
        

for i in range(K):
    sq = list(map(int,input().split()))
    sq[1] = N  - sq[1]
    sq[3] = N  - sq[3] 
    
    for i in range(sq[3], sq[1]):
        for j in range(sq[0], sq[2]):
            maps[i][j] = 1
areas = []
count = 0
for i in range(N):
    for j in range(M):
        if maps[i][j] == 0 and visited[i][j] == 0:
            areas.append(dfs(maps, i, j, visited))
            count += 1
            
print(count)
print(' '.join(map(str, sorted(areas))))