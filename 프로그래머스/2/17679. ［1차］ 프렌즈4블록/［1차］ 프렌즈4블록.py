from collections import Counter
def solution(m, n, board):
    for i in range(m):
        board[i] = list(board[i])
    idx = 1
    answer = 0
    x = [0, 0, 1, 1]
    y = [0, 1, 0, 1]
    

    while True:
        coor = []
        for ix in range(m-1):
            for iy in range(n-1):
                block = []
                for dx, dy in zip(x,y):
                    block.append(board[ix+dx][iy+dy])
                blocks = Counter(block)
                if len(list(blocks)) == 1:
                    for dx, dy in zip(x,y):
                        coor.append([ix+dx,iy+dy])
                        
        coor = set([tuple(i) for i in coor])
        
        if not coor:
            break
        answer += len(coor)     
        for nx, ny in coor:
            board[nx][ny] = 0
        temp = list(map(list,zip(*board)))
        for ls in temp:
            while 0 in ls:
                ls.remove(0)
            while len(ls) != m:
                ls.insert(0,idx)
                idx+=1
        board = list(map(list,zip(*temp)))

    return answer

 # CCBDE
 # AAADE
 # AAABE
 # CCBBF