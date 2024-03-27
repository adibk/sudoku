import unittest
import sys
import os

import random

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from utils import calculus

class TestCalculus(unittest.TestCase):
    def setUp(self):
        self.max_test = 1_000_000_000_000
        self.nb_rand_test = 20
        
    def test_perfect_sqrt_None(self):
        self.assertEqual(calculus.perfect_sqrt(None), None)
    
    def test_perfect_sqrt_sple_values(self):
        self.assertEqual(calculus.perfect_sqrt(1), 1)
        self.assertEqual(calculus.perfect_sqrt(0), 0)
        self.assertEqual(calculus.perfect_sqrt(-1), None)
        self.assertEqual(calculus.perfect_sqrt(4), 2)

    def test_perfect_sqrt_hardcoded_success(self):
        self.assertEqual(calculus.perfect_sqrt(256), 16)
        self.assertEqual(calculus.perfect_sqrt(10000), 100)
        self.assertEqual(calculus.perfect_sqrt(1780199 * 1780199), 1780199)

    def test_perfect_sqrt_rand(self):
        for _ in range(self.nb_rand_test):
            rand_int = random.randint(1, self.max_test)
            self.assertEqual(calculus.perfect_sqrt(rand_int * rand_int), rand_int)
        
    def test_perfect_sqrt_rand_neg(self):
        for _ in range(self.nb_rand_test):
            self.assertEqual(calculus.perfect_sqrt(-random.randint(1, self.max_test)), None)

    def test_perfect_sqrt_rand_fail(self):
        """Test calculus.perfect_sqrt with various invalid inputs that should all fail."""
        invalid_inputs = ['string', 'c', (4,), {4}, [4], [1, 2, 3]]

        for input in invalid_inputs:
            with self.subTest(input_value=input):
                with self.assertRaises(TypeError):
                    calculus.perfect_sqrt(input)
