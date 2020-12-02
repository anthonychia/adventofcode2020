import numpy as np

a = np.genfromtxt('input.txt')

# Part 1

for i in range(len(a)):
    for j in range(i, len(a)):
        if a[i] + a[j] == 2020:
            print(a[i] * a[j])
            break

# Part 2

for i in range(len(a)):
    for j in range(i, len(a)):
        for k in range(j, len(a)):
            if a[i] + a[j] + a[k] == 2020:
                print(a[i] * a[j] * a[k])
                break
