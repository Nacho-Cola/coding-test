import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    count = 0
    while True:
        cur_min = heapq.heappop(scoville)
        if cur_min < K:
            nxt_min = heapq.heappop(scoville)
            heapq.heappush(scoville,cur_min + nxt_min *2)
        else:
            break
        if len(scoville)==1 and scoville[0]<K:
            return -1
        count += 1
    return count