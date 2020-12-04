import numpy as np
import re

filename = 'input.txt'

npassport = sum(line == '\n' for line in open(filename))
passportList = []

f = open(filename)

for passport in range(npassport):
    line = f.readline()
    list = {}
    while line != '\n':
        list.update({field.split(':')[0]: field.split(':')[1] for field in line.replace('\n', '').split(' ')})
        line = f.readline()
    passportList.append(list)

required = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])

passportList = np.asarray(passportList)

# Part 1

valid = [len(set(passport.keys()).intersection(required)) >= len(required) for passport in passportList]
print(sum(valid))

# Part 2

passList = []
for passport in passportList[valid]:
    checks = []
    for key, value in passport.items():
        print((key, value))
        if key == 'byr':
            checks.append((int(value) >= 1920) & (int(value) <= 2002))
        elif key == 'iyr':
            checks.append((int(value) >= 2010) & (int(value) <= 2020))
        elif key == 'eyr':
            checks.append((int(value) >= 2020) & (int(value) <= 2030))
        elif key == 'hgt':
            if value[-2:] == 'cm': checks.append((int(value[:-2]) >= 150) & (int(value[:-2]) <= 193))
            elif value[-2:] == 'in': checks.append((int(value[:-2]) >= 59) & (int(value[:-2]) <= 76))
        elif key == 'hcl':
            checks.append(bool(re.search('^#[0-9a-f]{6}$', value)))
        elif key == 'ecl':
            checks.append(value in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'))
        elif key == 'pid':
            checks.append(all(char.isdigit() for char in value) & (len(value) == 9))
        print(checks)
    passList.append(all(checks))

print(sum(passList))