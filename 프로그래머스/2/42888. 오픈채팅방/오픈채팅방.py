def solution(records):
    answer = []
    id_dic = {}
    for record in records:
        text = record.split()
        if text[0] == 'Enter':
            id_dic[text[1]]={'ms':text[0], 'name':text[2]}
        
        if text[0] == 'Change':
            id_dic[text[1]]['name'] = text[2]
            
    for record in records:
        text = record.split()
        if text[0] == 'Enter':
            answer.append(f"{id_dic[text[1]]['name']}님이 들어왔습니다.")
        if text[0] == 'Leave':
            answer.append(f"{id_dic[text[1]]['name']}님이 나갔습니다.")
    
    
    return answer