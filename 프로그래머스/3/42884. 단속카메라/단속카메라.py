def solution(routes):
    answer = 1
    routes = sorted(routes)
    car = routes[0]
    for i in routes[1:]:
        if car[1] >= i[0]:
            car = [car[0], min(car[1], i[1])]
        else:
            car = i
            answer += 1
    return answer 