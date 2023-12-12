import unittest
from logic.employee_logic import *
from test.mock_data_wrapper import MockDataWrapper
from model import *

class TestEmployee(unittest.TestCase):

    # MOCK_MANAGERS = [
    #    Manager(
    #         name="Bob",
    #         password="",
    #         # TODO: Incomplete
    #     )
    # ]
    MOCK_FLIGHT_MANAGERS = []
    MOCK_PILOTS = []
    MOCK_FLIGHT_ATTENDANTS = []

    VOYAGE_TEMPLATE = Voyage(
        destination=0,
        sold_seats=0,
        plane=None,
        pilots=[],
        flight_attendants=[],
        departure_time=datetime(1, 1, 1),
        departure_flight=0,
        arrival_departure_time=datetime(1, 1, 1),
        arrival_flight=0,
        date=datetime(1, 1, 1),
        return_date=datetime(1, 1, 1),
        status=""
    )
    

    def test_create_employee_manager_valid(self):
        pass

    def test_create_employee_manager_invalid_work_phone(self):
        pass

    def test_create_employee_flight_manager_valid(self):
        pass

    def test_create_employee_flight_manager_invalid_work_phone(self):
        pass

    def test_create_employee_flight_attendant_valid(self):
        pass

    def test_create_employee_flight_attendant_invalid_assignments(self):
        pass

    def test_create_employee_pilot_valid(self):
        pass

    def test_create_employee_pilot_invalid_assignments(self):
        pass

    def test_create_employee_pilot_invalid_license(self):
        pass
