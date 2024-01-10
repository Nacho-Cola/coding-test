def solution(nums):
    num_list = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                num_list.append(nums[i] + nums[j] + nums[k])
    answer = num_list.copy()
    for num in num_list:
        for o in range(2,num):
            if num % o == 0 :
                answer.remove(num)
                break

    return len(answer)