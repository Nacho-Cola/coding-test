from collections import deque

def solution(s):
    
    answer = 0
    que = deque(s)
    
    while que:
        same = 0
        diff = 0
        
        x = que.popleft()
        if not que:
            answer += 1
            break
        que.appendleft(x)

        for _ in range(len(que)):
            n = que.popleft()
            if n == x:
                same += 1
            else:
                diff += 1
            
            if same == diff:
                answer += 1
                break
        if same != diff:
            answer += 1
    return answer