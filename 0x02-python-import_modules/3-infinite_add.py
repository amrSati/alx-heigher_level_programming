#!/usr/bin/python3
def main():
    from sys import argv as numbers

    result = 0

    for i in range(1, len(numbers)):
        result += int(numbers[i])

    print(result)


if __name__ == "__main__":
    main()
