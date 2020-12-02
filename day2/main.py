import numpy as np
from collections import Counter 

# Part 1

regexp = r'([0-9]+)-([0-9]+) ([a-zA-Z]): ([a-zA-Z0-9]+)'
output = np.fromregex('input.txt', regexp, 
                    [('min', np.int64), ('max', np.int64), ('letter', 'U1'), ('password', 'object')])
                    
print(sum([ (Counter(password)[letter] >= min) & (Counter(password)[letter] <= max) for min, max, letter, password in output ]))

# Part 2

print(sum([ (password[pos1-1] == letter) != (password[pos2-1] == letter) for pos1, pos2, letter, password in output ]))
        