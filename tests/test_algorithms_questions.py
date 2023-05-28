"""Test the functions in src.pfalgorithms_richelbilderbeek.algorithm_questions."""
import unittest

from src.pfalgorithms_richelbilderbeek.algorithms_questions import (
    is_prime,
)


class TestMediumQuestions(unittest.TestCase):

    """Class to test the functions in algorithm_questions.py."""

    def test_is_prime(self):
        """Test 'is_prime'."""
        self.assertIsNotNone(is_prime.__doc__)
        self.assertRaises(TypeError, is_prime, "I am a string")
        self.assertTrue(is_prime(2))
        self.assertFalse(is_prime(1))
        self.assertTrue(is_prime(11))

    """Your tests here.

    1: `get_digits(x)`
    2a: `flip_coin(x)`
    2b: `roll_dice(x)`
    """
