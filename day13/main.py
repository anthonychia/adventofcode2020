import numpy as np
import math

f = open('input.txt')
earliest = int(f.readline())
l = [(index, bus) for index, bus in enumerate(f.readline().split(','))]
bus_pos, bus_id = list(zip(*l))
bus_id = np.asarray(bus_id)
bus_pos = np.asarray(bus_pos)
f.close()

mask = bus_id != 'x'
bus_id = bus_id[bus_id != 'x']
bus_pos = bus_pos[mask]
bus_id = [int(bus) for bus in bus_id]
schedule = [math.ceil(earliest/bus)*bus for bus in bus_id]
closest_bus = bus_id[schedule.index(min(schedule))]

# Part 1
print((math.ceil(earliest/closest_bus)*closest_bus - earliest)*closest_bus)

# Part 2
def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

