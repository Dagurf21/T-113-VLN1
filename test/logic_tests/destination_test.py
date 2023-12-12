import unittest

from logic.destination_logic import DestinationLogic
from .mock_data_wrapper import MockDataWrapper
from model import Destination


class TestDestinations(unittest.TestCase):
    MOCK_DESTINATIONS = [
        Destination(
            country="Test",
            airport="BIRK",
            distance_km=0,
            flight_time=0,
            representative="Chuck Norris",
            emergency_number="581-2345",
        ),
        Destination(
            country="Greenland",
            airport="BGGH",
            distance_km=1427,
            flight_time=200,
            representative="Also Chuck Norris",
            emergency_number="581-2345",
        ),
    ]

    def test_create_destination_all_valid(self):
        data = MockDataWrapper()
        destination_logic = DestinationLogic(data)

        for dest in self.MOCK_DESTINATIONS:
            destination_logic.create_destination(dest)

        result = []

        for dest in data.get_all_destinations():
            dest.id = None
            result.append(dest)

        self.assertListEqual(
            result,
            self.MOCK_DESTINATIONS,
            "Destination should have been created as it has valid data",
        )

    def test_create_destination_invalid_distance(self):
        data = MockDataWrapper()
        destination_logic = DestinationLogic(data)

        destination_logic.create_destination(
            Destination(
                id=0,
                country="Test",
                airport="BIRK",
                distance_km=-192,
                flight_time=300,
                representative="John",
                emergency_number="123-1234",
            )
        )

        result = data.get_all_destinations()
        self.assertTrue(
            len(result) == 0,
            "The destination should not have been created as it has invalid data",
        )

    def test_create_destination_invalid_flight_time(self):
        data = MockDataWrapper()
        destination_logic = DestinationLogic(data)

        destination_logic.create_destination(
            Destination(
                id=0,
                country="Test",
                airport="BIRK",
                distance_km=192,
                flight_time=-300,
                representative="John",
                emergency_number="123-1234",
            )
        )

        result = data.get_all_destinations()
        self.assertTrue(
            len(result) == 0,
            "The destination should not have been created as it has invalid data",
        )

    def test_create_destination_invalid_number(self):
        data = MockDataWrapper()
        destination_logic = DestinationLogic(data)

        destination_logic.create_destination(
            Destination(
                id=0,
                country="Test",
                airport="BIRK",
                distance_km=192,
                flight_time=-300,
                representative="John",
                emergency_number="12-1234",
            )
        )

        result = data.get_all_destinations()
        self.assertTrue(
            len(result) == 0,
            "The destination should not have been created as it has invalid data",
        )

    def test_get_all_destinations(self):
        data = MockDataWrapper()
        destination_logic = DestinationLogic(data)

        for dest in self.MOCK_DESTINATIONS:
            data.create_destination(dest)

        destination_list = []
        for dest in destination_logic.get_all_destinations():
            dest.id = None
            destination_list.append(dest)

        self.assertListEqual(
            destination_list,
            self.MOCK_DESTINATIONS,
            "get_all_destinations should have returned all the destinations with the same data",
        )

    def test_get_destination(self):
        data = MockDataWrapper()
        destination_logic = DestinationLogic(data)

        for dest in self.MOCK_DESTINATIONS:
            data.create_destination(dest)

        counter = 0

        for dest in self.MOCK_DESTINATIONS:
            result = destination_logic.get_destination(counter)
            counter += 1
            result.id = None

            self.assertEqual(
                result,
                dest,
                "get_destination should have given the destinations back with the same data",
            )

    def test_update_destination_country(self):
        data = MockDataWrapper()
        destination_logic = DestinationLogic(data)

        for dest in self.MOCK_DESTINATIONS:
            data.create_destination(dest)

        for dest in data.get_all_destinations():
            dest.country = "TEST"
            destination_logic.update_destination(dest)

        for dest in data.get_all_destinations():
            self.assertNotEqual(
                dest.country,
                "TEST",
                "Country should not have changed. It should be immutable",
            )

    def test_update_destination_airport(self):
        data = MockDataWrapper()
        destination_logic = DestinationLogic(data)

        for dest in self.MOCK_DESTINATIONS:
            data.create_destination(dest)

        for dest in data.get_all_destinations():
            dest.airport = "TEST"
            destination_logic.update_destination(dest)

        for dest in data.get_all_destinations():
            self.assertNotEqual(
                dest.airport,
                "TEST",
                "Airport should not have changed. It should be immutable",
            )

    def test_update_destination_distance(self):
        data = MockDataWrapper()
        destination_logic = DestinationLogic(data)

        for dest in self.MOCK_DESTINATIONS:
            data.create_destination(dest)

        for dest in data.get_all_destinations():
            dest.distance_km = 314321432431
            destination_logic.update_destination(dest)

        for dest in data.get_all_destinations():
            self.assertNotEqual(
                dest.distance_km,
                314321432431,
                "Distance should not have changed. It should be immutable",
            )

    def test_update_destination_flight_time(self):
        data = MockDataWrapper()
        destination_logic = DestinationLogic(data)

        for dest in self.MOCK_DESTINATIONS:
            data.create_destination(dest)

        for dest in data.get_all_destinations():
            dest.flight_time = 314321432431
            destination_logic.update_destination(dest)

        for dest in data.get_all_destinations():
            self.assertNotEqual(
                dest.flight_time,
                314321432431,
                "Flight time should not have changed. It should be immutable",
            )

    def test_update_destination_representetive(self):
        data = MockDataWrapper()
        destination_logic = DestinationLogic(data)

        for dest in self.MOCK_DESTINATIONS:
            data.create_destination(dest)

        counter = 0

        for dest in data.get_all_destinations():
            dest.representative = ""
            dest.id = counter
            destination_logic.update_destination(dest)
            counter += 1

        for dest in data.get_all_destinations():
            self.assertEqual(
                dest.representative, "", "Representative should have been changed"
            )

    def test_update_destination_emergency_number(self):
        data = MockDataWrapper()
        destination_logic = DestinationLogic(data)

        for dest in self.MOCK_DESTINATIONS:
            data.create_destination(dest)

        for dest in data.get_all_destinations():
            dest.emergency_number = ""
            destination_logic.update_destination(dest)

        for dest in data.get_all_destinations():
            self.assertEqual(
                dest.emergency_number, "", "Emergency number should have been changed"
            )

    def test_delete_destination(self):
        data = MockDataWrapper()
        destination_logic = DestinationLogic(data)

        for dest in self.MOCK_DESTINATIONS:
            data.create_destination(dest)

        id_to_remove = 0
        destination_logic.delete_destination(id_to_remove)
        expect = None

        result = data.get_destination(0)

        self.assertEqual(
            expect,
            result,
            f"Element with id of {id_to_remove} should have been removed",
        )
