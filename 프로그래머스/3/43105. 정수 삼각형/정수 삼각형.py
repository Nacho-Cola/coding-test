def solution(triangle):
    answer = 0
    n = len(triangle)+1
    dp = [[0] * n for i in range(n)]
    
    for i in range(1,n):
        for j in range(1,i+1):
            dp[i][j] = triangle[i-1][j-1]
    
    for i in range(1,n):
        for j in range(1,i+1):
            dp[i][j] += max(dp[i-1][j-1], dp[i-1][j])
    
    return max(dp[-1])