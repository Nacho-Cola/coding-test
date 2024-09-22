def solution(order):
    answer = 0
    stack = []
    j = 0
    i = 0
    
    while i < len(order):
        
        if i+1 == order[j]:
            answer+=1
            j+=1
            i+=1
            
        elif stack and stack[-1]==order[j]:
            
            for k in stack[::-1]:
                if k == order[j]:
                    answer+=1
                    j+=1
                    stack.pop()
                else:
                    break
        else:
            stack.append(i+1)
            i+=1
        
    if stack and stack[-1]==order[j]:

        for k in stack[::-1]:
            if k == order[j]:
                answer+=1
                j+=1
                stack.pop()
            else:
                break
        
    return answer


# def solution(order):
#     answer = 0

#     stack = []
#     for idx, num in enumerate(order):
#         stack.append(idx+1)

#         while stack and stack[-1] == order[answer]:
#             stack.pop()
#             answer +=1

#     return answer
