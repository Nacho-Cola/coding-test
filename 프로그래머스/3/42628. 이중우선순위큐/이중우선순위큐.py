def solution(operations):
    answer = []
    for command in operations:
        if command[0] == "I":
            answer.append(int(command[1:]))
        else:
            if answer:
                if command[2] == '1':
                    answer.remove(max(answer))
                else:
                    answer.remove(min(answer))
    print(answer)
    return [max(answer),min(answer)] if answer else [0,0]