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
        # print((key, value))
        if key == 'byr':
            checks.append(bool(re.search('(19[2-8][0-9]|199[0-9]|200[0-2])', value)))
        elif key == 'iyr':
            checks.append(bool(re.match('(201[0-9]|2020)', value)))
        elif key == 'eyr':
            checks.append(bool(re.match('(202[0-9]|2030)', value)))
        elif key == 'hgt':
            if value[-2:] == 'cm':
                checks.append((int(value[:-2]) >= 150) & (int(value[:-2]) <= 193))
            elif value[-2:] == 'in':
                checks.append((int(value[:-2]) >= 59) & (int(value[:-2]) <= 76))
            else:
                checks.append(False)
        elif key == 'hcl':
            checks.append(bool(re.match('#([0-9]|[a-f]){6}', value)))
        elif key == 'ecl':
            checks.append(bool(re.match('(amb|blu|brn|gry|grn|hzl|oth)', value)))
        elif key == 'pid':
            checks.append(bool(re.match(r'\d{9}(?!\S)', value)))
        # print(checks)
    passList.append(all(checks))

print(sum(passList))