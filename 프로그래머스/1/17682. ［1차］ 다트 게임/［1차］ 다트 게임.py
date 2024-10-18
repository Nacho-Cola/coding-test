import re
def solution(dartResult):
    answer = 0
    num = list(map(int,[i for i in re.split(r'[A-Z\*\#]',dartResult)if i]))
    option = [i for i in re.split(r'[0-9]',dartResult) if i]
    
    for i in range(2,-1,-1):
        if option[i][0] == 'D':
            num[i] = num[i]**2
        elif option[i][0] == 'T':
            num[i] = num[i]**3
        
    for i in range(2,-1,-1):
        if len(option[i]) == 2:
            if option[i][1] == '*':
                num[i] *= 2
                if i-1 > -1:
                    num[i-1] *=2
                
            if option[i][1] == '#':
                num[i] *= -1            
        
    return sum(num)