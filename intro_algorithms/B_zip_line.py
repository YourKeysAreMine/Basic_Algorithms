n = int(input())
arr_1 = list(map(int, input().split()))
arr_2 = list(map(int, input().split()))

result = []
for i in range(n):
    result.append(arr_1[i])
    result.append(arr_2[i])
print(*result)