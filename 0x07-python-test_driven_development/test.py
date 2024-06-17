#!/usr/bin/python3
func = __import__("4-print_square").print_square
"""Testing ``print_square`` function
"""


def main():
    func(4)
    print("")
    func(10)
    print("")
    func(0)
    print("")
    func(1)
    print("")
    print("AAAAA")
    try:
        print_square(-1)
    except Exception:
        print(Exception)
    print("")


if __name__ == "__main__":
    main()
