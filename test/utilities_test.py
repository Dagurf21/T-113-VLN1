import unittest
from logic.logic_utilities import *

class TestValidator(unittest.TestCase):
    def setUp(self):
        self.validator = Validator()

    def test_valid_phone_number(self):
        self.assertTrue(self.validator.phone_number("123-1234"))

    def test_invalid_phone_number(self):
        self.assertFalse(self.validator.phone_number("12-1234"))

    def test_valid_ssn(self):
        self.assertTrue(self.validator.ssn("1112231239"))

    def test_invalid_ssn(self):
        self.assertFalse(self.validator.ssn("1113231239"))
        self.assertFalse(self.validator.ssn("1122231239"))
        self.assertFalse(self.validator.ssn("1112231232"))
        self.assertFalse(self.validator.ssn("1112231233"))
        self.assertFalse(self.validator.ssn("4112231239"))

    def test_valid_email(self):
        self.assertTrue(self.validator.email("a@a.is"))
        self.assertTrue(self.validator.email("a@a.a.a"))
        self.assertTrue(self.validator.email("a_a@a.a"))
        self.assertTrue(self.validator.email("a.a@a.a"))
        
    def test_invalid_email(self):
        self.assertFalse(self.validator.email("a.@a"))
        self.assertFalse(self.validator.email(".@a"))
        self.assertFalse(self.validator.email("a@.a"))
        self.assertFalse(self.validator.email("@.a"))
        self.assertFalse(self.validator.email("a.@"))
        self.assertFalse(self.validator.email("a@."))
        self.assertFalse(self.validator.email(".@"))
        self.assertFalse(self.validator.email("a@a@a.a"))

