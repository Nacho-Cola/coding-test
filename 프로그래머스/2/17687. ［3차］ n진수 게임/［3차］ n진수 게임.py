num_lst = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
def solution(n, t, m, p):
    answer = ''
    
    tubes_num = [i*m+p for i in range(t)]
    
    def make_N_number(n, i):
        number = ''
        while i > 0:
            i, mod = divmod(i,n)
            number += str(num_lst[mod])
        return number[::-1]
    
    def make_N_list(n,tb_num):
        N_list = '0'
        i = 1
        while len(N_list) <= tb_num:
            N_list += make_N_number(n, i)
            i+=1
        return N_list
            
    N_lst = make_N_list(n,tubes_num[-1])
    for num in tubes_num:
        answer += N_lst[num-1]
    
    return answer
