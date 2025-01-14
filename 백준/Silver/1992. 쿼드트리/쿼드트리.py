def compress(x, y, size):
    first = matrix[x][y]
    for i in range(x, x + size):
        for j in range(y, y + size):
            if matrix[i][j] != first:
                half = size // 2
                return "(" + \
                       compress(x, y, half) + \
                       compress(x, y + half, half) + \
                       compress(x + half, y, half) + \
                       compress(x + half, y + half, half) + \
                       ")"
    return first

N = int(input())
matrix = [input().strip() for _ in range(N)]
print(compress(0, 0, N))
