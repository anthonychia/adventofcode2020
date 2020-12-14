import re
from collections import Counter
import numpy as np
from itertools import product

def convert_to_binary(number):
    return format(number, '036b')

def apply_mask(mask, number):
    binary = convert_to_binary(number)
    after_mask_binary = ''.join([binary[i] if mask[i] == 'X' else mask[i] for i in range(len(binary))])
    return int(after_mask_binary, 2)

def apply_mask_v2(mask, number):
    l = []
    binary = convert_to_binary(number)
    binary_list = list(binary).copy()
    for i in range(len(mask)):
        if mask[i] == 'X':
            binary_list[i] = 'X'
        elif mask[i] == '1':
            binary_list[i] = '1'
    repeat = Counter(mask)['X']
    X_pos = list(np.where(np.array([i for i in mask]) == 'X')[0])
    seq_list = [seq for seq in product("01", repeat=repeat)]

    l_binary = []
    if len(X_pos) > 0:
        for seq in seq_list:
            for i in range(len(seq)):
                binary_list[X_pos[i]] = seq[i]
            binary_str = ''.join(binary_list)
            l_binary.append(binary_str)
            l.append(int(binary_str, 2))
    else:
        binary_str = ''.join(binary_list)
        l_binary.append(binary_str)
        l.append(int(binary_str, 2))
    return l


data = open('input.txt').read().split('mask')

ops = {re.findall(r'^ = ([X0-9]+)', line)[0]:
           {int(i): int(j) for i, j in re.findall(r'mem\[([0-9]+)\] = ([0-9]+)', line)} for line in data[1:]}

# Part 1
mem = {}
for mask, op in ops.items():
    # check if there's value in mem
    for key, v in op.items():
        mem[key] = apply_mask(mask, v)

print(sum(mem.values()))

# Part 2
mem_v2 = {}
for mask, op in ops.items():
    # check if there's value in mem
    for key, v in op.items():
        new_add = apply_mask_v2(mask, key)
        for add in new_add:
            mem_v2[add] = v

# total = 0
# for k, v in mem_v2.items():
#     if isinstance(v, list):
#         total += sum(v)
#     else:
#         raise Exception('mem address contains no value or wrong type')
#
print(sum(mem_v2.values()))