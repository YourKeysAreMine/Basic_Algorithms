n = int(input())
arr = list(map(int, input().split()))
K = int(input())
def twosum(arr, K):
    previous = set()
    for A in arr:
        Y = K - A
        if Y in previous:
            return f'{Y} {A}'
        else:
            previous.add(A)
    return 'None'

print(twosum(arr, K))