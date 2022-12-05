#!/bin/bash

# Make sure to set $AOC_SESSION_COOKIE in ENV vars
export AOC_SESSION_COOKIE="53616c7465645f5f8f04bb70cd6e84e86d4705153636896cf332f6c649fd3ee80a21c6b250bfb20cd95f161f9a9f27c9"

DAY=$(printf "%02d" $1)
cp -R day_XX day_$DAY
curl --cookie session=$AOC_SESSION_COOKIE -o ./day_$DAY/input.txt https://adventofcode.com/2021/day/$1/input
code /Users/justin.bricker/eventbrite/my/advent_of_code/
sleep 2
open -a "Google Chrome" https://adventofcode.com/2021/day/$1