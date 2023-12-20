def solution(elements):
    answer = []
    ss = elements.copy()
    for i in range(1,len(elements)+1):
        elements = ss + ss[:i]
        for j in range(len(elements)):
            answer.append(sum(elements[j:j+i]))
            if i == len(ss):
                break
    return len(set(answer))
