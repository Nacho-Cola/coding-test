
#import sys
#sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
	A, B, N = list(map(int, input().split()))
	count = 1
	x, y = min(A, B), max(A, B)
	while x+y <= N:
		x, y = min(x, y), max(x, y)
		x +=y
		count +=1
	print(count)
    # ///////////////////////////////////////////////////////////////////////////////////
