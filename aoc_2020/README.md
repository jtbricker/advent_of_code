# Advent of Code 2020

## Automatically Download the input and create boilerplate

* Ensure that you have the `AOC_SESSION_COOKIE` env variable defined
* Run the `fetch_aoc_day.sh` script, passing in the day you are fetching (e.g 2, 12, 25)
  * This Creates the `day_##` package folder with a `solution.py` file for the solution and `input.txt` with the programs puzzle input.

## Run the solution(s)
* Use the `run.py` script, optionally passing in the day you want to run (by default it will run all days)
  * e.g. `./run.py 3` will run the `main()` method located in `day_03/solution.py`