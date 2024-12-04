from aoc import AocData

data = AocData(4)

matrix = data.matrix(split_at="")

WORD = "XMAS"

def check(x, y, n):
    # forgetting that negative indexing exists lead to the silliest debugging session
    if x < 0 or y < 0:
        return False
    try:
        return matrix[y][x] == WORD[n]
    except IndexError:
        return False

def check_left(x, y):
    return all([check(x - n, y, n) for n in range(0, len(WORD))])

def check_right(x, y):
    return all([check(x + n, y, n) for n in range(0, len(WORD))])

def check_up(x, y):
    return all([check(x, y - n, n) for n in range(0, len(WORD))])

def check_down(x, y):
    return all([check(x, y + n, n) for n in range(0, len(WORD))])

def check_dr(x, y):
    return all([check(x + n, y + n, n) for n in range(0, len(WORD))])

def check_ur(x, y):
    return all([check(x + n, y - n, n) for n in range(0, len(WORD))])

def check_dl(x, y):
    return all([check(x - n, y + n, n) for n in range(0, len(WORD))])

def check_ul(x, y):
    return all([check(x - n, y - n, n) for n in range(0, len(WORD))])


checks = [
    check_left, check_right, check_up, check_down, check_dr, check_ur, check_dl, check_ul
]

def check_words(x, y):
    return len([True for func in checks if func(x, y)])

def check_puzzle():
    res = 0
    for y, line in enumerate(matrix):
        for x, _ in enumerate(line):
           res += check_words(x, y)

    return res

print(check_puzzle())

def check_x(x, y):
    return sum([
        check_dr(x - 1, y - 1),
        check_dl(x + 1, y - 1),
        check_ur(x - 1, y + 1),
        check_ul(x + 1, y + 1),
    ]) == 2

# manipulate the global state yay
# change a pseudo-constant, double yay
WORD = "MAS"


def part_2():
    res = 0
    for y, line in enumerate(matrix):
        for x, _ in enumerate(line):
           res += check_x(x, y)

    return res

print(part_2())