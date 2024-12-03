from aoc import AocData
import re

data = AocData(3)
text = data.text().replace("\n", "")

def day03(text):
    matches = re.findall(r"mul\(([0-9]*),([0-9]*)\)", text)
    print(sum([int(a)*int(b) for a, b in matches]))

day03(text)
do_matches = re.findall(r"(^|do\(\))(.*?)(don't\(\)|$)", text)
text2 = "".join([match[1] for match in do_matches])
day03(text2)
