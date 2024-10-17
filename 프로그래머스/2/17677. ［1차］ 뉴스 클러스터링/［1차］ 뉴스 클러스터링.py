import re
from collections import Counter
def solution(str1, str2):
    answer = 0
    inter = 0
    union = 0
    str1, str2 = str1.upper() , str2.upper()
    set_A = Counter([str1[i]+str1[i+1] for i in range(len(str1)-1) if (str1[i]+str1[i+1]).isalpha() ])
    set_B = Counter([str2[i]+str2[i+1] for i in range(len(str2)-1)if (str2[i]+str2[i+1]).isalpha() ])
    
    inter_elements = list(set_A & set_B)  # 교집합
    union_elements = list(set_A | set_B)  # 합집합
    
    for i in inter_elements:
        inter += min(set_A[i], set_B[i]) 
    for i in union_elements:
        union += max(set_A[i], set_B[i])
        
    return int(inter/union * 65536) if inter or union else 65536