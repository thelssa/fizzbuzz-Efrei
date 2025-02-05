import unittest
from io import StringIO
import sys
from main import fizzbuzz

class TestFizzBuzz(unittest.TestCase):
    def setUp(self):
        self.held, sys.stdout = sys.stdout, StringIO()

    def tearDown(self):
        sys.stdout = self.held

    def test_fizzbuzz_divisible_by_3_and_5(self):
        fizzbuzz(15)
        self.assertEqual(sys.stdout.getvalue().strip(), "FizzBuzzBuzz")

    def test_fizzbuzz_divisible_by_3(self):
        fizzbuzz(9)
        self.assertEqual(sys.stdout.getvalue().strip(), "Fizz")

    def test_fizzbuzz_divisible_by_5(self):
        fizzbuzz(10)
        self.assertEqual(sys.stdout.getvalue().strip(), "Buzz")

    def test_fizzbuzz_contains_3(self):
        fizzbuzz(13)
        self.assertEqual(sys.stdout.getvalue().strip(), "13Fizz")

    def test_fizzbuzz_contains_5(self):
        fizzbuzz(52)
        self.assertEqual(sys.stdout.getvalue().strip(), "52Buzz")

    def test_fizzbuzz_not_divisible_or_contains_3_or_5(self):
        fizzbuzz(7)
        self.assertEqual(sys.stdout.getvalue().strip(), "7")

if __name__ == '__main__':
    unittest.main()