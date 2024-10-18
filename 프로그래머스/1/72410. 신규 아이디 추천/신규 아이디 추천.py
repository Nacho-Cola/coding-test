import re
def solution(new_id):
    fil = re.compile(r'[a-z0-9\_\-\.]')
    new_id = ''.join(fil.findall(new_id.lower()))
    
    while '..' in new_id:
        new_id = new_id.replace('..', '.') 
        
    if len(new_id) > 0:
        if new_id[0] == '.':
            new_id = new_id[1:]
        
    if len(new_id) > 0:
        if new_id[-1] == '.':
            new_id = new_id[:-1]
    

    if len(new_id) == 0:
        new_id = 'a'
        

    if len(new_id) > 15:
        new_id = new_id[0:15] 
        if new_id[-1] == ".": 
            new_id = new_id[:-1]
    
    if len(new_id) <= 2:
        while True:
            if len(new_id) == 3:
                break
            else:
                last_a = new_id[-1]
                new_id = new_id + last_a
                
    answer = new_id
    return answer
