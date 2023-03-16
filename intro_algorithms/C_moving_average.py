n = int(input())
arr = list(map(int, input().split()))
K = int(input())
result = []
current_sum = sum(arr[0:K])
result.append(current_sum / K)
for i in range(0, len(arr) - K):
        current_sum -= arr[i]
        current_sum += arr[i+K]
        current_avg = current_sum / K
        result.append(current_avg)
print(*result)