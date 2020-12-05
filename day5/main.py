import math
import numpy as np


def binary_partition(sequence, rrange):
    mini = rrange[0]
    maxi = rrange[1]
    for i in sequence:
        cursor = math.ceil((maxi - mini)/2)
        if i == 'B' or i == 'R':
            mini = mini + cursor
        if i == 'F' or i == 'L':
            maxi = maxi - cursor
    if mini == maxi:
        return mini
    else:
        raise Exception("doesn't converge")


partitions = open('input.txt').read().split('\n')

rowRange = (0, 127)
seatRange = (0, 7)

seatList = [(binary_partition(p[:7], rowRange), binary_partition(p[-3:], seatRange)) for p in partitions]

# Part 1

print(max([row*8 + seat for row, seat in seatList]))

# Part 2

seatMatrix = np.zeros((max(rowRange)+1, max(seatRange)+1))

for row, seat in seatList:
    seatMatrix[row, seat] = 1

# Find my seat
for rindex, row in enumerate(seatMatrix):
    if sum([i == 0 for i in row]) == 1:
        myRow = rindex
        for sindex, seat in enumerate(row):
            if seat == 0: mySeat = sindex
        break

print(myRow*8 + mySeat)
