#!/bin/bash

# Make sure to set $AOC_SESSION_COOKIE in ENV vars
export AOC_SESSION_COOKIE="53616c7465645f5f9b42f17f21690b471e6ec2a64d8d7dc4cd788436926ca010b6865bceb5b48ed567af57b792525a8efb4f180b001fae2182089db166a4a7ef"

DAY=$(printf "%02d" $1)
# TODO: This cp produces unexpected behavior if `day_$DAY` folder already exists
cp -R day_XX day_$DAY
curl --cookie session=$AOC_SESSION_COOKIE -o ./day_$DAY/input.txt https://adventofcode.com/2022/day/$1/input
code ..
sleep 2
open -a "Google Chrome" https://adventofcode.com/2022/day/$1