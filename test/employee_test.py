import unittest
from logic.employee_logic import *
from test.mock_data_wrapper import MockDataWrapper
from model import *

class TestEmployee(unittest.TestCase):

    MOCK_MANAGERS = [
       Manager(
            name="Bob",
            password="123bobistheman",
            address="bobstreet",
            ssn="1112231239",
            mobile_phone="123-1234",
            email="bobtm@nanair.is",
            home_phone="464-4213",
            work_phone="321-3213",
        ),
        Manager(
            name="John",
            password="1234",
            address="45 John St.",
            ssn="1112233219",
            mobile_phone="919-",
            email="jonn@nanair.is",
            home_phone=None,
            work_phone="912-3213",
        )
    ]
    MOCK_FLIGHT_MANAGERS = [
       FlightManager(
            name="Steve",
            password="abc",
            address="99 St. St.",
            ssn="1112237829",
            mobile_phone="712-6342",
            email="steve@nanair.is",
            home_phone=None,
            work_phone="444-4444",
        ),
        FlightManager(
            name="Peter",
            password="4321",
            address="22 Pete St.",
            ssn="1112238889",
            mobile_phone="765-4321",
            email="peter@nanair.is",
            home_phone="623-1346",
            work_phone="919-9191",
        )
    ]
    MOCK_PILOTS = [
       Pilot(
            name="George",
            password="securityexpert",
            address="12 George Av.",
            ssn="1112232569",
            mobile_phone="612-6342",
            email="george@nanair.is",
            home_phone="916-2345",
            assignments=[],
            license="C750",
        ),
        Pilot(
            name="Tom",
            password="AAAAAAA",
            address="8 Tom Blvd.",
            ssn="1112237779",
            mobile_phone="765-4321",
            email="tom@nanair.is",
            home_phone=None,
            assignments=[],
            license="C150",
        )
    ]
    MOCK_FLIGHT_ATTENDANTS = [
       FlightAttendant(
            name="Geoff",
            password="creativitydeclining",
            address="1 Geoff Park",
            ssn="1112231119",
            mobile_phone="211-2111",
            email="geoff@nanair.is",
            home_phone=None,
            assignments=[],
        ),
        FlightAttendant(
            name="Lois",
            password="BBBBBBB",
            address="8 Lois Blvd.",
            ssn="1112236549",
            mobile_phone="853-2135",
            email="lois@nanair.is",
            home_phone="421-6423",
            assignments=[],
        )
    ]

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
    
    MOCK_EMPLOYEES = []
    
    def setUp(self):
        self.MOCK_EMPLOYEES.clear()
        self.MOCK_EMPLOYEES.extend(self.MOCK_MANAGERS)
        self.MOCK_EMPLOYEES.extend(self.MOCK_FLIGHT_MANAGERS)
        self.MOCK_EMPLOYEES.extend(self.MOCK_PILOTS)
        self.MOCK_EMPLOYEES.extend(self.MOCK_FLIGHT_ATTENDANTS)

    def test_create_employee_invalid_ssn(self):
        raise NotImplementedError

    def test_create_employee_invalid_mobile_phone(self):
        raise NotImplementedError

    def test_create_employee_invalid_email(self):
        raise NotImplementedError

    def test_create_employee_invalid_home_phone(self):
        raise NotImplementedError

    def test_create_employee_manager_valid(self):
        raise NotImplementedError

    def test_create_employee_manager_invalid_work_phone(self):
        raise NotImplementedError

    def test_create_employee_flight_manager_valid(self):
        raise NotImplementedError

    def test_create_employee_flight_manager_invalid_work_phone(self):
        raise NotImplementedError

    def test_create_employee_flight_attendant_valid(self):
        raise NotImplementedError

    def test_create_employee_flight_attendant_invalid_assignments(self):
        raise NotImplementedError

    def test_create_employee_pilot_valid(self):
        raise NotImplementedError

    def test_create_employee_pilot_invalid_assignments(self):
        raise NotImplementedError

    def test_create_employee_pilot_invalid_license(self):
        raise NotImplementedError

    def test_get_all_employees(self):
        raise NotImplementedError

    def test_get_employee(self):
        raise NotImplementedError

    def test_get_employee_by_email(self):
        raise NotImplementedError

    def test_get_employee_by_job(self):
        raise NotImplementedError

    def test_get_all_pilots(self):
        raise NotImplementedError

    def test_get_pilots_by_license(self):
        raise NotImplementedError

    def test_update_employee_valid(self):
        raise NotImplementedError
    
    def test_update_employee_invalid_ssn(self):
        raise NotImplementedError
    
    def test_update_employee_invalid_mobile_phone(self):
        raise NotImplementedError

    def test_update_employee_invalid_email(self):
        raise NotImplementedError

    def test_update_employee_invalid_home_phone(self):
        raise NotImplementedError

    def test_update_employee_invalid_job(self):
        raise NotImplementedError

    def test_update_manager_valid(self):
        raise NotImplementedError

    def test_update_manager_invalid_work_phone(self):
        raise NotImplementedError

    def test_update_flight_manager_valid(self):
        raise NotImplementedError

    def test_update_flight_manager_invalid_work_phone(self):
        raise NotImplementedError

    def test_update_pilot_invalid_assignments(self):
        raise NotImplementedError

    def test_update_pilot_invalid_license(self):
        raise NotImplementedError

    def test_update_flight_attendant_valid(self):
        raise NotImplementedError

    def test_update_flight_attendant_invalid_assignments(self):
        raise NotImplementedError

    def test_delete_employee(self):
        raise NotImplementedError

    def test_is_employee_manager(self):
        raise NotImplementedError

    def test_is_employee_flight_manager(self):
        raise NotImplementedError

