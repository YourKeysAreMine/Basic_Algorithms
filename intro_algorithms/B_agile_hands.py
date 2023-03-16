def agile_hands(n: int, numbers: list):
    result = 0
    already_checked = {}
    for value in test_list:
        if value not in already_checked:
            already_checked[value] = 1
        else:
            already_checked[value] += 1
    for value in already_checked.values():
        if value <= n*2:
            result += 1
    return result


if __name__ == '__main__':
    n = int(input())
    test_list = [y for x in
                 [list(map(str, input().strip())) for i in range(4)]
                 for y in x if y != '.']
    print(agile_hands(n, test_list))