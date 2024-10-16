from collections import deque
def solution(n, edge):
    answer = 0
    graph = [[]for _ in range(n+1)]
    visited = [0] * (n+1)
    visited[1] = 1
    dis = [1e9] * (n+1)
    dis[1]=1
    que = deque([1])
    
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    
    while que:
        node= que.popleft()
        for n in graph[node]:
            if visited[n] == 0:
                visited[n] = 1
                que.append((n))
                dis[n] = dis[node] + 1
    
    return dis.count(max(dis[1:]))