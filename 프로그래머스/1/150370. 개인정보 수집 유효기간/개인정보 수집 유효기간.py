def com_day(td, dt):
    if dt[0] < td[0]: 
        return True
    elif dt[0] == td[0]:
        if dt[1] < td[1]:
            return True
        elif dt[1] == td[1]:
            if dt[2] <= td[2]:
                return True
    return False

def solution(today, terms, privacies):
    end_days = []
    answer = []
    terms = {i[0]: int(i[1:]) for i in terms}
    today = list(map(int, today.split('.')))

    for date in privacies:
        end_date = list(map(int, date[:-2].split('.')))
        day = terms[date[-1]]
        
        end_date[1] += day
        end_date[0] += end_date[1] // 12  
        end_date[1] = end_date[1] % 12 
        if end_date[1] == 0:
            end_date[1] = 12
            end_date[0] -= 1
        
        end_days.append(end_date)
    
    for i, dt in enumerate(end_days):
        if com_day(today, dt):
            answer.append(i + 1) 
    
    return answer
