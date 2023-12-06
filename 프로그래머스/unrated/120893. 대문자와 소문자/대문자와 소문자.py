def solution(my_string):
    a = ''
    for i in my_string:
        if  ord(i) > 90:
            i = i.upper()
        else:
            i = i.lower()
        a = a + i
    return a