def solution(dots):
    arr = []
    for i in range(len(dots)):
        for j in range(len(dots)):
            if((dots[i][0] - dots[j][0]) != 0 ):
                if j>i:
                    arr.append((dots[i][1] - dots[j][1]) / (dots[i][0] - dots[j][0]))
                    
    return int((arr[0] - arr[5] == 0) or (arr[1] - arr[4] == 0) or (arr[2] - arr[3] == 0))
