answer_arr = [0,0]

def get_qd(len_arr, arr):
    if len_arr == 1:  
        answer_arr[arr[0][0]] += 1
        return
    
    sum_q = sum(sum(row) for row in arr) 
    total_elements = len_arr * len_arr
            
    if sum_q == total_elements:
        answer_arr[1] += 1
    elif sum_q == 0:
        answer_arr[0] += 1
    else:
        length = len_arr // 2
        get_qd(length, [row[:length] for row in arr[:length]])  
        get_qd(length, [row[length:] for row in arr[:length]])  
        get_qd(length, [row[:length] for row in arr[length:]])  
        get_qd(length, [row[length:] for row in arr[length:]])  


def solution(arr):
    global answer_arr
    answer_arr = [0, 0]  
    get_qd(len(arr), arr)

    return answer_arr