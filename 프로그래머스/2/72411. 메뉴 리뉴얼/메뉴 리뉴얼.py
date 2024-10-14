from itertools import combinations
from collections import Counter
def solution(orders, course):
    
    answer = []
    for k in course:
        com = []
        for order in orders:
            for set_menu in combinations(order,k):
                set_menu = ''.join(sorted(set_menu))
                com.append(set_menu)
        com = Counter(com).most_common()
        answer += [menu for menu, cnt in com if cnt > 1 and cnt == com[0][1]]
    return sorted(answer)