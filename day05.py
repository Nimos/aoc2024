from collections import defaultdict
from functools import cmp_to_key
from aoc import AocData

data = AocData(5)

data = data.get_raw(small=False)

requirements, pages = data.split("\n\n")

requirements_dict = defaultdict(list)
for requirement in requirements.split("\n"):
    before, after = requirement.split("|")
    requirements_dict[before].append(after)
    
def check_page(page: list):
    for idx, num in enumerate(page):
        try:
            if any([x in page[:idx+1] for x in requirements_dict[num]]):
                return False
        except KeyError:
            pass
    return True

def get_middle(page: list):
    middle_idx = len(page)/2
    return int(page[int(middle_idx)])

res = 0
for page in pages.split("\n"):
    if not page:
        continue
    page = page.split(",")
    if page and check_page(page):
        res += get_middle(page)
        
print(res)

def cmp_page_num(num1, num2):
    try:
        if num1 in requirements_dict[num2]:
            return -1
        else:
            return 1
    except KeyError:
        return 0

def order_page(page):
    return sorted(page, key=cmp_to_key(cmp_page_num))
    
res = 0
for page in pages.split("\n"):
    if not page:
        continue
    page = page.split(",")
    if not check_page(page):
        page = order_page(page)
        res += get_middle(page)
    
print(res)