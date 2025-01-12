import sys
input = sys.stdin.read

def find_min_length(n):
    number = 1
    length = 1
    while number % n != 0:
        number = (number * 10 + 1) % n
        length += 1
    return length

def main():
    data = input().strip().split()
    for line in data:
        n = int(line)
        print(find_min_length(n))

if __name__ == "__main__":
    main()
