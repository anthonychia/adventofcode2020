groups = [[set(person) for person in line.split('\n')] for line in open('input.txt').read().split('\n\n')]

# Part 1
print(sum(len(set.union(*group)) for group in groups))

# Part 2
print(sum(len(set.intersection(*group)) for group in groups))
