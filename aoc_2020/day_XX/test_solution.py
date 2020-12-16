import unittest

from lib.helpers import load_input
from .solution import (
    part_1,
    part_2,
)

PART_1_ANSWER = 1
PART_2_ANSWER = 2

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.test_data = load_input(__file__, "input_test.txt")
    
    def test_part_1(self):
        answer = part_1(self.test_data)
        self.assertEqual(answer, PART_1_ANSWER)

    def test_part_2(self):
        answer = part_2(self.test_data)
        self.assertEqual(answer, PART_2_ANSWER)


def run_tests():
    suite = unittest.TestSuite(map(TestSolution, filter(lambda x: x.startswith('test_'), dir(TestSolution))))
    results = unittest.TextTestRunner().run(suite)

if __name__ == "__main__":
    run_tests()