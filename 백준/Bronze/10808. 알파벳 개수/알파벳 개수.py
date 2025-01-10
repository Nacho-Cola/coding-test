alpha = [0] * 26

S = list(input())
for c in S:
    alpha[ord(c)-97] +=1
    
for i in alpha:
    print(i,end=' ')