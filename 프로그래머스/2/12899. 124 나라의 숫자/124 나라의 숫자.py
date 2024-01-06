def solution(n):
    answer = ''
    num_ls = ['1', '2', '4']
    while n>0:
        n -= 1
        answer = num_ls[n%3] + answer
        n = n//3
    return answer
# 1  1
# 2  2
# 3  4
# 4  11
# 5  12
# 6  14
# 7  21
# 8  22
# 9  24
# 10 41
# 11 42
# 12 44
# 13 111


# 0 0 0
# 1 0 1
# 2 0 2
# 3 1 0
# 4 1 1
# 5 1 2
# 6 2 0

# 13 3 0