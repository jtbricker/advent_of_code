from lib.helpers import load_input

from collections import Counter

def part_1(data):
    # For each rule and password in input, count the number of
    # passwords that follow the rule
    # Rule:  min-max char, `char` can appear exactly between min and max times in pw
    count = 0
    for d in data:
        tmp = d.split(':')
        pw = tmp[1].strip()
        rule = tmp[0].strip().split()[0]
        char = tmp[0].strip().split()[1]
        min_rule = int(rule.split('-')[0].strip())
        max_rule = int(rule.split('-')[1].strip())
        counts = Counter(pw)

        if min_rule <= counts[char] <= max_rule:
            count += 1
    
    print(count)

def part_2(data):
    # For each rule and password in input, count the number of
    # passwords that follow the rule
    # Rule:  ind1-ind2 char, `char` must appear at either or both ind1 or ind2 (1-based indexing)
    count = 0
    for d in data:
        tmp = d.split(':')
        pw = tmp[1].strip()
        rule = tmp[0].strip().split()[0]
        char = tmp[0].strip().split()[1]
        ind1 = int(rule.split('-')[0].strip()) - 1
        ind2 = int(rule.split('-')[1].strip()) - 1

        if  (pw[ind1] == char or pw[ind2] == char) and not (pw[ind1] == char and pw[ind2] == char):
            count += 1
    
    print(count)

def main():   
    data = load_input(__file__)

    part_1(data)
    part_2(data)

if __name__ == "__main__":
    main()