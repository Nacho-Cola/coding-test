
def solution(lines):
    count = {}
    a = []
    answer = 0
    for i in lines:
        f = list(range(i[0], i[1]))
        a = a + f
    
    for val in a:
        if val in count:
            count[val] += 1
        else:
            count[val] = 1
    
    for num in count.values():
        if num > 1 :
            answer +=1
    return answer