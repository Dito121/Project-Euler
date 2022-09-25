import unittest
from problem_1 import sum_of_3_5_multiples
from problem_2 import sum_of_fibonacci_sequence
from problem_3 import find_prime_factors
from problem_4 import largest_palindrome
from problem_5 import problem_5
from problem_6 import problem_6
from problem_7 import problem_7


class test_problems(unittest.TestCase):
    def test_problem_1(self):
        self.assertEqual(sum_of_3_5_multiples(10), 23)

    def test_problem_2(self):
        self.assertEqual(sum_of_fibonacci_sequence(4000000), 4613732)

    # def test_problem_3(self):
    #     self.assertEqual(find_prime_factors(13195), [5, 7, 13, 29])

    # def test_problem_4(self):
    #     self.assertEqual(largest_palindrome(100), "9009")

    def test_problem_5(self):
        self.assertEqual(problem_5(10), 2520)

    def test_problem_6(self):
        self.assertEqual(problem_6(10), 2640)

    def test_problem_7(self):
        self.assertEqual(problem_7(6), 13)


if __name__ == '__main__':
    unittest.main()
