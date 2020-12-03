#!/bin/bash

# Make sure to set $AOC_SESSION_COOKIE in ENV vars

DAY=$(printf "%02d" $1)
cp -R day_XX day_$DAY
curl --cookie session=$AOC_SESSION_COOKIE -o ./day_$DAY/input.txt https://adventofcode.com/2020/day/$1/input
code /Users/justin.bricker/eventbrite/my/advent_of_code/
sleep 2
open -a "Google Chrome" https://adventofcode.com/2020/day/$1