import unittest
from datetime import timedelta, datetime
from logic.flight_logic import *
from test.mock_data_wrapper import MockDataWrapper
from model import *

class TestFlight(unittest.TestCase):
    MOCK_DESTINATIONS = [
        Destination(
            country="Reykjavik",
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

    def test_create_flight_valid(self):
        data = MockDataWrapper()
        flight_logic = FlightLogic(data)

        data.create_destination(self.MOCK_DESTINATIONS[0])
        data.create_destination(self.MOCK_DESTINATIONS[1])

        date = datetime.now()
        flight_logic.create_flight(0, 1, date, "01:00")

        self.assertIsNotNone(data.get_flight(0))
        self.assertEqual(data.get_flight(0), Flight(
            flight_number="NA010",
            departure=0,
            destination=1,
            date=date,
            departure_time="01:00",
            arrival_time="04:20",
        ))

    def test_create_flight_invalid_departure(self):
        data = MockDataWrapper()
        flight_logic = FlightLogic(data)

        data.create_destination(self.MOCK_DESTINATIONS[0])
        data.create_destination(self.MOCK_DESTINATIONS[1])

        date = datetime.now()
        flight_logic.create_flight(9, 1, date, "01:00")

        self.assertIsNone(data.get_flight(0))

    def test_create_flight_invalid_arrival(self):
        data = MockDataWrapper()
        flight_logic = FlightLogic(data)

        data.create_destination(self.MOCK_DESTINATIONS[0])
        data.create_destination(self.MOCK_DESTINATIONS[1])

        date = datetime.now()
        flight_logic.create_flight(0, -1, date, "01:00")

        self.assertIsNone(data.get_flight(0))

    def test_create_flight_invalid_time(self):
        data = MockDataWrapper()
        flight_logic = FlightLogic(data)

        data.create_destination(self.MOCK_DESTINATIONS[0])
        data.create_destination(self.MOCK_DESTINATIONS[1])

        date = datetime.now()
        flight_logic.create_flight(0, 1, date, "0:-01")

        self.assertIsNone(data.get_flight(0))

    def test_create_multiple_valid_flights(self):
        data = MockDataWrapper()
        flight_logic = FlightLogic(data)

        data.create_destination(self.MOCK_DESTINATIONS[0])
        data.create_destination(self.MOCK_DESTINATIONS[1])

        date = datetime.now()

        flight_logic.create_flight(0, 1, date, "01:00")
        flight_logic.create_flight(1, 0, date, "01:30")
        flight_logic.create_flight(0, 1, date, "02:00")

        self.assertIsNotNone(data.get_flight(0))
        self.assertEqual(data.get_flight(0), Flight(
            flight_number="NA010",
            departure=0,
            destination=1,
            date=date,
            departure_time="01:00",
            arrival_time="04:20",
        ))
        
        self.assertIsNotNone(data.get_flight(1))
        self.assertEqual(data.get_flight(1), Flight(
            flight_number="NA011",
            departure=0,
            destination=1,
            date=date,
            departure_time="01:30",
            arrival_time="04:50",
        ))

        self.assertIsNotNone(data.get_flight(2))
        self.assertEqual(data.get_flight(2), Flight(
            flight_number="NA012",
            departure=0,
            destination=1,
            date=date,
            departure_time="02:00",
            arrival_time="05:20",
        ))

    def test_create_flight_nr(self):
        data = MockDataWrapper()
        flight_logic = FlightLogic(data)

        data.create_destination(self.MOCK_DESTINATIONS[0])
        data.create_destination(self.MOCK_DESTINATIONS[1])

        date = datetime.now()

        for i in range(20):
            loc_id = i % 2
            flight_number = flight_logic.create_flight_nr(loc_id, 1 - loc_id, date)
            self.assertEqual(f"NA01{i}", flight_number)

            data.create_flight(Flight(
                flight_number=flight_number,
                departure=0,
                destination=1,
                date=date,
                departure_time="",
                arrival_time="",
            ))
    
    def test_get_same_date_flights(self):
        data = MockDataWrapper()
        flight_logic = FlightLogic(data)

        data.create_destination(self.MOCK_DESTINATIONS[0])
        data.create_destination(self.MOCK_DESTINATIONS[1])
        
        data.create_flight(Flight(
            flight_number="NA010",
            departure=0,
            destination=1,
            date=datetime(2023, 12, 4, 15, 00),
            departure_time="",
            arrival_time="",
        ))
        data.create_flight(Flight(
            flight_number="NA011",
            departure=0,
            destination=1,
            date=datetime(2023, 12, 4, 19, 00),
            departure_time="",
            arrival_time="",
        ))
        data.create_flight(Flight(
            flight_number="NA010",
            departure=0,
            destination=1,
            date=datetime(2023, 12, 6, 13, 00),
            departure_time="",
            arrival_time="",
        ))

        res = flight_logic.get_same_date_flights(1, datetime(2023, 12, 4))
        self.assertEqual(res, 2)
    
    def test_flights_going_to(self):
        data = MockDataWrapper()
        flight_logic = FlightLogic(data)

        data.create_destination(self.MOCK_DESTINATIONS[0])
        data.create_destination(self.MOCK_DESTINATIONS[1])
        
        flights = [
            Flight(
                flight_number="NA010",
                departure=0,
                destination=1,
                date=datetime(2023, 12, 4, 15, 00),
                departure_time="",
                arrival_time="",
            ),
            Flight(
                flight_number="NA011",
                departure=0,
                destination=1,
                date=datetime(2023, 12, 4, 19, 00),
                departure_time="",
                arrival_time="",
            ),
        ]
        data.create_flight(Flight(
            flight_number="NA010",
            departure=1,
            destination=0,
            date=datetime(2023, 12, 6, 13, 00),
            departure_time="",
            arrival_time="",
        ))

        res = flight_logic.flights_going_to()
        raise NotImplementedError()
    
    def test_calculate_arrival_time(self):
        data = MockDataWrapper()
        flight_logic = FlightLogic(data)

        data.create_destination(self.MOCK_DESTINATIONS[0])
        data.create_destination(self.MOCK_DESTINATIONS[1])

        # TODO: Should this take datetime in instead
        #self.assertEqual(flight_logic.calculate_arrival_time("03:20", 1), timedelta(hours=))
        raise NotImplementedError()
    
    def test_add_staff_to_flights(self):
        raise NotImplementedError()

    def test_get_all_flights(self):
        data = MockDataWrapper()
        flight_logic = FlightLogic(data)

        data.create_destination(self.MOCK_DESTINATIONS[0])
        data.create_destination(self.MOCK_DESTINATIONS[1])
        
        flights = [
            Flight(
                flight_number="NA010",
                departure=0,
                destination=1,
                date=datetime(2023, 12, 4, 15, 00),
                departure_time="",
                arrival_time="",
            ),
            Flight(
                flight_number="NA011",
                departure=0,
                destination=1,
                date=datetime(2023, 12, 4, 19, 00),
                departure_time="",
                arrival_time="",
            ),
        ]

        data.create_flight(flights[0])
        data.create_flight(flights[1])

        self.assertListEqual(flights, flight_logic.get_all_flight())

    def test_get_flight(self):
        data = MockDataWrapper()
        flight_logic = FlightLogic(data)

        data.create_destination(self.MOCK_DESTINATIONS[0])
        data.create_destination(self.MOCK_DESTINATIONS[1])
        
        flights = [
            Flight(
                flight_number="NA010",
                departure=0,
                destination=1,
                date=datetime(2023, 12, 4, 15, 00),
                departure_time="",
                arrival_time="",
            ),
            Flight(
                flight_number="NA011",
                departure=0,
                destination=1,
                date=datetime(2023, 12, 4, 19, 00),
                departure_time="",
                arrival_time="",
            ),
        ]

        data.create_flight(flights[0])
        data.create_flight(flights[1])

        self.assertEqual(flights[1], flight_logic.get_flight("NA011"))

    def test_update_flight(self):
        data = MockDataWrapper()
        flight_logic = FlightLogic(data)

        data.create_destination(self.MOCK_DESTINATIONS[0])
        data.create_destination(self.MOCK_DESTINATIONS[1])

        flight = Flight(
            flight_number="NA010",
            departure=0,
            destination=1,
            date=datetime(2023, 12, 4, 15, 00),
            departure_time="",
            arrival_time="",
        )

        data.create_flight(flight)
        flight.departure = -1
        flight.destination = -1
        flight.date = datetime(1, 1, 1)
        flight.departure_time="TEST"
        flight.arrival_time="TEST"

        # TODO: Wouldn't there be able to exist multiple flights with the same 
        # flight number or would the flight be deleted after it has concluded
        flight_logic.update_flight("NA010", flight)
        self.assertNotEqual(data.get_first_flight().departure, -1)
        self.assertNotEqual(data.get_first_flight().destination, -1)
        self.assertNotEqual(data.get_first_flight().date, datetime(1, 1, 1))
        self.assertEqual(data.get_first_flight().departure_time, "TEST")
        self.assertEqual(data.get_first_flight().arrival_time, "TEST")

    def test_delete_flight(self):
        data = MockDataWrapper()
        flight_logic = FlightLogic(data)

        data.create_destination(self.MOCK_DESTINATIONS[0])
        data.create_destination(self.MOCK_DESTINATIONS[1])

        data.create_flight(Flight(
            flight_number="NA010",
            departure=0,
            destination=1,
            date=datetime(2023, 12, 4, 15, 00),
            departure_time="",
            arrival_time="",
        ))

        flight_logic.delete_flight("NA010", "what...?")
        raise NotImplementedError
    
    def test_assign_pilot(self):
        data = MockDataWrapper()
        flight_logic = FlightLogic(data)

        data.create_destination(self.MOCK_DESTINATIONS[0])
        data.create_destination(self.MOCK_DESTINATIONS[1])

        pilot = Pilot(
            id=0,
            name="John",
            password=None,
            address=None,
            ssn=None,
            mobile_phone=None,
            email=None,
            home_phone=None,
            license="C750",
        )
        manager = Manager(
            id=0,
            name="John",
            password=None,
            address=None,
            ssn=None,
            mobile_phone=None,
            email=None,
            home_phone=None,
            work_phone=None,
        )
        data.create_employee(pilot)
        data.create_employee(manager)

        flight = Flight(
            flight_number="NA010",
            departure=0,
            destination=1,
            date=datetime(2023, 12, 4, 15, 00),
            departure_time="",
            arrival_time="",
        )

        data.create_flight(flight)

        flight_logic.assign_pilot(self, pilot, flight)
        flight_logic.assign_pilot(self, manager, flight)

        raise NotImplementedError()


