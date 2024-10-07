from math import gcd

def check_card(n,arr):
    if n==1:
        return 0
    for a in arr:
        if a % n == 0:
            return 0
    return 1

def solution(arrayA, arrayB):
    answer = 0
    A, B = arrayA[0], arrayB[0]
    
    for i in range(1,len(arrayA)):
        A = gcd(A, arrayA[i])
        B = gcd(B, arrayB[i])
        
    A = A if check_card(A,arrayB) else 0
    B = B if check_card(B,arrayA) else 0
    
    return max(A,B)