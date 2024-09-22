from collections import deque
def solution(x, y, n):
    answer = 0
    que = deque([(x,0)])
    visited = set([x])
    while que:
        dx, count = que.popleft()
        if dx == y:
            return count
        dx1, dx2, dx3 = dx+n, dx*2, dx*3

        if dx1 <= y and dx1 not in visited:
            visited.add(dx1)
            que.append((dx1,count+1))
        if dx2 <= y and dx2 not in visited:
            visited.add(dx2)
            que.append((dx2,count+1))
        if dx3 <= y and dx3 not in visited:
            visited.add(dx3)
            que.append((dx3,count+1))
        
    return -1

