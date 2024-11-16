def omok(arr,N): 
    for i in range(N):
        for j in range(N):
            if j + 4 < N:
                if arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i][j+3] + arr[i][j+4] == 'ooooo': # 가로
                    return 'YES'
            if j + 4 < N and i + 4 < N:
                if arr[i][j] + arr[i+1][j+1] + arr[i+2][j+2] + arr[i+3][j+3] + arr[i+4][j+4] == 'ooooo': # 우 대각
                    return 'YES'
            if i + 4 < N:
                if arr[i][j] + arr[i+1][j] + arr[i+2][j] + arr[i+3][j] + arr[i+4][j] == 'ooooo': #세로
                    return 'YES'
            if j - 4 < N and i + 4 < N:
                if arr[i][j] + arr[i+1][j-1] + arr[i+2][j-2] + arr[i+3][j-3] + arr[i+4][j-4] == 'ooooo': # 좌 대각
                    return 'YES'
    return 'NO'
            
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(list(input()))
    print(f'#{test_case} {omok(arr,N)}')


