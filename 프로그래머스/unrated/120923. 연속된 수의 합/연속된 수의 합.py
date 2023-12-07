def solution(num, total):
    answer=[]
    mid = total/num
    if(mid*10%10) == 0 :
        answer = list(range(int(mid-num//2), int(mid+num//2+1)))
    elif num <= total:
        answer = list(range(int(mid-num//2)+1, int(mid+num//2+1)))
    else:
        answer = list(range(int(mid-num//2), int(mid+num//2+1)))
        
    return answer