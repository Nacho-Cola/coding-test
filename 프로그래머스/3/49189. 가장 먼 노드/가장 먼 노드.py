from collections import deque
def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    distance = [500001] * (n+1)
    for a,b in edge:
        graph[a].append(b)
        graph[b].append(a)
    
    que = deque([(1,1)])
    while que:
        node, dis = que.popleft()
        distance[node] = dis
        for n in graph[node]:
            if distance[n] > dis + 1:
                distance[n] =  dis + 1
                que.append((n,dis+1))
    
        
    return distance.count(max(distance[1:]))