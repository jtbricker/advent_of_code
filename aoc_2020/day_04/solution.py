from dataclasses import dataclass
from pathlib import Path
from re import match

@dataclass
class Passport():
    byr: str = None
    iyr: str = None
    eyr: str = None
    hgt: str = None
    hcl: str = None
    ecl: str = None
    pid: str = None
    cid: str = None

    def is_valid(self):
        return (
            self.byr and
            self.iyr and
            self.eyr and 
            self.hgt and 
            self.hcl and 
            self.ecl and 
            self.pid 
        )

    def is_valid_enhanced(self):
        import re
        return (
            self.byr and bool(re.search("^\d{4}$", self.byr)) and (1920 <= int(self.byr) <= 2002) and
            self.iyr and bool(re.search("^\d{4}$", self.iyr)) and (2010 <= int(self.iyr) <= 2020) and
            self.eyr and bool(re.search("^\d{4}$", self.eyr)) and (2020 <= int(self.eyr) <= 2030) and
            self.hgt and bool(re.search("^\d+(cm|in)$", self.hgt)) and (('cm' in self.hgt and 150 <= int(self.hgt.split('cm')[0]) <= 193) or ('in' in self.hgt and 59 <= int(self.hgt.split('in')[0]) <= 76)) and
            self.hcl and bool(re.search("^#[0-9a-f]{6}$", self.hcl)) and
            self.ecl and bool(re.search("^(amb|blu|brn|gry|grn|hzl|oth)$", self.ecl)) and
            self.pid and bool(re.search("^\d{9}$", self.pid))
        )


def part_1(passports):
    """ Return the count of valid passports, where valid is defined as 
    not missing any fields (except country id - cid)

    Args:
        passports ([List[Passport]]): List of prepopulated passport objects
    """
    return sum([1 for p in passports if p.is_valid()])

def part_2(passports):
    """ Return the count of valid passports, where valid is defined as 
    the following:

        byr (Birth Year) - four digits; at least 1920 and at most 2002.
        iyr (Issue Year) - four digits; at least 2010 and at most 2020.
        eyr (Expiration Year) - four digits; at least 2020 and at most 2030.s
        hgt (Height) - a number followed by either cm or in:
            If cm, the number must be at least 150 and at most 193.
            If in, the number must be at least 59 and at most 76.
        hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
        ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
        pid (Passport ID) - a nine-digit number, including leading zeroes.
        cid (Country ID) - ignored, missing or not.

    Args:
        passports ([List[Passport]]): List of prepopulated passport objects
    """
    return sum([1 for p in passports if p.is_valid_enhanced()])

def main():
    input_path = Path(__file__).parent.absolute() / 'input.txt'

    passports = []
    with input_path.open('r') as file:
        lines = [line.strip() for line in file.readlines()]
    
    d = {}
    for line in lines:
        if not line:
            passports.append(Passport(**d))
            d = {}
        d.update({k:v for k,v in [item.split(':') for item in line.split()]})
    passports.append(Passport(**d))


    print(part_1(passports))
    print(part_2(passports))

if __name__ == "__main__":
    main()