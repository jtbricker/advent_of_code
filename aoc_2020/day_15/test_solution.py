import unittest

from lib.helpers import load_input
from .solution import (
    part_1,
    part_2,
)

PART_1_ANSWER = 436
PART_2_ANSWER = 175594

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.test_data = load_input(__file__, "input_test.txt")
    
    def test_part_1_1(self):
        answer = part_1(self.test_data)
        self.assertEqual(answer, PART_1_ANSWER)

    # def test_part_1_2(self):
    #     answer = part_1(["1,3,2"])
    #     self.assertEqual(answer, 1)

    # def test_part_1_3(self):
    #     answer = part_1(["2,1,3"])
    #     self.assertEqual(answer, 10)

    # def test_part_1_4(self):
    #     answer = part_1(["1,2,3"])
    #     self.assertEqual(answer, 27)

    # def test_part_1_5(self):
    #     answer = part_1(["2,3,1"])
    #     self.assertEqual(answer, 78)

    # def test_part_1_6(self):
    #     answer = part_1(["3,2,1"])
    #     self.assertEqual(answer, 438)

    # def test_part_1_7(self):
    #     answer = part_1(["3,1,2"])
    #     self.assertEqual(answer, 1836)

    # def test_part_2(self):
    #     answer = part_2(self.test_data)
    #     self.assertEqual(answer, PART_2_ANSWER)

    # def test_part_2_2(self):
    #     answer = part_2(["1,3,2"])
    #     self.assertEqual(answer, 2578)

    # def test_part_2_3(self):
    #     answer = part_2(["2,1,3"])
    #     self.assertEqual(answer, 3544142)

    # def test_part_2_4(self):
    #     answer = part_2(["1,2,3"])
    #     self.assertEqual(answer, 261214)

    # def test_part_2_5(self):
    #     answer = part_2(["2,3,1"])
    #     self.assertEqual(answer, 6895259)

    # def test_part_2_6(self):
    #     answer = part_2(["3,2,1"])
    #     self.assertEqual(answer, 18)

    # def test_part_2_7(self):
    #     answer = part_2(["3,1,2"])
    #     self.assertEqual(answer, 362)


def run_tests():
    exclude = []
    tests = filter(lambda x: x.startswith('test_') and x not in exclude, dir(TestSolution))
    suite = unittest.TestSuite(map(TestSolution, tests))
    results = unittest.TextTestRunner().run(suite)

if __name__ == "__main__":
    run_tests()