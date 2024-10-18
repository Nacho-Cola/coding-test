def check_prime (num):
    if num == 1:
        return 0

    for p in range(2,int(num**0.5)+1):
        if not num % p:
            return 0
    return 1

def cal(n,k):
    if k == n:
        return n
    answer = -1
    num = ''
    while n:
        num += str(n % k)
        n //=k
    return num[::-1]

def solution(n, k): 
    result = 0
    prime = [2,3]
    num = cal(n,k)
    nums = [int(i) for i in num.split('0') if i]
    for i in nums:
        result += check_prime(i)
    return result