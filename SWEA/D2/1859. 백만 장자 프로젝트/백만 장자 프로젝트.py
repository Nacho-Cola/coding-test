T = int(input())
for test_case in range(1, T + 1):
	N = int(input())
	lst = list(map(int, input().split()))
	
	value = 0
	M = lst[-1]
	for i, num in enumerate(lst[::-1]):
		if M >= num:
			value = M - num + value
		else:
			M = num
	print(f'#{test_case} {value}')