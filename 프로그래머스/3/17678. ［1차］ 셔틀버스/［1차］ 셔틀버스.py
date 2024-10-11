def solution(n, t, m, timetable):
    pre = lambda x : list(map(int,x.split(':')))
    crew_time = sorted([pre(time)[0]*60 + pre(time)[1] for time in timetable])
    bus_time = [9*60 + t*i for i in range(n)]

    i = 0
    for tm in bus_time:
        cnt = 0   
        while cnt < m and i < len(crew_time) and crew_time[i] <= tm:
            i += 1
            cnt += 1
        if cnt < m : answer = tm
        else: answer = crew_time[i-1] - 1

    return str(answer//60).zfill(2) + ":" + str(answer%60).zfill(2)

