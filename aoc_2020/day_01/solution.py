#!/usr/local/bin/python

import pathlib

def main():
    input_path = pathlib.Path(__file__).parent.absolute() / 'input.txt'
    with input_path.open('r') as file:
        lines = [int(line) for line in file.readlines() if line.strip() != '']

    # Part 1:  Find the 2 numbers in the list that sum to 2020, print their product
    for line in lines:
        if (2020 - line) in lines:
            print(line*(2020-line))
            break

    # Part 2:  Find the 3 numbers in the list that sum to 2020, print their product
    for i in range(len(lines)):
        for j in range(i+1, len(lines)):
            x = lines[i]
            y = lines[j]
            if (2020 - x - y) in lines[j+1:]:
                print(x*y*(2020-x-y))
                return

if __name__ == "__main__":
    main()