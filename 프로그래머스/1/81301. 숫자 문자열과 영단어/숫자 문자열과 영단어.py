def solution(s):
    answer = ''
    stack = ''
    
    dic = {'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4',
           'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}

    for i in s:
        if i.isdigit():
            answer += i
            stack = ''
        else:
            stack += i
            if stack in dic:
                answer += dic[stack]
                stack = ''
    return int(answer)