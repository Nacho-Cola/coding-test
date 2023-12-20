def solution(name, yearning, photo):
    answer = []
    dic = dict(zip(name,yearning))
    for per in photo:
        point = 0
        for j in per:
            if j in name:
                point += dic[j]
        answer.append(point)
    return answer