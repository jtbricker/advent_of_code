#!/usr/local/bin/python

from lib.helpers import load_input

def main():
    data = [int(line) for line in load_input(__file__)]

    # Part 1:  Find the 2 numbers in the list that sum to 2020, print their product
    for line in data:
        if (2020 - line) in data:
            print(line*(2020-line))
            break

    # Part 2:  Find the 3 numbers in the list that sum to 2020, print their product
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            x = data[i]
            y = data[j]
            if (2020 - x - y) in data[j+1:]:
                print(x*y*(2020-x-y))
                return

if __name__ == "__main__":
    main()