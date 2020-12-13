import numpy as np
from itertools import combinations

preamble = 25

data = np.asarray([int(line) for line in open('input.txt').read().split('\n')])

# Part 1
for i in range(preamble+1, len(data)):
    previous_list = data[i-preamble:i]
    possible_sum = [sum(pairs) for pairs in combinations(previous_list, 2)]
    # check next number is sum of any previous 2 numbers
    next_number = data[i]
    if next_number not in possible_sum:
        invalid_number = data[i]
        break

print(invalid_number)

# Part 2
possible_sum = []
nset = 2
invalid_index = i
while invalid_number not in possible_sum and nset <= 1000:
    possible_combi = [data[i:i+nset] if i+nset <= len(data[:invalid_index]) else [] for i in range(len(data[:invalid_index]))]
    possible_sum = [sum(combi) for combi in possible_combi]
    nset += 1

l = possible_combi[possible_sum.index(invalid_number)]

print(max(l) + min(l))