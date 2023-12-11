import unittest
from logic.logic_utilities import *

class TestValidator(unittest.TestCase):
    def test_valid_phone_number(self):
        val = Validator()
        result = val.phone_number("123-1234")
        self.assertEqual(result, True)

    def test_invalid_phone_number(self):
        val = Validator()
        result = val.phone_number("12-1234")
        self.assertEqual(result, False)

