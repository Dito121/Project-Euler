import unittest
from problem_1 import sum_of_3_5_multiples
from problem_2 import sum_of_fibonacci_sequence


class test_problems(unittest.TestCase):
    def test_problem_1(self):
        self.assertEqual(sum_of_3_5_multiples(10), 23)

    def test_problem_2(self):
        self.assertEqual(sum_of_fibonacci_sequence(4000000), 4613732)


if __name__ == '__main__':
    unittest.main()
