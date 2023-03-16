NUMBERS = {
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z'],
}

class Solution:
    def combinations(self, digits):
        self.result = []       
        self.backtrack(digits, 0, [])
        return self.result

    def backtrack(self, digits, current_index, current_result):
        if current_index >= len(digits):
            self.result.append(''.join(current_result))
            return
        else:
            for char in NUMBERS[digits[current_index]]:
                current_result.append(char)
                self.backtrack(digits, current_index + 1, current_result)
                current_result.pop()

if __name__ == '__main__':
    numbers = input()
    object = Solution()
    print(*object.combinations(numbers))
