def solution(n, times):
    end = max(times)*n
    start = 1
    answer = 0
    while start <= end:
        mid = (start+end)//2
        total = 0
        for i in times:
            total += mid//i 
            if total > n:
                break
        if total >= n:
            end = mid-1
            answer = mid
        else:
            start = mid + 1
    return answer

