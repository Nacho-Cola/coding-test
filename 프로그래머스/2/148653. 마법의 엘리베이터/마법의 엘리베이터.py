def solution(storey):
    storey = list('0'+ str(storey))[::-1]
    count = 0
    for i in range(len(storey)-1):
        if int(storey[i]) > 5 or (int(storey[i]) == 5 and int(storey[i+1]) >= 5):
            count += 10 - int(storey[i])
            storey[i+1] = str(int(storey[i+1]) + 1)
        else:
            count += int(storey[i])

    return count + int(storey[-1])