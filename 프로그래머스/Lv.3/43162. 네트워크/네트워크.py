def bfs(computer, v, visited):
    visited[v] = True
    for w in range(len(computer[0])):
        if computer[v][w] == 1 and not visited[w]:
            bfs(computer, w, visited)
    

def solution(n, computers):
    answer = 0
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            answer+=1
            bfs(computers, i, visited)
    return answer