from itertools import permutations
def solution(k, dungeons):
    answer = []
    for root in permutations(dungeons):
        count = 0 
        life = k
        for dungeon in root:
            if life < dungeon[0]:
                break
            if life >= dungeon[1]:
                life -= dungeon[1]
                count += 1
            else:
                break
        answer.append(count)
    return max(answer)