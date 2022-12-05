from lib.helpers import load_input

class BagRule:
    def __init__(self, bag_type, rules_str):
        self.bag_type = bag_type
        self.rules = self._parse_rules(rules_str)

    def _parse_rules(self, rules_str):
        rules = {}

        rules_strings = rules_str.split(',')
        for r in rules_strings:
            num_limit = r.split()[0]
            if num_limit == 'no':
                continue
            else:
                num_limit = int(num_limit)
            bag_type = " ".join(r.split('bag')[0].strip().split()[1:])
            rules[bag_type] = num_limit
        return rules

    def can_contain(self, bag_type):
        return bag_type in self.rules.keys()


def get_bags_that_can_hold(bag_rules, bag_type="shiny gold"):
    can_hold = []
    for bt, rule in bag_rules.items():
        if rule.can_contain(bag_type):
            can_hold.append(bt)
            can_hold += get_bags_that_can_hold(bag_rules, bt)

    return can_hold

def get_bag_count(bag_rules, bag_type):
    count = 0
    bag_rule = bag_rules[bag_type]
    for bt, num in bag_rule.rules.items():
        count += ( num + num * get_bag_count(bag_rules, bt) )
    return count

def part_1(bag_rules):
    """Determine how many different outer bags could contain a "shiny gold"
    bag based on the provided rules

    Args:
        data (dict[str:BagRule]): Dictionary of rules keyed by bag_type
    """
    return len(set(get_bags_that_can_hold(bag_rules, "shiny gold")))

def part_2(bag_rules):
    """Count the total number of bags inside of the "shiny gold" bag given the
    required rules

    Args:
        data (dict[str:BagRule]): Dictionary of rules keyed by bag_type
    """
    return get_bag_count(bag_rules, 'shiny gold')

def main():
    data = load_input(__file__)

    bag_rules = {}
    for line in data:
        bag_type, rules_str = [x.strip() for x in line.strip()[:-1].split("bags contain")] # Trim and remove period
        bag_rules[bag_type] = BagRule(bag_type, rules_str)

    # Make sure there is only one set of rules per bag_type in the input
    assert(len(bag_rules.keys()) == len(data))

    print(part_1(bag_rules))
    print(part_2(bag_rules))

if __name__ == "__main__":
    main()