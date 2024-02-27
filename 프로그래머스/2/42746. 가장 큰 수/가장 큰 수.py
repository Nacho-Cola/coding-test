
def solution(n):
    string = list(map(str,n))
    string.sort(key=lambda x:x*3, reverse=True)
    return str(int(''.join(string)))
