def solution(dirs):
    
    way = set()
    x, y = 0, 0
    for i in list(dirs):
        new_x, new_y = x, y
        
        if i == "U" and y < 5:
            new_y += 1
        elif i == "D" and y > -5:
            new_y -= 1
        elif i == "L" and x > -5:
            new_x -= 1
        elif i == "R" and x < 5:
            new_x += 1
        else:
            continue  # 이동할 수 없는 경우는 무시
        
        way.add(((x, y), (new_x, new_y)))
        way.add(((new_x, new_y), (x, y)))
        
        x, y = new_x, new_y 
        
    return len(way)//2