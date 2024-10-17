def solution(n, arr1, arr2):
    answer = []
    maps = []
    
    def cal(i):
        temp = 0
        num = ''
        while i:
            temp = i % 2
            i//=2
            num += str(temp)
        return num[::-1].zfill(n)
    
    for i,j in zip(arr1, arr2):
        line = ''
        a, b = cal(i), cal(j)
        for m in range(n):
            if a[m] == '1' or b[m] == '1':
                line += '#'
            else:
                line += ' '
        maps.append(line)
        
    return maps