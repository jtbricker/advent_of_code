import unittest

from lib.helpers import load_input
from .solution import (
    part_1,
    part_2,
)

PART_1_ANSWER = 7
PART_2_ANSWER = 19

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.test_data = load_input(__file__, "input_test.txt")
    
    def test_part_1_1(self):
        answer = part_1(self.test_data)
        self.assertEqual(answer, PART_1_ANSWER)

    def test_part_1_2(self):
        answer = part_1("bvwbjplbgvbhsrlpgdmjqwftvncz")
        self.assertEqual(answer, 5)
    
    def test_part_1_3(self):
        answer = part_1("nppdvjthqldpwncqszvftbrmjlhg")
        self.assertEqual(answer, 6)

    def test_part_1_4(self):
        answer = part_1("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg")
        self.assertEqual(answer, 10)

    def test_part_1_5(self):
        answer = part_1("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw")
        self.assertEqual(answer, 11)

    def test_part_2_1(self):
        answer = part_2(self.test_data)
        self.assertEqual(answer, PART_2_ANSWER)

    def test_part_2_2(self):
        answer = part_2("bvwbjplbgvbhsrlpgdmjqwftvncz")
        self.assertEqual(answer, 23)
    
    def test_part_2_3(self):
        answer = part_2("nppdvjthqldpwncqszvftbrmjlhg")
        self.assertEqual(answer, 23)

    def test_part_2_4(self):
        answer = part_2("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg")
        self.assertEqual(answer, 29)

    def test_part_2_5(self):
        answer = part_2("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw")
        self.assertEqual(answer, 26)


def run_tests():
    exclude = []
    tests = filter(lambda x: x.startswith('test_') and x not in exclude, dir(TestSolution))
    suite = unittest.TestSuite(map(TestSolution, tests))
    results = unittest.TextTestRunner().run(suite)

if __name__ == "__main__":
    run_tests()