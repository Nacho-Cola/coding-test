def bfs(computers, v, visited):
    visited[v] = True
    for w in range(len(computers[0])):
        if computers[v][w] == 1 and not visited[w]:
            bfs(computers, w, visited)
        
        

def solution(n, computers):
    answer = 0
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            bfs(computers, i, visited)
            answer += 1
    return answer