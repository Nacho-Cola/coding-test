def solution(s):
    corr = 0;
    for i in range(0,len(s)):
        stack =[]
        j = 0
        for bra in s:
            if bra == '[' or bra == '(' or bra =='{':
                stack.append(bra)
            if len(stack):
                if stack[-1] == '(' and bra == ')':stack.pop()
                elif stack[-1] == '{' and bra == '}':stack.pop()
                elif stack[-1] == '[' and bra == ']':stack.pop()
            else:
                j+=1
        if len(stack) == 0 and j!=len(s):
            corr+=1
        s = s + s[0]
        s = s[1:]
    return corr