import unittest
from app.logic import prime_generator

class TestPrimeNumberGenerator(unittest.TestCase):
    #Tests for correct output for inputs less or equal to 20
    def test_prime_generator(self):
        self.assertEqual(prime_generator(20),[2,3,5,7,11,13,17])

    #Tests correct output for inputs more than 50
    def test_prime_generator_large_input(self):
        self.assertEqual(prime_generator(80),[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79])

        #Tests correct error message for wrong string input
    def test_prime_generator_string_input(self):
        self.assertEqual(prime_generator('y'),'Input must be an integer, String given')

    #Tests correct error message for wrong float input
    def test_prime_generator_float_input(self):
        self.assertEqual(prime_generator(122.3333),'Input must be an integer, Float given')