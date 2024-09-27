from collections import Counter
def solution(friends, gifts):
    
    dic_give = {i:0 for i in friends}
    dic_gaved = {i:0 for i in friends}
    gift_num = {i:0 for i in friends}
    gifts_friends = {i:[] for i in friends}
    answer = {i:0 for i in friends}
    
    for i in gifts:
        A, B = i.split()
        dic_give[A] += 1
        dic_gaved[B] += 1
        gifts_friends[A].append(B)
        
    for i in friends:
        gift_num[i] = dic_give[i] - dic_gaved[i]
        gifts_friends[i] = Counter(gifts_friends[i])
        for j in friends:
            if j not in gifts_friends[i]:
                gifts_friends[i][j] = 0
        
    for i in friends:
        for j,count in gifts_friends[i].items():
            
            if count > gifts_friends[j][i]:
                answer[i] += 1
                
            elif count == gifts_friends[j][i]:
                if gift_num[i] > gift_num[j]:
                    answer[i] += 1
        
            
    
    return max(answer.values())