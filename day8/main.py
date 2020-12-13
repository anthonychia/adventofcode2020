import numpy as np


def string_to_int(string):
    if string[0] == '-':
        return -1 * int(string[1:])
    elif string[0] == '+':
        return int(string[1:])
    else:
        raise Exception('invalid step')


def infinite_loop_check(instructions):
    executions = []
    acc = 0
    cursor = 0
    while cursor not in executions and cursor != len(instructions):
        instruct, step = instructions[cursor]
        executions.append(cursor)
        if instruct == 'acc':
            acc += string_to_int(step)
        elif instruct == 'jmp':
            cursor += string_to_int(step)
            continue
        cursor += 1
    print(acc)
    if cursor == len(instructions):
        return False
    else:
        return True


def modify_instructions(instructions, index):
    modified_instructions = instructions.copy()
    if modified_instructions[index][0] == 'jmp':
        modified_instructions[index] = ['nop', modified_instructions[index][1]]
    elif modified_instructions[index][0] == 'nop':
        modified_instructions[index] = ['jmp', modified_instructions[index][1]]
    else:
        raise Exception('invalid modification')
    return modified_instructions


instructions = [line.split(' ') for line in open('input.txt').read().split('\n')]

# Part 1
infinite_loop_check(instructions)

# Part 2
indexes = list(np.where([instruct == 'nop' or instruct == 'jmp' for instruct, step in instructions])[0])

for cursor in indexes:
    modified_instructions = modify_instructions(instructions, int(cursor))
    if not infinite_loop_check(modified_instructions):
        break