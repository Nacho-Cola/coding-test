def solution(s):
    answer = []
    n = 0;
    for i in range(0,len(s)):
        answer =[]
        j = 0
        for bra in s:
            if bra == '[' or bra == '(' or bra =='{':
                answer.append(bra)
            if len(answer):
                if answer[-1] == '(' and bra == ')':
                    answer.pop()
                elif answer[-1] == '{' and bra == '}':
                    answer.pop()
                elif answer[-1] == '[' and bra == ']':
                    answer.pop()
            else:
                j+=1
        if len(answer) == 0 and j!=len(s):
            n+=1
        s = s + s[0]
        s = s[1:]
    return n