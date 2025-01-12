def modul(a, b, c):
    if b == 0:
        return 1
    elif b == 1:
        return a % c
    else:
        temp = modul(a, b // 2, c)
        temp = (temp * temp) % c
        if b % 2 == 0:
            return temp
        else:
            return (temp * a) % c

A, B, C = map(int, input().split())
print(modul(A, B, C))
