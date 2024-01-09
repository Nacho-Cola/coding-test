
def solution(msg):
    answer = []
    dic = {chr(i) : i-64 for i in range(65,91)}
    start, end = 0, 1
    msg = list(msg) + ["0"]
    print(msg)
    while end < len(msg):
        while ''.join(msg[start:end]) in dic:
            end+=1
        temp = ''.join(msg[start:end])
        dic[temp] = len(dic) + 1
        answer.append(dic[temp[:-1]])
        start , end = end - 1, end
    return answer