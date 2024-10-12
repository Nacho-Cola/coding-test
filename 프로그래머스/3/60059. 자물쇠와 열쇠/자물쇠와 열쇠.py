def rotate(key):
    return list(zip(*key[::-1]))
def check(arr,n,m):
    for i in range(m):
        for j in range(m):
            if arr[n+i][n+j]!=1:
                return False
    return True

def solution(key, lock):
    n = len(key)
    m = len(lock)
    board = [[0]*(2*n+m) for _ in range(2*n+m)]
    for i in range(m):
        for j in range(m):
            board[n+i][n+j] = lock[i][j]
    
    for _ in range(4):
        key = rotate(key)
        for i in range(1,n+m):
            for j in range(1,n+m):
                result = []
                for k in range(n):
                    for l in range(n):
                        board[i+k][j+l] += key[k][l] 
                        
                if check(board,n,m):
                    return True
                
                for k in range(n):
                    for l in range(n):
                        board[i+k][j+l] -= key[k][l] 
                
                        
    return False

