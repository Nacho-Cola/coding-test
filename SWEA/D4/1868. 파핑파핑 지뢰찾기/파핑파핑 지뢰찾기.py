T = int(input())

for test_case in range(1, T + 1):
    result = 0 
    N = int(input())
    mine_map = []
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    
    for _ in range(N):
        mine_map.append(list(input()))

    for n in range(N):
        for m in range(N):
            if mine_map[n][m] == '.':
                mine_count = 0
                for dx, dy in directions:
                    nx, ny = n + dx, m + dy
                    if 0 <= nx < N and 0 <= ny < N and mine_map[nx][ny] == '*':
                        mine_count += 1
                mine_map[n][m] = str(mine_count)


    visited = [[False] * N for _ in range(N)]

    def dfs(x, y):
        stack = [(x, y)]
        while stack:
            cx, cy = stack.pop()
            if visited[cx][cy]:
                continue
            visited[cx][cy] = True
            if mine_map[cx][cy] == '0':  
                for dx, dy in directions:
                    nx, ny = cx + dx, cy + dy
                    if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and mine_map[nx][ny] != '*':
                        stack.append((nx, ny))

    for n in range(N):
        for m in range(N):
            if mine_map[n][m] == '0' and not visited[n][m]:
                dfs(n, m)  
                result += 1

    for n in range(N):
        for m in range(N):
            if mine_map[n][m] != '*' and not visited[n][m]:
                result += 1

    print(f"#{test_case} {result}")
