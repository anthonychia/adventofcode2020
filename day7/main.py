import re


bagList = open('input.txt').read().replace('bags', '').replace('bag', '').split('\n')

bagDict = {bag.split('contain')[0].strip() : bag.split('contain')[1].replace('.', '').strip() for bag in bagList}

for key, value in bagDict.items():
    if 'no ' in value:
        bagDict[key] = None
    else:
        bagDict[key] = {color: int(n) for n, color in re.findall(r'([0-9]+) (\w+ \w+)', value)}

def find_bag_recursively(color):
    total = 0
    if isinstance(color, dict):
        allBags.update(color)
        for i, value in color.items():
            if isinstance(bagDict[i], int):
                total += value
            if isinstance(bagDict[i], dict):
                total += find_bag_recursively(bagDict[i])
        return total

def sum_bag(color):
    total=0
    for i, value in bagDict[color].items():
        total += value
        if isinstance(bagDict[i], dict):
            total += value*sum_bag(i)
    return total

# Part 1
checks = []
for outerBag, innerBags in bagDict.items():
    allBags={}
    find_bag_recursively(innerBags)
    checks.append('shiny gold' in allBags.keys())

print(sum(checks))

# Part 2
print(sum_bag('shiny gold'))

