from collections import deque
def solution(begin, target, words):
    if target in words:
        queue = deque([(begin,0)])
        while queue:
            x, curr = queue.popleft()
            for i in words:
                count = 0
                for j in range(len(i)):
                    if x[j] != i[j]:
                        count +=1
                if count == 1:
                    if i == target:
                        return curr +1
                    queue.append((i, curr + 1));
                    words. remove(i)
                    
                    print(i)
    return 0