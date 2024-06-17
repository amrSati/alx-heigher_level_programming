#!/usr/bin/python3

for c in range(-122, -96, 2):
    print("{:c}{:c}".format((c * -1), ((c * -1) - 33)), end='')
