import numpy as np
from collections import Counter
import math

bag = [int(line) for line in open('input.txt').read().split('\n')]
bag.sort()

built_in = max(bag) + 3
bag.append(built_in)

diff = []
current_jolt = 0

for adapter in bag:
    diff.append(adapter - current_jolt)
    current_jolt = adapter

# Part 1
counts = Counter(diff)

print(counts[1]*counts[3])


# Part 2
# count consecutive repeated numbers < 3
repeated = np.array([len(j) for j in ''.join([str(i) for i in diff]).split('3')])
repeated = repeated[repeated > 1]


def ncr(n, k):
    n_fac = math.factorial(n)
    k_fac = math.factorial(k)
    n_minus_k_fac = math.factorial(n - k)
    return n_fac//(k_fac*n_minus_k_fac)

combi = []

for i in repeated:
    r = i-1
    rsum = 0
    while r >= 0 and i-r <= 3:
        # print((i-1, r))
        rsum += ncr(i-1, r)
        r -= 1
    combi.append(rsum)

print(np.prod(combi, dtype='int64'))

