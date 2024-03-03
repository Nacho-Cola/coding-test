def solution(m, n, puddles):
    table = [[0]*(m+1) for _ in range(n+1)]
    
    for i,j in puddles:
        table[j][i] = 1
    
    table[0][1] = 1
    
    for i in range(1,n+1):
         for j in range(1,m+1):
            if table[i][j]:
                table[i][j] = 0
            else:
                table[i][j] = (table[i-1][j] + table[i][j-1]) % 1000000007
    return table[-1][-1]