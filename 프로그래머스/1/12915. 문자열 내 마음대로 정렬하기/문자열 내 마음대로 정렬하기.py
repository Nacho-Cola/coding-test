def solution(s, n):
    s =  sorted(s)
    s =  sorted(s, key = lambda s:s[n])
    return s