def closest_null(houses_on_street: list, n: int) -> list:
    result = [0] * len(houses_on_street)
    distance = float('inf')
    for index, value in enumerate(houses_on_street):
        if value == 0:
            result[index] = 0
            distance = 0
            for index_backwards in range(index, -1, -1):
                if distance <= result[index_backwards]:
                    result[index_backwards] = distance
                    distance += 1
                else:
                    break
            distance = 0
        else:
            distance += 1
            result[index] = distance
    return result

if __name__ == '__main__':
    n = int(input())
    houses_on_street = [int(num) for num in input().split(' ')]
    print(*closest_null(houses_on_street, n))