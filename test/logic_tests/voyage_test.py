import unittest
from logic.voyage_logic import *
from .mock_data_wrapper import MockDataWrapper
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
        )

        voyage = data.get_first_voyage()
        self.assertIsNotNone(voyage)
        self.assertEqual(voyage.sold_seats, 150)
        self.assertEqual(voyage.departure_time, datetime.time(15, 00))
        self.assertEqual(voyage.departure_flight, "NA010")
        self.assertEqual(voyage.return_departure_time, datetime.time(12, 00))
        self.assertEqual(voyage.return_flight, "NA010")
        self.assertEqual(voyage.departure_date, datetime.date(2023, 2, 15))
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
        )

        voyage = data.get_first_voyage()
        self.assertIsNotNone(voyage)
        self.assertEqual(voyage.sold_seats, 150)
        self.assertEqual(voyage.departure_time, datetime.time(15, 00))
        self.assertEqual(voyage.departure_flight, "NA010")
        self.assertEqual(voyage.return_departure_time, datetime.time(17, 00))
        self.assertEqual(voyage.return_flight, "NA011")
        self.assertEqual(voyage.departure_date, datetime.date(2023, 2, 15))
        self.assertEqual(voyage.return_date, datetime.date(2023, 2, 15))
        self.assertEqual(voyage.status, VoyageStatus.NotStarted)
    
    # Outdated test - Does not run
    def test_get_all_voyages(self):
        data = MockDataWrapper()
        voyage_logic = VoyageLogic(data)

        data.create_plane(self.MOCK_PLANES[0])
        data.create_destination(self.MOCK_DESTINATIONS[0])
        data.create_destination(self.MOCK_DESTINATIONS[1])

        voyages = [
            Voyage(
                id=0,
                destination=1,
                sold_seats=100,
                plane=0,
                departure_time=datetime.time(1, 20),
                departure_flight="FA010",
                departure_date=datetime.date(2023, 10, 5),
                return_departure_time=datetime.time(1, 20),
                return_flight="FA010",
                return_date=datetime.date(2023, 10, 8),
                status=VoyageStatus.Finished,
            ),
            Voyage(
                id=1,
                destination=1,
                sold_seats=228,
                plane=0,
                departure_time=datetime.time(9, 50),
                departure_flight="FA010",
                departure_date=datetime.date(2023, 11, 15),
                return_departure_time=datetime.time(1, 20),
                return_flight="FA010",
                return_date=datetime.date(2023, 11, 19),
                status=VoyageStatus.Finished,
            )
        ]

        data.create_voyage(voyages[0])
        data.create_voyage(voyages[1])

        res = voyage_logic.get_all_voyages()
        self.assertListEqual(voyages, res)


    # Outdated test - Does not run
    def test_get_voyage(self):
        data = MockDataWrapper()
        voyage_logic = VoyageLogic(data)

        data.create_plane(self.MOCK_PLANES[0])
        data.create_destination(self.MOCK_DESTINATIONS[0])
        data.create_destination(self.MOCK_DESTINATIONS[1])

        voyages = [
            Voyage(
                id=0,
                destination=1,
                sold_seats=100,
                plane=0,
                departure_time=datetime.time(1, 20),
                departure_flight="FA010",
                departure_date=datetime.date(2023, 10, 5),
                return_departure_time=datetime.time(1, 20),
                return_flight="FA010",
                return_date=datetime.date(2023, 10, 8),
                status=VoyageStatus.Finished,
            ),
            Voyage(
                id=1,
                destination=1,
                sold_seats=228,
                plane=0,
                departure_time=datetime.time(9, 50),
                departure_flight="FA010",
                departure_date=datetime.date(2023, 11, 15),
                return_departure_time=datetime.time(1, 20),
                return_flight="FA010",
                return_date=datetime.date(2023, 11, 19),
                status=VoyageStatus.Finished,
            )
        ]

        data.create_voyage(voyages[0])
        data.create_voyage(voyages[1])

        voyage = voyage_logic.get_voyage(1)
        self.assertEqual(voyage, voyages[1])

    # Outdated test - Does not run
    def test_update_voyage(self):
        data = MockDataWrapper()
        voyage_logic = VoyageLogic(data)

        data.create_plane(self.MOCK_PLANES[0])
        data.create_destination(self.MOCK_DESTINATIONS[0])
        data.create_destination(self.MOCK_DESTINATIONS[1])

        voyage = Voyage(
            id=0,
            destination=1,
            sold_seats=100,
            plane=0,
            departure_time=datetime.time(1, 20),
            departure_flight="FA010",
            departure_date=datetime.date(2023, 10, 5),
            return_departure_time=datetime.time(1, 20),
            return_flight="FA010",
            return_date=datetime.date(2023, 10, 8),
            pilots=[],
            flight_attendants=[],
            status=VoyageStatus.Finished,
        )

        data.create_voyage(voyage)

        data.create_employee(Pilot(
            name="",
            password="",
            address="",
            ssn="",
            mobile_phone="",
            email="",
            home_phone=None,
            license="",
        ))

        voyage.destination = 9
        voyage.sold_seats = 150
        voyage.plane = 5
        voyage.departure_time = datetime.time(3, 40)
        voyage.departure_flight = "FA011"
        voyage.departure_date = datetime.date(2023, 10, 8)
        voyage.return_departure_time = datetime.time(9, 20)
        voyage.return_flight = "FA011"
        voyage.return_date = datetime.date(2023, 10, 10)
        voyage.status = VoyageStatus.LandedAbroad
        voyage.pilots = [0]
        voyage.flight_attendants = [1, 2]

        voyage_logic.update_voyage(voyage)

        result = data.get_first_voyage()
        self.assertNotEqual(result.destination, 9)
        self.assertEqual(result.sold_seats, 150)
        self.assertNotEqual(result.plane, 5)
        self.assertNotEqual(result.departure_time, datetime.time(3, 40))
        self.assertNotEqual(result.departure_flight, "FA011")
        self.assertNotEqual(result.departure_date, datetime.date(2023, 10, 8))
        self.assertNotEqual(result.return_departure_time, datetime.time(9, 20))
        self.assertNotEqual(result.return_flight, "FA011")
        self.assertNotEqual(result.return_date, datetime.date(2023, 10, 10))
        self.assertNotEqual(result.status, VoyageStatus.LandedAbroad)
        self.assertListEqual(result.pilots, [0])
        self.assertListEqual(result.flight_attendants, [])

    def test_delete_voyage(self):
        data = MockDataWrapper()
        voyage_logic = VoyageLogic(data)

        data.create_plane(self.MOCK_PLANES[0])
        data.create_destination(self.MOCK_DESTINATIONS[0])
        data.create_destination(self.MOCK_DESTINATIONS[1])

        voyages = [
            Voyage(
                id=0,
                destination=1,
                sold_seats=100,
                plane=0,
                departure_time=datetime.time(1, 20),
                departure_flight="FA010",
                departure_date=datetime.date(2023, 10, 5),
                return_departure_time=datetime.time(1, 20),
                return_flight="FA010",
                return_date=datetime.date(2023, 10, 8),
                status=VoyageStatus.Finished,
            ),
            Voyage(
                id=1,
                destination=1,
                sold_seats=228,
                plane=0,
                departure_time=datetime.time(9, 50),
                departure_flight="FA010",
                departure_date=datetime.date(2023, 11, 15),
                return_departure_time=datetime.time(1, 20),
                return_flight="FA010",
                return_date=datetime.date(2023, 11, 19),
                status=VoyageStatus.Finished,
            )
        ]

        data.create_voyage(voyages[0])
        data.create_voyage(voyages[1])

        voyage_logic.delete_voyage(0)

        voyages.remove(voyages[0])

        self.assertListEqual(voyages, data.get_all_voyages())
