import unittest
from logic.voyage_logic import *
from test.mock_data_wrapper import MockDataWrapper
import datetime
from model import *

class TestVoyage(unittest.TestCase):
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

    MOCK_PLANES = [
        Plane(
            name="Terminator",
            ty="737",
            manufacturer="Boeing",
            capacity=300,
        ),
        Plane(
            name="Terminator 2",
            ty="A320",
            manufacturer="Airbus",
            capacity=350,
        ),
        Plane(
            name="Terminator",
            ty="777",
            manufacturer="Boeing",
            capacity=250,
        ),
    ]

    def test_create_voyage_valid(self):
        data = MockDataWrapper()
        voyage_logic = VoyageLogic(data)

        data.create_plane(self.MOCK_PLANES[0])
        data.create_destination(self.MOCK_DESTINATIONS[0])
        data.create_destination(self.MOCK_DESTINATIONS[1])

        voyage_logic.create_voyage(
            0, # Plane id
            1, # Destination
            datetime.date(2023, 2, 15), # Date
            datetime.date(2023, 2, 16), # Return departure date
            datetime.time(15, 00), # Departure time
            datetime.time(12, 00), # Return departure time
            150,
            [],
            []
        )

        voyage = data.get_first_voyage()
        self.assertIsNotNone(voyage)
        self.assertEqual(voyage.sold_seats, 150)
        self.assertEqual(voyage.departure_time, datetime.time(15, 00))
        self.assertEqual(voyage.departure_flight, "NA010")
        self.assertEqual(voyage.arrival_departure_time, datetime.time(12, 00))
        self.assertEqual(voyage.arrival_flight, "NA010")
        self.assertEqual(voyage.date, datetime.date(2023, 2, 15))
        self.assertEqual(voyage.return_date, datetime.date(2023, 2, 16))
        self.assertEqual(voyage.status, VoyageStatus.NotStarted)

    def test_create_same_day_voyage_valid(self):
        data = MockDataWrapper()
        voyage_logic = VoyageLogic(data)

        data.create_plane(self.MOCK_PLANES[0])
        data.create_destination(self.MOCK_DESTINATIONS[0])
        data.create_destination(self.MOCK_DESTINATIONS[1])

        voyage_logic.create_voyage(
            0, # Plane id
            1, # Destination
            datetime.date(2023, 2, 15), # Date
            datetime.date(2023, 2, 15), # Return departure date
            datetime.time(15, 00), # Departure time
            datetime.time(17, 00), # Return departure time
            150,
            [],
            []
        )

        voyage = data.get_first_voyage()
        self.assertIsNotNone(voyage)
        self.assertEqual(voyage.sold_seats, 150)
        self.assertEqual(voyage.departure_time, datetime.time(15, 00))
        self.assertEqual(voyage.departure_flight, "NA010")
        self.assertEqual(voyage.arrival_departure_time, datetime.time(17, 00))
        self.assertEqual(voyage.arrival_flight, "NA011")
        self.assertEqual(voyage.date, datetime.date(2023, 2, 15))
        self.assertEqual(voyage.return_date, datetime.date(2023, 2, 15))
        self.assertEqual(voyage.status, VoyageStatus.NotStarted)
