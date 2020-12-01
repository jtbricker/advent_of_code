#!/bin/bash

# Make sure to set $AOC_SESSION_COOKIE in ENV vars

DAY=$(printf "%02d" $1)
curl --cookie session=$AOC_SESSION_COOKIE -o ./2020/day_$DAY/input.txt --create-dirs https://adventofcode.com/2020/day/$1/input
touch ./2020/day_$DAY/solution.py
touch ./2020/day_$DAY/__init__.py
code .
sleep 2
open -a "Google Chrome" https://adventofcode.com/2020/day/$1