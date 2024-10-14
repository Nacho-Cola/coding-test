def rotate(maps, x1, y1, x2, y2):
    
    temp = maps[x1][y1]
    min_num = temp
    
    
    for i in range(x1+1,x2+1):
        maps[i-1][y1] = maps[i][y1]
        min_num = min(min_num,maps[i][y1])
    
    for i in range(y1+1,y2+1):
        maps[x2][i-1] = maps[x2][i]
        min_num = min(min_num,maps[x2][i])
    
    for i in range(x2-1,x1-1,-1):
        maps[i+1][y2] = maps[i][y2]
        min_num = min(min_num,maps[i][y2])
        
    for i in range(y2-1,y1-1,-1):
        maps[x1][i+1] = maps[x1][i]
        min_num = min(min_num,maps[x1][i])
        
    maps[x1][y1+1] = temp
    min_num = min(min_num,temp)
    
    return min_num
    

def solution(rows, columns, queries):
    answer = []
    maps = [[i for i in range(j,j+columns)] for j in range(1,rows*columns,columns)]
    
    for x1,y1,x2,y2 in queries:
        answer.append(rotate(maps, x1-1, y1-1, x2-1, y2-1))
    
    return answer