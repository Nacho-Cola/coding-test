def solution(phone_book):
    phone_book = sorted(phone_book)
    for i, ch in enumerate(phone_book[:-1]) :
        if ch == phone_book[i+1][:len(ch)]:
             return False
    return True