import unittest

from lib.helpers import load_input
from .solution import (
    part_1,
    part_2,
    calculate_scenic_score,
    parse_data,
)

PART_1_ANSWER = 21
PART_2_ANSWER = 8

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.test_data = load_input(__file__, "input_test.txt")
        self.parsed_data = parse_data(self.test_data)
    
    def test_part_1(self):
        answer = part_1(self.test_data)
        self.assertEqual(answer, PART_1_ANSWER)
    
    def test_part_2_calculate_scenic_score_second_row_middle(self):
        scenic_score = calculate_scenic_score(self.parsed_data, 1, 2)
        self.assertEqual(scenic_score, 4)

    def test_part_2_calculate_scenic_score_fourth_row_middle(self):
        scenic_score = calculate_scenic_score(self.parsed_data, 3, 2)
        self.assertEqual(scenic_score, 8)
    
    def test_part_2_final(self):
        answer = part_2(self.test_data)
        self.assertEqual(answer, PART_2_ANSWER)


def run_tests():
    exclude = []
    tests = filter(lambda x: x.startswith('test_') and x not in exclude, dir(TestSolution))
    suite = unittest.TestSuite(map(TestSolution, tests))
    results = unittest.TextTestRunner().run(suite)

if __name__ == "__main__":
    run_tests()