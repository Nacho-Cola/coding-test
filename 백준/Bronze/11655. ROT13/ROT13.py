rot = list(input())

for c in rot:
    if c.isalpha():
        asc = ord(c)
        if asc >= ord('a'):
            print(chr((asc - ord('a') + 13) % 26 + ord('a')), end='')
        else:
            print(chr((asc - ord('A') + 13) % 26 + ord('A')), end='')
    else:
        print(c,end='')