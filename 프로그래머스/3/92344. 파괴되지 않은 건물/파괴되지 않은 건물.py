

def solution(board, skills):
    n = len(board)
    m = len(board[0])
    answer = 0
    effect = [[0]*(m+1) for _ in range(n+1)]
    
    for typ, r1, c1, r2, c2, degree in skills:
        effect[r1][c1] += degree if typ==2 else -degree
        effect[r1][c2+1] -= degree if typ==2 else -degree 
        effect[r2+1][c1] -= degree if typ==2 else -degree
        effect[r2+1][c2+1] += degree if typ==2 else -degree
        
    
    for i in range(n):
        for j in range(m):
            effect[i+1][j] += effect[i][j]
            
    for i in range(n):
        for j in range(m):
            effect[i][j+1] += effect[i][j]
            
    for i in range(n):
        for j in range(m):
            board[i][j] += effect[i][j]
            if board[i][j]>0:answer+=1
    
    return answer



    