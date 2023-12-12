import unittest
import datetime
from logic.flight_logic import *
from .mock_data_wrapper import MockDataWrapper
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

        date = datetime.date.today()
        flight_logic.create_flight(0, 1, date, datetime.time(1, 00))

        res = data.get_flight("NA010", date)
        expect = Flight(
            flight_number="NA010",
            departure=0,
            destination=1,
            date=date,
            departure_time=datetime.time(1, 00),
            arrival_time=datetime.time(4, 20),
        )

        self.assertIsNotNone(res)
        self.assertEqual(res, expect)

    def test_create_flight_invalid_departure(self):
        data = MockDataWrapper()
        flight_logic = FlightLogic(data)

        data.create_destination(self.MOCK_DESTINATIONS[0])
        data.create_destination(self.MOCK_DESTINATIONS[1])

        date = datetime.date.today()
        flight_logic.create_flight(9, 1, date, datetime.time(1, 00))

        self.assertIsNone(data.get_flight("NA010", date))

    def test_create_flight_invalid_arrival(self):
        data = MockDataWrapper()
        flight_logic = FlightLogic(data)

        data.create_destination(self.MOCK_DESTINATIONS[0])
        data.create_destination(self.MOCK_DESTINATIONS[1])

        date = datetime.date.today()
        flight_logic.create_flight(0, -1, date, datetime.time(1, 00))

        self.assertIsNone(data.get_flight("NA010", date))

    def test_create_multiple_valid_flights(self):
        data = MockDataWrapper()
        flight_logic = FlightLogic(data)

        data.create_destination(self.MOCK_DESTINATIONS[0])
        data.create_destination(self.MOCK_DESTINATIONS[1])

        date = datetime.date.today()

        flight_logic.create_flight(0, 1, date, datetime.time(1, 00))
        flight_logic.create_flight(1, 0, date, datetime.time(1, 30))
        flight_logic.create_flight(0, 1, date, datetime.time(2, 00))

        flight1 = data.get_flight("NA010", date)
        self.assertIsNotNone(flight1)
        self.assertEqual(flight1, Flight(
            flight_number="NA010",
            departure=0,
            destination=1,
            date=date,
            departure_time=datetime.time(1, 00),
            arrival_time=datetime.time(4, 20),
        ))
        
        flight2 = data.get_flight("NA011", date)
        self.assertIsNotNone(flight2)
        self.assertEqual(flight2, Flight(
            flight_number="NA011",
            departure=1,
            destination=0,
            date=date,
            departure_time=datetime.time(1, 30),
            arrival_time=datetime.time(4, 50),
        ))

        flight3 = data.get_flight("NA012", date)
        self.assertIsNotNone(flight3)
        self.assertEqual(flight3, Flight(
            flight_number="NA012",
            departure=0,
            destination=1,
            date=date,
            departure_time=datetime.time(2, 00),
            arrival_time=datetime.time(5, 20),
        ))

    def test_create_flight_nr(self):
        data = MockDataWrapper()
        flight_logic = FlightLogic(data)

        data.create_destination(self.MOCK_DESTINATIONS[0])
        data.create_destination(self.MOCK_DESTINATIONS[1])

        date = datetime.datetime.now()

        for i in range(20):
            loc_id = i % 2
            flight_number = flight_logic.create_flight_nr(loc_id, 1 - loc_id, date)
            self.assertEqual(f"NA01{i}", flight_number)

            data.create_flight(Flight(
                flight_number=flight_number,
                departure=0,
                destination=1,
                date=date,
                departure_time=datetime.time(12, 30),
                arrival_time=datetime.time(15, 00),
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
            date=datetime.date(2023, 12, 4),
            departure_time=datetime.time(12, 30),
            arrival_time=datetime.time(13, 30),
        ))
        data.create_flight(Flight(
            flight_number="NA011",
            departure=0,
            destination=1,
            date=datetime.date(2023, 12, 4),
            departure_time=datetime.time(16, 50),
            arrival_time=datetime.time(17, 35),
        ))
        data.create_flight(Flight(
            flight_number="NA010",
            departure=0,
            destination=1,
            date=datetime.date(2023, 12, 6),
            departure_time=datetime.time(5, 20),
            arrival_time=datetime.time(7, 40),
        ))

        res = flight_logic.get_same_date_flights(1, datetime.date(2023, 12, 4))
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
                date=datetime.date(2023, 12, 4),
                departure_time=datetime.time(15, 00),
                arrival_time=datetime.time(16, 00),
            ),
            Flight(
                flight_number="NA011",
                departure=0,
                destination=1,
                date=datetime.date(2023, 12, 4),
                departure_time=datetime.time(19, 00),
                arrival_time=datetime.time(22, 00),
            ),
        ]
        for flight in flights:
            data.create_flight(flight)

        data.create_flight(Flight(
            flight_number="NA010",
            departure=0,
            destination=2,
            date=datetime.date(2023, 12, 6),
            departure_time=datetime.time(13, 00),
            arrival_time=datetime.time(16, 00),
        ))

        res = flight_logic.flights_going_to(1)
        self.assertEqual(len(flights), len(res))
    
    def test_calculate_arrival_time(self):
        data = MockDataWrapper()
        flight_logic = FlightLogic(data)

        data.create_destination(self.MOCK_DESTINATIONS[0])
        data.create_destination(self.MOCK_DESTINATIONS[1])

        departure = datetime.datetime(2023, 10, 25, 0, 0)
        arrival = flight_logic.calculate_arrival_time(departure.date(), departure.time(), 1)

        self.assertEqual(arrival, datetime.datetime(2023, 10, 25, 3, 20))
    
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
                date=datetime.date(2023, 12, 4),
                departure_time=datetime.time(8, 00),
                arrival_time=datetime.time(10, 00),
            ),
            Flight(
                flight_number="NA011",
                departure=0,
                destination=1,
                date=datetime.date(2023, 12, 4),
                departure_time=datetime.time(10, 00),
                arrival_time=datetime.time(13, 00),
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
                date=datetime.date(2023, 12, 4),
                departure_time=datetime.time(15, 00),
                arrival_time=datetime.time(18, 30),
            ),
            Flight(
                flight_number="NA011",
                departure=0,
                destination=1,
                date=datetime.date(2023, 12, 4),
                departure_time=datetime.time(19, 00),
                arrival_time=datetime.time(21, 00),
            ),
        ]

        data.create_flight(flights[0])
        data.create_flight(flights[1])

        self.assertEqual(flights[1], flight_logic.get_flight("NA011", datetime.date(2023, 12, 4)))

    def test_update_flight(self):
        data = MockDataWrapper()
        flight_logic = FlightLogic(data)

        data.create_destination(self.MOCK_DESTINATIONS[0])
        data.create_destination(self.MOCK_DESTINATIONS[1])

        flight = Flight(
            flight_number="NA010",
            departure=0,
            destination=1,
            date=datetime.date(2023, 12, 4),
            departure_time=datetime.time(19, 00),
            arrival_time=datetime.time(23, 00),
        )

        data.create_flight(flight)
        flight.departure = -1
        flight.destination = -1
        flight.date = datetime.date(1, 1, 1)
        flight.departure_time=datetime.time(1, 1)
        flight.arrival_time=datetime.time(1, 1)

        # TODO: Wouldn't there be able to exist multiple flights with the same 
        # flight number or would the flight be deleted after it has concluded
        flight_logic.update_flight("NA010", flight)
        self.assertNotEqual(data.get_first_flight().departure, -1)
        self.assertNotEqual(data.get_first_flight().destination, -1)
        self.assertNotEqual(data.get_first_flight().date, datetime.date(1, 1, 1))
        self.assertEqual(data.get_first_flight().departure_time, datetime.time(1, 1))
        self.assertEqual(data.get_first_flight().arrival_time, datetime.time(1, 1))
    
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
            date=datetime.date(2023, 12, 4),
            departure_time=datetime.time(15, 00),
            arrival_time=datetime.time(16, 00),
        )

        data.create_flight(flight)

        flight_logic.assign_pilot(self, pilot, flight)
        flight_logic.assign_pilot(self, manager, flight)

        raise NotImplementedError()


