# https://www.hackerrank.com/challenges/python-mutations/problem


def mutate_string(string, position, character):
    line = string[:position]
    line += character
    line += string[position+1:]
    return line


if __name__ == '__main__':

    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)