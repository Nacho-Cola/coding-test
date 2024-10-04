from itertools import combinations

def solution(relation):
    row_count = len(relation)
    col_count = len(relation[0])
    
    # 모든 가능한 속성 조합 생성
    all_combinations = []
    for i in range(1, col_count + 1):
        all_combinations.extend(combinations(range(col_count), i))
    
    # 유일성 체크
    unique_combinations = []
    for combo in all_combinations:
        temp = [tuple(item[i] for i in combo) for item in relation]
        if len(set(temp)) == row_count:
            unique_combinations.append(set(combo))
    
    # 최소성 체크
    candidate_keys = []
    for i in range(len(unique_combinations)):
        is_minimal = True
        for j in range(len(candidate_keys)):
            if candidate_keys[j].issubset(unique_combinations[i]):
                is_minimal = False
                break
        if is_minimal:
            candidate_keys.append(unique_combinations[i])
    
    return len(candidate_keys)