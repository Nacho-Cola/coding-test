
def view_point(arr, i):
    if arr[i] - arr[i - 2] <= 0:
        return 0
    if arr[i] - arr[i -1] <= 0 :
        return 0
    if arr[i] - arr[i +1] <= 0 :
        return 0
    if arr[i] - arr[i + 2] <= 0 :
        return 0
    min_1 = arr[i] - arr[i - 2]
    min_2 = arr[i] - arr[i -1] 
    min_3 = arr[i] - arr[i +1]    
    min_4 =  arr[i] - arr[i + 2] 
    return min(min_1, min_2, min_3, min_4)

for test_case in range(1, 11):
    result = 0
    N = int(input())
    arr = [0, 0] + list(map(int, input().split())) + [0,0]
    result = 0
    for i in range(2,N):
        result += view_point(arr, i)
    print(f'#{test_case} {result}')