import unittest

from logic.destination_logic import DestinationLogic
from test.mock_data_wrapper import MockDataWrapper
from model import Destination

class TestDestinations(unittest.TestCase):
    def test_create_destination_all_valid(self):
        data = MockDataWrapper()
        destinations = DestinationLogic(data)

        destinations.create_destination(Destination(
            id=0,
            country="Test",
            airport="BIRK",
            distance_km=192,
            flight_time=300,
            representative="John",
            emergency_number="123-1234",
        ))

        result = data.get_all_employees()
        self.assertTrue(len(result) > 0)

        result = result[0]
        self.assertEqual(result, Destination(
            id=0,
            country="Test",
            airport="BIRK",
            distance_km=192,
            flight_time=300,
            representative="John",
            emergency_number="123-1234",
        ))

    def test_create_destination_invalid_distance(self):
        data = MockDataWrapper()
        destinations = DestinationLogic(data)

        destinations.create_destination(Destination(
            id=0,
            country="Test",
            airport="BIRK",
            distance_km=-192,
            flight_time=300,
            representative="John",
            emergency_number="123-1234",
        ))

        result = data.get_all_employees()
        self.assertTrue(len(result) == 0)

    def test_create_destination_invalid_flight_time(self):
        data = MockDataWrapper()
        destinations = DestinationLogic(data)

        destinations.create_destination(Destination(
            id=0,
            country="Test",
            airport="BIRK",
            distance_km=192,
            flight_time=-300,
            representative="John",
            emergency_number="123-1234",
        ))

        result = data.get_all_employees()
        self.assertTrue(len(result) == 0)

    def test_create_destination_invalid_number(self):
        data = MockDataWrapper()
        destinations = DestinationLogic(data)

        destinations.create_destination(Destination(
            id=0,
            country="Test",
            airport="BIRK",
            distance_km=192,
            flight_time=-300,
            representative="John",
            emergency_number="12-1234",
        ))

        result = data.get_all_employees()
        self.assertTrue(len(result) == 0)
