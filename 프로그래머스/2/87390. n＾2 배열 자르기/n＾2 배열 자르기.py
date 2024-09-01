def solution(n, left, right):
    
    row_s = left // n + 1
    col_s = left % n
    row_e = right // n + 1
    arr = []
    
    def make_arr(n, row):
        temp = list(range(1,n+1))
        for i,n in enumerate(temp):
            if n <= row:
                temp[i] = row
        return temp
    
    for i in range(row_s, row_e + 1):
        arr += make_arr(n,i)
        
        
    return arr[col_s:col_s+right - left+1]