def solution(s):
    arr = [-1 for i in range(len(s))]
    for i in range(len(s)):
        for j, char in enumerate(s):
            if i<j:
                if s[i]==char :
                    arr[j] =  j - i 

    return arr