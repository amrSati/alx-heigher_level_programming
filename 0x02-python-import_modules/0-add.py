#!/usr/bin/python3

def main():
    from add_0 import add as addd

    a = 1
    b = 2

    print("{} + {} = {}".format(a, b, addd(a, b)))


if __name__ == "__main__":
    main()
