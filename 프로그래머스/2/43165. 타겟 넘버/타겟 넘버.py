def solution(numbers, target):

    def cal(idx, total):
        nonlocal answer

        if idx == len(numbers):
            if total == target:
                answer += 1
            return

        cal(idx+1, total + numbers[idx])
        cal(idx+1, total - numbers[idx])

    answer = 0
    cal(0, 0)

    return answer