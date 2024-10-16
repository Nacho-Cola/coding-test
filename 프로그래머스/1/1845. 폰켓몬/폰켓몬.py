def solution(nums):
    n = len(nums)//2
    poke = len(set(nums))
    if poke > n :
        return n
    return poke
