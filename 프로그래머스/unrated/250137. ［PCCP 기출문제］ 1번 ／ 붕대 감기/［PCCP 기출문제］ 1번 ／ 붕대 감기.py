def solution(bandage, health, attacks):
    curr_hp = health
    stack = 0
    for i in range(attacks[-1][0]+1):
        
        if i == attacks[0][0]:
            curr_hp -= attacks[0][1]
            stack = 0
            attacks.pop(0)
            
        else:
            curr_hp += bandage[1]
            if stack == bandage[0] - 1:
                curr_hp += bandage[2]
                stack = -1
            stack +=1
        
        if curr_hp >= health:
            curr_hp = health
            
        if curr_hp < 1:
            curr_hp = -1
            break
            
    return curr_hp