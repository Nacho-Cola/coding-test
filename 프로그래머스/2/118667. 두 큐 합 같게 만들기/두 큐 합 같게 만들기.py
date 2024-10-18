from collections import deque
def solution(queue1, queue2):
    que1 = deque(queue1)
    que2 = deque(queue2)
    
    sum_que1 = sum(que1)
    sum_que2 = sum(que2)
    
    if (sum_que1 + sum_que2)%2:
        return -1
    
    count = 0
    while que1 and que2 and count < len(queue1)*4:
        if sum_que1 > sum_que2:
            a = que1.popleft()
            que2.append(a)
            sum_que1 -= a
            sum_que2 += a
        elif sum_que1 < sum_que2:
            a = que2.popleft()
            que1.append(a)
            sum_que2 -= a
            sum_que1 += a
        else:
            return count
        count += 1
    return -1