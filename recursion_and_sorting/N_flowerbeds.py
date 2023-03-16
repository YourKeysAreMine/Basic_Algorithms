def gardens(input_list):
    input_list.sort()
    newData = []
    start = input_list[0][0]
    end = input_list[0][1]
    for i in range(n-1):
        if end < input_list[i+1][0]:
            newData.append('{} {}'.format(start, end))
            start = input_list[i+1][0]
            end = input_list[i+1][1]
        elif input_list[i+1][1] > end:
            end = input_list[i+1][1]
    newData.append('{} {}'.format(start, end))
    return newData


if __name__ == '__main__':
    n = int(input())
    input_list = []
    for i in range(n):
        input_list.append(tuple([int(x) for x in input().split(' ')]))
    print('\n'.join(gardens(input_list)), end='')
