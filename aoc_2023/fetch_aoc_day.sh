#!/bin/bash

# Make sure to set $AOC_SESSION_COOKIE in ENV vars
export AOC_SESSION_COOKIE="53616c7465645f5ff033aa0d562e7a598442e0f1d2b4cfc6ff9c4bbb6f5316431710897f84c765cd051e52b281ae2cdc9e0b179a731365de87f8e3c516b92e38"

DAY=$(printf "%02d" $1)
# TODO: This cp produces unexpected behavior if `day_$DAY` folder already exists
cp -R day_XX day_$DAY
curl --cookie session=$AOC_SESSION_COOKIE -o ./day_$DAY/input.txt https://adventofcode.com/2023/day/$1/input
code ..
sleep 2
open -a "Google Chrome" https://adventofcode.com/2023/day/$1