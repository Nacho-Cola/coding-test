from heapq import heappush, heappop
def solution(n, works):
    answer = 0
    heap = []
    for num in works:
        heappush(heap, (-num, num))
    for _ in range(n):
        if heap[0][1] != 0:
            n = heappop(heap)[1] - 1
            heappush(heap, (-n, n))
    for i,n in heap:
        answer += n**2
    return answer