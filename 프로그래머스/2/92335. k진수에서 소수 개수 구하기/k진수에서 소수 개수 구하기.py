def solution(n, k):
    answer = 0
    temp = ''
    while n>0:
        temp += str(n%k)
        n = n // k
    temp = map(int,list(filter(None, temp[::-1].split('0'))))
    nums = [n for n in temp if n>1]
    
    count = 0
    for num in nums:
        for j in range(2,int(num**.5)+1):
                if not num % j:
                    count+=1
                    break
    
    return len(nums) - count


