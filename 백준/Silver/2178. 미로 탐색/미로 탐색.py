import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

maze = []
for _ in range(N):
    maze.append(list(map(int,list(input().strip()))))
visited = [[0]*M for _ in range(N)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

que = deque([(0,0,1)])
visited[0][0] = 1

while que:
    y, x, c = que.popleft()
    if y == N-1 and x == M-1 :
        print(c)
        exit()
    
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        
        if 0<=ny<N and 0<=nx<M and visited[ny][nx] == 0:
            if maze[ny][nx] == 1:
                visited[ny][nx] = 1
                que.append((ny,nx, c+1))
            
