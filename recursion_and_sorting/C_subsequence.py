def subsequence(short_string, full_string):
    position = -1
    for value in short_string:
        try:
            position = full_string.index(value, position + 1)
        except ValueError:
            return False
    return True


if __name__ == '__main__':
    short_string = input()
    full_string = input()
    print(subsequence(short_string, full_string))
