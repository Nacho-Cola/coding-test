from heapq import heappop, heappush

def dijkstra(distance, graph):
    heap = []
    heappush(heap, [1,0])
    while heap:
        node, cost = heappop(heap)
        for n, c in graph[node]:
            if cost + c < distance[n]:
                distance[n] = cost + c
                heappush(heap, [n, cost+c])
    

def solution(N, road, K):
    distance = [500001]*(N+1)
    distance[1] = 0
    graph = [[] * (N+1) for _ in range(N+1)]
    
    for a, b, cost in road:
        graph[a].append((b,cost))
        graph[b].append((a,cost))
    
    dijkstra(distance,graph)
    
    return len([i for i in distance if i <= K])