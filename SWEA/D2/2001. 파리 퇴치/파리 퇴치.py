T = int(input())
for test_case in range(1, T + 1):
    M, N = map(int, input().split())
    arr = []
    for _ in range(M):
        arr.append(list(map(int, input().split())))
    
    max_bugs = 0
    for i in range(M-N+1):
        for j in range(M-N+1):
            bugs = 0
            for k in range(N):
                for l in range(N):
                	bugs += arr[i+k][j+l]
            max_bugs = max(max_bugs, bugs)
    print(f'#{test_case} {max_bugs}')
                
       