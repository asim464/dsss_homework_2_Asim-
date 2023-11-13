import unittest
from math_quiz import random_integer, random_choice, math_problem


class TestMathGame(unittest.TestCase):

    def test_function_A(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_function_B(self):
        operators =["+","-","*"]
        for _ in range(1000):
            random_operator= random_choice()
            self.assertIn(random_operator,operators)


    def test_function_C(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (5, 3, "*", "5*3", 15),
                (10, 2, "-", "10-2", 8)
    
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                problem, result = math_problem(num1, num2, operator)
                self.assertEqual(result,expected_answer)
                pass

if __name__ == "__main__":
    unittest.main()
