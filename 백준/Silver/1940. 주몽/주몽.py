import sys
input = sys.stdin.readline

N = int(input())
target = int(input())
numbers = sorted(map(int, input().split()))

left = 0
right = N - 1
result = 0

while left < right:
    current_sum = numbers[left] + numbers[right]
    if current_sum == target:
        result += 1
        left += 1
        right -= 1
    elif current_sum < target:
        left += 1
    else:
        right -= 1

print(result)
