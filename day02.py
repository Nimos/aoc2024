from aoc import AocData

data = AocData(2)

def is_safe(level):
    dampened = False
    last = level[0]
    dir = "inc" if level[0] < level[1] else "dec"
    for idx in range(1, len(level)):
        x = level[idx]
        if dir == "inc" and last >= x or x - last > 3\
                or dir == "dec" and last <= x or last - x > 3:
            return False
        last = x
    return True


# brain won't work right rn so let's just do this the stupid way
def get_brute_permutations(level):
    return [
        level[:n] + level[n+1:] for n in range(0, len(level))
    ]

print(len([x for x in data.matrix(int) if any([is_safe(x) for x in get_brute_permutations(x)])]))

