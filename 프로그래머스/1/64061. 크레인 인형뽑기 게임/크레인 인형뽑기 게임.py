def solution(board, moves):
    answer = 0
    str_board =[ [] for i in range(len(board)) ]
    stack = []
    
    for idx, i in enumerate(zip(*board)):
        for j in i[::-1]:
            if j!=0:
                str_board[idx].append(j)
                
    
    for i in moves:
        if str_board[i-1]:
            k_frends = str_board[i-1].pop()
            if stack and stack[-1] == k_frends:
                stack.pop()
                answer += 2
            else:
                stack.append(k_frends)
        
    print(str_board)    
    print(stack)
    
    return answer
    