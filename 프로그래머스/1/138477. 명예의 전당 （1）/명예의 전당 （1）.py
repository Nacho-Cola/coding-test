def solution(k, score):
    ls = []
    answer = []
    for i in score:
        if len(ls)<k:
            ls.append(i)
            answer.append(min(ls))
        else:
            if i > min(ls):
                ls.append(i)
                ls.remove(min(ls))
                answer.append(min(ls))
            else:
                answer.append(min(ls))
        
    return answer