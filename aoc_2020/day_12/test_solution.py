import unittest

from parameterized import parameterized

from lib.helpers import load_input
from .solution import (
    part_1,
    part_2,
    Ship,
    Waypoint,
    LEFT,
    RIGHT,
)

PART_1_ANSWER = 25
PART_2_ANSWER = 286

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
        (90, LEFT, (-4, 10)),
        (180, LEFT, (-10, -4)),
        (270, LEFT, (4, -10)),
        (360, LEFT, (10, 4)),
        (90, RIGHT, (4, -10)),
        (180, RIGHT, (-10, -4)),
        (270, RIGHT, (-4, 10)),
        (360, RIGHT, (10, 4)),
    ])
    def test_waypoint_turn(self, degrees, dir, new_pos):
        waypoint = Waypoint(10,4)
        waypoint.turn(dir, degrees)
        self.assertEqual((waypoint.x, waypoint.y), new_pos)


def run_tests():
    exclude = ['test_waypoint_turn']
    tests = filter(lambda x: x.startswith('test_') and x not in exclude, dir(TestSolution))
    suite = unittest.TestSuite(map(TestSolution, tests))
    results = unittest.TextTestRunner().run(suite)

if __name__ == "__main__":
    run_tests()