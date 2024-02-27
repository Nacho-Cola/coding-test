def solution(answers):
    answer = []
    num1 = [1,2,3,4,5]
    num2 = [2,1,2,3,2,4,2,5]
    num3 = [3,3,1,1,2,2,4,4,5,5]
    cor= [0 , 0 , 0]
    for i in answers:
        if i == num1[0]:
            cor[0]+=1
        if i == num2[0]:
            cor[1]+=1
        if i == num3[0]:
            cor[2]+=1
        num1 = num1[1:]+[num1[0]]
        num2 = num2[1:]+[num2[0]]
        num3 = num3[1:]+[num3[0]]
    
    return [i + 1 for i, v in enumerate(cor) if v == max(cor)]