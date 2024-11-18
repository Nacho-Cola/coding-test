def solution(sticker):
    if len(sticker) == 1:
        return sticker[0]
    
    pick_f = [0] + sticker[:-1]
    pick_s = [0] + sticker[1:]
    
    for i in range(2, len(pick_f)):
        pick_f[i] = max(pick_f[i-1], pick_f[i-2] + pick_f[i])
        pick_s[i] = max(pick_s[i-1], pick_s[i-2] + pick_s[i])
        
    return max(pick_f[-1], pick_s[-1])