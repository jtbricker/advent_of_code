import unittest

from parameterized import parameterized

from lib.helpers import load_input
from .solution import (
    part_1,
    part_2,
)

PART_1_ANSWER = 295
PART_2_ANSWER = 1068781

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.test_data = load_input(__file__, "input_test.txt")
    
    def test_part_1(self):
        answer = part_1(self.test_data)
        self.assertEqual(answer, PART_1_ANSWER)

    def test_part_2(self):
        answer = part_2(self.test_data)
        self.assertEqual(answer, PART_2_ANSWER)

    @parameterized.expand([
        ("17,x,13,19", 3417),
        ("67,7,59,61", 754018),
        ("67,x,7,59,61", 779210),
        ("67,7,x,59,61", 1261476),
        ("1789,37,47,1889", 1202161486),
    ])
    def  test_part_2_alt(self, buses, correct_answer):
        answer = part_2([0, buses])
        self.assertEqual(answer, correct_answer)


def run_tests():
    exclude = ['test_part_2_alt']
    tests = filter(lambda x: x.startswith('test_') and x not in exclude, dir(TestSolution))
    suite = unittest.TestSuite(map(TestSolution, tests))
    results = unittest.TextTestRunner().run(suite)

if __name__ == "__main__":
    run_tests()