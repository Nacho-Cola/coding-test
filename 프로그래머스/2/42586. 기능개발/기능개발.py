def solution(progresses, speeds):
    que = []
    prev_p = 0
    for p,s in zip(progresses, speeds):
        print(prev_p)
        if (not que) or (prev_p < int((100-p)/s+0.9)):
            prev_p = int((100-p)/s+0.9)
            que.append(1)
        else:
            que[-1] += 1
    return que