# https://www.hackerrank.com/challenges/python-string-split-and-join/problem


def split_and_join(line3):
    arr = line3.split(" ")
    line2 = "-".join(arr)

    return line2


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)