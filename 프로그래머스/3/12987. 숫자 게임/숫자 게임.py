from heapq import heapify, heappop, heappush
def solution(A, B):
    answer = 0
    heapA = [-i for i in A]
    heapB = [-i for i in B]
    heapify(heapA)
    heapify(heapB)
    for i in range(len(A)):
        a,b = heappop(heapA),heappop(heapB)
        if a > b :
            answer += 1
        else:
            heappush(heapB, b)
    return answer

