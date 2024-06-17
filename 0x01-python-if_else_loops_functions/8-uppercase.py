#!/usr/bin/python3

def uppercase(str):
    cc = 0

    for c in str:
        cc = ord(c)
        if cc in range(97, 123):
            cc -= 32
        print("{:c}".format(cc), end='')

    print()
