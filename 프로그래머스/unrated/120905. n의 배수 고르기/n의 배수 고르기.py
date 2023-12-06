def solution(n, numlist):
    a=[]
    for i in numlist:
        if i%n == 0:
            a.append(i)
    return a