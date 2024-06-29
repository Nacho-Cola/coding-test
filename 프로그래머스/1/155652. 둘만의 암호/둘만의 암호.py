def solution(s, skip, index):
    answer = ''
    temp = list(range(index + 1))
    for alpha in s:
        for i in temp:
            char = chr(ord(alpha) + i)
            if ord(char) > ord('z'):
                char = chr((ord(char) - ord('a')) % 26 + ord('a'))
                print(char)
            if char in skip:
                temp.append(temp[-1]+1)
        
        answer += chr((ord(char) - ord('a')) % 26 + ord('a'))
        temp = list(range(index + 1))
            
    return answer

# abcbefghijklmnopqrstuvwxyz
