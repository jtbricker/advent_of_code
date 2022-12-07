import unittest

from lib.helpers import load_input_raw
from .solution import (
    part_1,
    part_2,
    parse_data,
)

PART_1_ANSWER = 'CMZ'
PART_2_ANSWER = 'MCD'

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.test_data = load_input_raw(__file__, "input_test.txt")
    
    def test_part_1(self):
        answer = part_1(self.test_data)
        self.assertEqual(answer, PART_1_ANSWER)

    def test_part_2(self):
        answer = part_2(self.test_data)
        self.assertEqual(answer, PART_2_ANSWER)

    def test_parse_data(self):
        expected_first_row_of_columns = ['Z', 'N']
        expected_first_instruction = { 'to': 1, 'from': 2, 'count': 1}
        
        columns, instructions = parse_data(self.test_data)
        
        self.assertEqual(columns[1], expected_first_row_of_columns)
        self.assertEqual(instructions[0], expected_first_instruction)


def run_tests():
    exclude = []
    tests = filter(lambda x: x.startswith('test_') and x not in exclude, dir(TestSolution))
    suite = unittest.TestSuite(map(TestSolution, tests))
    results = unittest.TextTestRunner().run(suite)

if __name__ == "__main__":
    run_tests()