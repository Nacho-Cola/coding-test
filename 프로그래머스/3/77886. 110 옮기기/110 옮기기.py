
def solution(s):
    
    answer = []
    for st in s:
        stack = ''
        stack += st[:2]
        count_110 = 0
        for ch in st[2:] :
            stack += ch
            if stack[-3:] == '110':
                stack = stack[:-3]
                count_110+=1
                
        idx = stack.find("111")             
        if idx == -1:                      
            idx = stack.rfind('0')
            stack = stack[:idx+1]+"110"*count_110+stack[idx+1:]
        else:                               
            stack = stack[:idx]+"110"*count_110+stack[idx:]
        answer.append(stack)
        
            
    return answer