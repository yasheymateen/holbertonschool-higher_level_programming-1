#!/usr/bin/python3
for c in range(25, -1, -1):
    if c % 2 == 1:
        c += 97
    else:
        c += 65
    print('{:s}'.format(chr(c)), end='')
