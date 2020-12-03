#!/usr/bin/python3
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


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser("Advent of Code AOC2020")
    parser.add_argument(
        'day', nargs='*', default=None, help="Run only specific day's problem")
    args = parser.parse_args()

    if args.day:
        days = map(int, args.day)
    else:
        days = range(1, 26)

    main(days)