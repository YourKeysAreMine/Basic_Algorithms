def bracket_generator(n, prefix, left=0, right=0):
    if left == n and right == n:
        print(prefix)
    else:
        if left < n:
            bracket_generator(n, prefix + '(', left + 1, right)
        if right < left:
            bracket_generator(n, prefix + ')', left, right + 1)


if __name__ == '__main__':
    n = int(input())
    prefix = ''
    bracket_generator(n, prefix)
