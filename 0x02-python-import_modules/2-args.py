#!/usr/bin/python3
def main():
    from sys import argv as args

    length = len(args)

    print("{} argument".format(length - 1), end='')
    if length == 1:
        print("s.")
        return
    if length == 2:
        print(":\n1: {}".format(args[1]))
        return

    print("s:")
    for i in range(1, length):
        print("{}: {}".format(i, args[i]))


if __name__ == "__main__":
    main()
