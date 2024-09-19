from itertools import permutations

def solution(user_id, banned_id):
    len_ban = len(banned_id)  
    unique_combinations = set()  

    for u_ids in permutations(user_id, len_ban):
        ban_list = []
        for u_idx in range(len_ban):
            if len(u_ids[u_idx]) == len(banned_id[u_idx]):
                is_same = 1
                for i, j in zip(u_ids[u_idx], banned_id[u_idx]):
                    if j != '*' and i != j:
                        is_same = 0
                        break
                if is_same:
                    ban_list.append(u_ids[u_idx]) 

        if len(ban_list) == len_ban:  # 모든 금지된 ID에 대해 유효한 ID가 있어야 함
            unique_combinations.add(tuple(sorted(ban_list)))  
            
    return len(unique_combinations)