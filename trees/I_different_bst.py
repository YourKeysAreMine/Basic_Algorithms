def factorial(n):
    if n == 1:
        return 1
    else:
        return factorial(n-1) * n


if __name__ == '__main__':
    n = int(input())
    result = int(((factorial(2 * n))/(factorial(n) * factorial(n + 1))))
    print(result)
