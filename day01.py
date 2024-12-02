from aoc import AocData

data = AocData(1)

left = []
right = []
for l in data.lines():
    left.append(int(l.split(" ")[0]))
    right.append(int(l.split(" ")[-1]))

left = sorted(left)
right = sorted(right)

res = sum([(left[x] - right[x]) if left[x] > right[x] else (right[x] - left[x]) for x in range(0, len(left))])

print(res)

res2 = sum(left[x] * len([n for n in right if n == left[x]]) for x in range(0, len(left)))

print(res2)