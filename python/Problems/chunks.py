# Print chunks of a list or string

l1 = [1, 2, 3, 4, 5, 6, 7]
# --> [1, 2], [3, 4], [5, 6]...

str1 = 'ABCDEFGHIJKLM'
# --> 'ABC', 'DEF', 'GHI'...


def print_chunks(list, step):
    result = []
    for i in range(0, len(list), step):
        result.append(list[i:step + i])

    return result


if __name__ == "__main__":

    print(print_chunks(l1, 2))
    print(print_chunks(str1, 3))
