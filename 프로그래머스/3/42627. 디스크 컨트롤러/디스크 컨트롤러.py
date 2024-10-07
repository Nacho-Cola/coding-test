from heapq import heappush, heappop

def solution(jobs):
    answer = 0
    end_job = 0
    start, cur_time = -1, 0
    heap = []
    
    while end_job < len(jobs):
        for job in jobs:
            if start < job[0] <= cur_time:
                heappush(heap, [job[1],job[0]])
                
        if heap:
            cur_job = heappop(heap)
            start = cur_time
            cur_time += cur_job[0]
            answer += cur_time - cur_job[1]
            end_job += 1
        else:
            cur_time += 1
    
    return answer//len(jobs)