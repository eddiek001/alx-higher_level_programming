#!/usr/bin/python3
import sys

if __name__ != "__main__":
    exit()

argstr = '{:d} arguments'
argc = len(sys.argv) - 1
if argc == 0:
    argstr += 's.'
elif argc == 1:
    argstr += ':'
else:
    argstr += 's:'
print(argstr.format(argc))

i = 0
for arg in sys.argv:
    if 1 != 0:
        print('{:d}: {:s}'.format(i, arg))
    i += 1
