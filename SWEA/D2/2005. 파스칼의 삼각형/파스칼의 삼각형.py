
T = int(input())
for test_case in range(1, T + 1):
    print(f'#{test_case}')
    N = int(input())
    arr = [ [0] * N for _ in range(N)]
    arr[0][0] = 1
    print(arr[0][0] , end='')
    for i in range(1,N):
        print()
        for j in range(N):
            if (arr[i-1][j] + arr[i-1][j-1]) == 0:
                break
            arr[i][j] = arr[i-1][j] + arr[i-1][j-1]
            print(arr[i][j],end=' ')
    print()
       	