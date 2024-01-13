from collections import deque
def solution(n, roads, sources, destination):
    answer = []
    graph = [[] for _ in range(n+1)]
    distance = [-1] * (n+1)
    
    for start, end in roads:
        graph[start].append(end)
        graph[end].append(start)
    
    queue = deque([destination])
    distance[destination] = 0
    
    while queue:
        now = queue.popleft()
        for i in graph[now]:
            if distance[i] == -1:
                queue.append(i)
                distance[i] = distance[now] + 1
    
    for i in sources:
        answer.append(distance[i])
    return answer

    