from collections import deque

def dfs(maps):
    result = 1e9
    visited = [[[1e8] * len(maps) for _ in range(len(maps))] for _ in range(4)]
    visited[0][0][0] = 0
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    que = deque([(0,0,0,0),(0,0,2,0)])
    while que:
        x,y,d,cost = que.popleft()
        for i in range(4):
            n_cost = 0
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<len(maps) and 0<=ny<len(maps) and maps[nx][ny] == 0:
                if d==i : n_cost = 100
                else : n_cost = 600
                
                new_cost = cost+n_cost

                if new_cost <= visited[d][nx][ny]:
                    visited[d][nx][ny] = new_cost
                    if nx==len(maps)-1 and ny==len(maps):
                        continue
                    que.append([nx,ny,i,new_cost])
                    
    for i in range(4):
        result = min(result, visited[i][-1][-1])
    return result

def solution(board):
    return dfs(board)