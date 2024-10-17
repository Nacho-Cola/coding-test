from heapq import heappop, heappush

def dijkstra(graph, distance):
    heap = []
    heappush(heap, (1,0))
    while heap:
        node, cost = heappop(heap)
        for n,c in graph[node]:
            if cost+c < distance[n]:
                distance[n] = cost+c
                heappush(heap,(n,cost+c))
            
            
    
def solution(N, road, K):
    answer = 0
    graph = [[] for _ in range(N+1)]
    distance = [500001] * (N+1)
    distance[1] = 0
    
    for a,b,cost in road:
        graph[a].append((b,cost))
        graph[b].append((a,cost))    
        
    dijkstra(graph,distance)
    return len([i for i in distance[1:] if i <= K])