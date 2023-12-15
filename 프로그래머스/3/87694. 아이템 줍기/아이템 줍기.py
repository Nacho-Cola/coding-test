from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    maps = [[-1]*102 for i in range(102)]
    for cor in rectangle:
        x1, y1, x2, y2 = map(lambda x : x*2, cor)
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                if x1 < x < x2 and y1 < y < y2:
                    maps[x][y] = 0
                elif maps[x][y] != 0:
                    maps[x][y] = 1

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    queue = deque([(characterX*2,characterY*2)])
    while queue:
        x, y = queue.popleft()
        if x == (itemX*2) and y == (itemY*2):
                return maps[x][y]//2
            
        for n in range(4):
            nx, ny = x + dx[n], y + dy[n]
            if 0<=nx<102 and 0<=ny<102:
                if maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y]+1
                    queue.append((nx, ny))
    return 0