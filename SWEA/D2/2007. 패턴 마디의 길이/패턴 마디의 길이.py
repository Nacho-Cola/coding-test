T = int(input())
for test_case in range(1, T + 1):
	string = input()
	length = 0
	for i in range(10,0,-1):
		if string[0:i] == string[i:i+i]:
			length = i
	print(f'#{test_case} {length}')