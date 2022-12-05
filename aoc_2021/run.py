#!/Users/justin.bricker/eventbrite/my/advent_of_code/aoc_2021/venv/bin/python
# -*- coding: utf-8 -*-

import os
import importlib


def main(which_days):
    for day in which_days:
        day_module = importlib.import_module(
            'day_{0:02d}'.format(day))
        print("Solutions to Day {0:02d}\n-------------------".format(day))
        day_module.main()
        print('')

def test(day):
    test_module = importlib.import_module('day_{0:02d}.test_solution'.format(day))
    print("Tests for Day {0:02d}\n-------------------".format(day))
    test_module.run_tests()
    print('')

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser("Advent of Code AOC2020")
    parser.add_argument(
        'day', nargs=1, default=None, help="Run only specific day's problem")
    parser.add_argument(
        '--test', '-t', action='store_true', help="Run test for day")
    args = parser.parse_args()

    if args.day:
        days = map(int, args.day)
    else:
        days = range(1, 26)

    if args.test:
        day = list(days)[0]
        test(day)
    
    else:
        main(days)