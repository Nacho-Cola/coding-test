from itertools import product
def solution(users, emoticons):
    
    rates =product([10,20,30,40],repeat=len(emoticons))
    answer = []
    
    for rate in rates:
        total_membership = 0
        total_cost = 0
        for user_rate, user_bal in users:
            membership = 0
            sum_price = 0
            for r,price in zip(rate,emoticons):
                if r >= user_rate:
                    sum_price += price * (100-r)//100
                if sum_price >= user_bal:
                    membership += 1
                    break
            if membership:
                total_membership += 1
            else:
                total_cost += sum_price
            
        answer.append([total_membership,total_cost])
    
    return sorted(answer)[-1]