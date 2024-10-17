
def traveler(graph,cost,sales,node):
    cost[node][0] = 0
    cost[node][1] = sales[node-1]
    
    if not graph[node]:
        return 
    
    extra_cost = float('inf')
    for child in graph[node]:
        traveler(graph,cost,sales,child)
        if cost[child][0] < cost[child][1]:
            cost[node][0] += cost[child][0]
            cost[node][1] += cost[child][0]
            extra_cost = min(extra_cost, cost[child][1] - cost[child][0])
        else:
            cost[node][0] += cost[child][1]
            cost[node][1] += cost[child][1]
            extra_cost = 0
    cost[node][0] += extra_cost
        
    
def solution(sales, links):
    N = len(sales)+1
    graph = [[] for _ in range(N)]
    cost = [[0,0] for _ in range(N)]
    for a,b in links:
        graph[a].append(b)
    traveler(graph,cost,sales,1)
    return min(cost[1])