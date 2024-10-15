def solution(strs, t):
    strs = set(strs)
    n = len(t)
    dp = [0] * (n+1)
    
    for i in range(1,n+1):
        dp[i] = float('inf')
        for j in range(1,6):
            if i - j < 0 :
                continue
            else:
                s = i - j
                if t[s:i] in strs:
                    dp[i] = min(dp[i], dp[i-j]+1)

    if dp[-1] == float('inf'):
        return -1
    return dp[-1] 