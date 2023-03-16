n = input()

def is_correct_bracket_seq(sequense):
    result = True
    list = []
    for i in sequense:
        if i in '({[':
            list.append(i)
        elif i in ')}]':
            if len(list) == 0:
                result = False
                break
            if i == ')' and list.pop() == '(':
                continue
            if i == '}' and list.pop() == '{':
                continue
            if i == ']' and list.pop() == '[':
                continue
            else:
                result = False
                break
    if len(list) != 0:
        result = False
    return result

print(is_correct_bracket_seq(n))