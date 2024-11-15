
def sam_yook_goo(N):
    count = 0
    sN = str(N)
    for s in sN:
        if s == '3' or s == '6' or s == '9':
            count += 1
    if len(sN) == count:
        return '-' * count
    elif count :
        return '-'
    else:
        return N

N = int(input())
for i in range(1,N+1):
    print(sam_yook_goo(i),end=' ')
	