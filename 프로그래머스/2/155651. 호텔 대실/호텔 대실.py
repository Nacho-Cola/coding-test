def solution(book_time):
    answer = 0
    room = []
    for c_in, c_out in sorted(book_time, key=lambda x: x[0]):
        
        c_in, c_out = list(map(int,c_in.split(':'))), list(map(int,c_out.split(':')))
        c_in = c_in[0]*60 + c_in[1]
        c_out = c_out[0]*60 + c_out[1]
        
        
        need_new = True
        for i,out_time in enumerate(room):
            if c_in >= out_time:
                need_new = False
                room[i] = c_out + 10
                break
        if need_new:
            room.append(c_out + 10)
            
    return len(room)