
def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        chars = ''
        for i in skill_tree:
            if i in list(skill):
                chars += i
        if skill[:len(chars)] == chars:
            answer += 1
        
    return answer