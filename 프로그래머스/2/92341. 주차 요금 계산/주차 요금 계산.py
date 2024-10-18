import math
def solution(fees, records):
    dic = {}
    for record in records:
        cost = 0
        time, num, state = record.split()
        time = int(time[:2]) * 60 + int(time[3:])
        if not num in dic:
            dic[num] = {'time':time, 'extra':0, 'cost':0, 'state':state}
        else:
            if dic[num]['state'] == 'IN':
                dic[num]['extra'] += time - dic[num]['time'] 
                dic[num]['state'] = state
                dic[num]['time'] = time
            else:
                dic[num]['state'] = state
                dic[num]['time'] = time
            
                
    for cars in dic.items():
        if dic[cars[0]]['state'] == 'IN':
            dic[cars[0]]['extra'] += 23*60+59 - dic[cars[0]]['time'] 
        
        dt = dic[cars[0]]['extra']    
        if dt <= fees[0]: 
            dic[cars[0]]['cost'] = fees[1]
        else:
            extra = math.ceil((dic[cars[0]]['extra']-fees[0])/fees[2])
            dic[cars[0]]['cost'] = fees[1] + fees[3] * extra
    return [dic[i]['cost'] for i in sorted(list(dic))]