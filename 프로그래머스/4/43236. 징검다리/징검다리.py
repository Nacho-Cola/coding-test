def solution(distance, rocks, n):
    rocks.sort()
    rocks.append(distance)
    end = distance
    start = 1
    while start <= end:
        mid = (end+start)//2
        cur_rock = 0
        del_rock = 0
        for rock in rocks:
            if rock - cur_rock >= mid:
                del_rock +=1
                cur_rock = rock
        if del_rock >= len(rocks)-n:
            start = mid + 1
        else:
            end = mid - 1
    return start - 1