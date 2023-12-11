import unittest
from logic.flight_logic import *
from test.mock_data_wrapper import MockDataWrapper

class TestFlight(unittest.TestCase):
    def test_create_valid_flight(self):
        data = MockDataWrapper()

