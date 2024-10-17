def solution(numbers, hand):
    
    answer = ''
    L_hand = -2
    R_hand = -1
    
    mid_col = {2:[3,1,0,1,2,1,2,3,2,3,4,4], 
               5:[2,2,1,2,1,0,1,2,1,2,3,3],
               8:[1,3,2,3,2,1,2,1,0,1,2,2],
               0:[0,4,3,4,3,2,3,2,1,2,1,1]}
    
    for i in numbers:
        if i==1 or i==4 or i==7:
            answer += 'L'
            L_hand = i
        elif i==3 or i==6 or i==9:
            answer += 'R'
            R_hand = i
        else:
            if mid_col[i][L_hand] == mid_col[i][R_hand]:
                if hand[0] == 'r':
                    answer +='R'
                    R_hand = i
                else:
                    answer +='L'
                    L_hand = i
            elif mid_col[i][L_hand] > mid_col[i][R_hand]:
                answer +='R'
                R_hand = i
            else:
                answer += 'L'
                L_hand = i
    return answer