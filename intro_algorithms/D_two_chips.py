n = int(input())
arr = list(map(int, input().split()))
K = int(input())
def twosum(arr, K):
    for i in range(0, len(arr)):
            for j in range(i+1, len(arr)):
                if arr[i] + arr[j] == K:
                    return f'{arr[i]} {arr[j]}'
    return "None"

print(twosum(arr, K))