import unittest
import datetime
from logic.employee_logic import *
from .mock_data_wrapper import MockDataWrapper
from model import *
from copy import deepcopy


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
            mobile_phone="919-2934",
            email="jonn@nanair.is",
            home_phone=None,
            work_phone="912-3213",
        ),
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
        ),
    ]
    MOCK_PILOTS = [
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
        ),
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
        ),
    ]

    VOYAGE_TEMPLATE = Voyage(
        destination=0,
        sold_seats=0,
        plane=None,
        pilots=[],
        flight_attendants=[],
        departure_time=datetime.time(1, 1, 1),
        departure_flight=0,
        return_departure_time=datetime.time(1, 1, 1),
        return_flight=0,
        departure_date=datetime.date(1, 1, 1),
        return_date=datetime.date(1, 1, 1),
        status="",
    )

    MOCK_EMPLOYEES = []

    def setUp(self):
        self.MOCK_EMPLOYEES.clear()
        self.MOCK_EMPLOYEES.extend(self.MOCK_MANAGERS)
        self.MOCK_EMPLOYEES.extend(self.MOCK_FLIGHT_MANAGERS)
        self.MOCK_EMPLOYEES.extend(self.MOCK_PILOTS)
        self.MOCK_EMPLOYEES.extend(self.MOCK_FLIGHT_ATTENDANTS)

    def test_create_employee_invalid_ssn(self):
        data = MockDataWrapper()
        employee_logic = EmployeeLogic(data)

        employee = deepcopy(self.MOCK_EMPLOYEES[1])
        employee.ssn = "asa124839"

        employee_logic.create_employee(employee)
        self.assertIsNone(data.get_first_employee())

    def test_create_employee_invalid_mobile_phone(self):
        data = MockDataWrapper()
        employee_logic = EmployeeLogic(data)

        employee = deepcopy(self.MOCK_EMPLOYEES[1])
        employee.mobile_phone = "asd-1234"

        employee_logic.create_employee(employee)
        self.assertIsNone(data.get_first_employee())

    def test_create_employee_invalid_email(self):
        data = MockDataWrapper()
        employee_logic = EmployeeLogic(data)

        employee = deepcopy(self.MOCK_EMPLOYEES[1])
        employee.email = "asd1234.@asd"

        employee_logic.create_employee(employee)
        self.assertIsNone(data.get_first_employee())

    def test_create_employee_invalid_home_phone(self):
        data = MockDataWrapper()
        employee_logic = EmployeeLogic(data)

        employee = deepcopy(self.MOCK_EMPLOYEES[1])
        employee.home_phone = "asd-1234"

        employee_logic.create_employee(employee)
        self.assertIsNone(data.get_first_employee())

    def test_create_employee_manager_valid(self):
        data = MockDataWrapper()
        employee_logic = EmployeeLogic(data)

        employee_logic.create_employee(self.MOCK_MANAGERS[0])
        self.assertIsNotNone(data.get_first_employee())

    def test_create_employee_manager_invalid_work_phone(self):
        data = MockDataWrapper()
        employee_logic = EmployeeLogic(data)

        employee = deepcopy(self.MOCK_MANAGERS[0])
        employee.work_phone = "asd-1234"

        employee_logic.create_employee(employee)
        self.assertIsNone(data.get_first_employee())

    def test_create_employee_flight_manager_valid(self):
        data = MockDataWrapper()
        employee_logic = EmployeeLogic(data)

        employee_logic.create_employee(self.MOCK_FLIGHT_MANAGERS[0])
        self.assertIsNotNone(data.get_first_employee())

    def test_create_employee_flight_manager_invalid_work_phone(self):
        data = MockDataWrapper()
        employee_logic = EmployeeLogic(data)

        employee = deepcopy(self.MOCK_FLIGHT_MANAGERS[0])
        employee.work_phone = "asd-1234"

        employee_logic.create_employee(employee)
        self.assertIsNone(data.get_first_employee())

    def test_create_employee_flight_attendant_valid(self):
        data = MockDataWrapper()
        employee_logic = EmployeeLogic(data)

        employee_logic.create_employee(self.MOCK_FLIGHT_ATTENDANTS[0])
        self.assertIsNotNone(data.get_first_employee())

    def test_create_employee_flight_attendant_invalid_assignments(self):
        data = MockDataWrapper()
        employee_logic = EmployeeLogic(data)

        employee = deepcopy(self.MOCK_FLIGHT_ATTENDANTS[0])
        employee.assignments = [9, 2, 2]

        employee_logic.create_employee(employee)
        self.assertIsNone(data.get_first_employee())

    def test_create_employee_pilot_valid(self):
        data = MockDataWrapper()
        employee_logic = EmployeeLogic(data)

        data.create_plane(
            Plane(
                name="",
                ty="C750",
                manufacturer="",
                capacity=0,
            )
        )
        data.create_plane(
            Plane(
                name="",
                ty="C150",
                manufacturer="",
                capacity=0,
            )
        )

        employee_logic.create_employee(self.MOCK_PILOTS[0])
        self.assertIsNotNone(data.get_first_employee())

    def test_create_employee_pilot_invalid_assignments(self):
        data = MockDataWrapper()
        employee_logic = EmployeeLogic(data)

        employee = deepcopy(self.MOCK_PILOTS[0])
        employee.assignments = [9, 2, 3, 2]

        employee_logic.create_employee(employee)
        self.assertIsNone(data.get_first_employee())

    def test_get_all_employees(self):
        data = MockDataWrapper()
        employee_logic = EmployeeLogic(data)

        for employee in self.MOCK_EMPLOYEES:
            data.create_employee(employee)

        employee_list = []
        for employee in employee_logic.get_all_employees():
            employee.id = None
            employee_list.append(employee)

        self.assertListEqual(self.MOCK_EMPLOYEES, employee_list)

    def test_get_employee(self):
        data = MockDataWrapper()
        employee_logic = EmployeeLogic(data)

        for employee in self.MOCK_EMPLOYEES:
            data.create_employee(employee)

        gotten_employee = employee_logic.get_employee(5)
        gotten_employee.id = None

        self.assertEqual(self.MOCK_EMPLOYEES[5], gotten_employee)

    def test_get_employee_by_email(self):
        data = MockDataWrapper()
        employee_logic = EmployeeLogic(data)

        for employee in self.MOCK_EMPLOYEES:
            data.create_employee(employee)

        expect = self.MOCK_EMPLOYEES[5]
        gotten_employee = employee_logic.get_employee_by_email(expect.email)
        gotten_employee.id = None

        self.assertEqual(expect, gotten_employee)

    def test_get_employee_by_job(self):
        data = MockDataWrapper()
        employee_logic = EmployeeLogic(data)

        for employee in self.MOCK_EMPLOYEES:
            data.create_employee(employee)

        pilot_list = []
        gotten_pilots = employee_logic.get_employees_by_job("Pilot")
        for pilot in gotten_pilots:
            pilot.id = None
            pilot_list.append(pilot)

        self.assertListEqual(self.MOCK_PILOTS, pilot_list)

    def test_get_all_pilots(self):
        data = MockDataWrapper()
        employee_logic = EmployeeLogic(data)

        for employee in self.MOCK_EMPLOYEES:
            data.create_employee(employee)

        pilot_list = []
        for pilot in employee_logic.get_all_pilots():
            pilot.id = None
            pilot_list.append(pilot)

        self.assertListEqual(self.MOCK_PILOTS, pilot_list)

    def test_get_pilots_by_license(self):
        data = MockDataWrapper()
        employee_logic = EmployeeLogic(data)

        data.create_plane(
            Plane(
                name="",
                ty="C750",
                manufacturer="",
                capacity=0,
            )
        )
        data.create_plane(
            Plane(
                name="",
                ty="C150",
                manufacturer="",
                capacity=0,
            )
        )

        data.create_employee(self.MOCK_PILOTS[0])
        data.create_employee(self.MOCK_PILOTS[1])

        gotten_pilot = employee_logic.get_pilots_by_license("C750")
        gotten_pilot[0].id = None

        self.assertListEqual([self.MOCK_PILOTS[1]], gotten_pilot)

    def test_update_employee_valid(self):
        data = MockDataWrapper()
        employee_logic = EmployeeLogic(data)

        employee = deepcopy(self.MOCK_EMPLOYEES[0])
        data.create_employee(employee)

        prev_pw = employee.password

        employee.id = 0
        employee.address = "TEST"
        employee.password = "54321"
        employee.mobile_phone = "123-1234"
        employee.home_phone = "123-1234"
        employee.email = "test@test.test"
        employee_logic.update_employee(employee)

        self.assertEqual(data.get_first_employee().address, "TEST")
        self.assertNotEqual(data.get_first_employee().password, prev_pw)
        self.assertEqual(data.get_first_employee().mobile_phone, "123-1234")
        self.assertEqual(data.get_first_employee().home_phone, "123-1234")
        self.assertEqual(data.get_first_employee().email, "test@test.test")

    def test_update_employee_invalid_fields(self):
        data = MockDataWrapper()
        employee_logic = EmployeeLogic(data)

        employee = deepcopy(self.MOCK_EMPLOYEES[0])
        data.create_employee(employee)

        employee.ssn = "1112231239"
        employee.name = "Testman"
        employee_logic.update_employee(employee)

        self.assertNotEqual(data.get_first_employee().address, "TEST")

    def test_update_employee_invalid_mobile_phone(self):
        data = MockDataWrapper()
        employee_logic = EmployeeLogic(data)

        employee = deepcopy(self.MOCK_EMPLOYEES[0])
        data.create_employee(employee)

        employee.mobile_phone = "1vqr32-3"
        employee_logic.update_employee(employee)

        self.assertNotEqual(data.get_first_employee().mobile_phone, "1vqr32-3")

    def test_update_employee_invalid_email(self):
        data = MockDataWrapper()
        employee_logic = EmployeeLogic(data)

        employee = deepcopy(self.MOCK_EMPLOYEES[0])
        data.create_employee(employee)

        employee.email = "123"
        employee_logic.update_employee(employee)

        self.assertNotEqual(data.get_first_employee().email, "123")

    def test_update_employee_invalid_home_phone(self):
        data = MockDataWrapper()
        employee_logic = EmployeeLogic(data)

        employee = deepcopy(self.MOCK_EMPLOYEES[0])
        data.create_employee(employee)

        employee.home_phone = "521"
        employee_logic.update_employee(employee)

        self.assertNotEqual(data.get_first_employee().home_phone, "521")

    def test_update_manager_valid(self):
        data = MockDataWrapper()
        employee_logic = EmployeeLogic(data)

        employee = deepcopy(self.MOCK_MANAGERS[0])
        data.create_employee(employee)

        employee.work_phone = "123-1234"
        employee_logic.update_employee(employee)

        self.assertNotEqual(data.get_first_employee().work_phone, "123-1234")

    def test_update_manager_invalid_work_phone(self):
        data = MockDataWrapper()
        employee_logic = EmployeeLogic(data)

        employee = deepcopy(self.MOCK_MANAGERS[0])
        data.create_employee(employee)

        employee.work_phone = "612"
        employee_logic.update_employee(employee)

        self.assertNotEqual(data.get_first_employee().work_phone, "612")

    def test_update_flight_manager_valid(self):
        data = MockDataWrapper()
        employee_logic = EmployeeLogic(data)

        employee = deepcopy(self.MOCK_FLIGHT_MANAGERS[0])
        data.create_employee(employee)

        employee.work_phone = "123-1234"
        employee_logic.update_employee(employee)

        self.assertNotEqual(data.get_first_employee().work_phone, "123-1234")

    def test_update_flight_manager_invalid_work_phone(self):
        data = MockDataWrapper()
        employee_logic = EmployeeLogic(data)

        employee = deepcopy(self.MOCK_FLIGHT_MANAGERS[0])
        data.create_employee(employee)

        employee.work_phone = "612"
        employee_logic.update_employee(employee)

        self.assertNotEqual(data.get_first_employee().work_phone, "612")

    def test_update_pilot_valid(self):
        data = MockDataWrapper()
        employee_logic = EmployeeLogic(data)

        employee = deepcopy(self.MOCK_PILOTS[0])
        data.create_employee(employee)

        voyage = deepcopy(self.VOYAGE_TEMPLATE)
        data.create_voyage(voyage)

        data.create_plane(
            Plane(
                name="",
                ty="C750",
                manufacturer="",
                capacity=0,
            )
        )
        data.create_plane(
            Plane(
                name="",
                ty="C150",
                manufacturer="",
                capacity=0,
            )
        )

        employee.assignments = [0]
        employee.license = "C150"
        employee.id = 0
        employee_logic.update_employee(employee)

        self.assertListEqual(data.get_first_employee().assignments, [0])
        self.assertEqual(data.get_first_employee().license, "C150")

    def test_update_pilot_invalid_assignments(self):
        data = MockDataWrapper()
        employee_logic = EmployeeLogic(data)

        employee = deepcopy(self.MOCK_PILOTS[0])
        data.create_employee(employee)

        employee.assignments = [1, 9]
        employee_logic.update_employee(employee)

        self.assertListEqual(data.get_first_employee().assignments, [])

    def test_update_pilot_invalid_license(self):
        data = MockDataWrapper()
        employee_logic = EmployeeLogic(data)

        employee = deepcopy(self.MOCK_PILOTS[0])
        data.create_employee(employee)

        employee.id = 0
        employee.license = "C750"
        employee_logic.update_employee(employee)

        self.assertEqual(data.get_first_employee().license, "C750")

    def test_update_flight_attendant_valid(self):
        data = MockDataWrapper()
        employee_logic = EmployeeLogic(data)

        employee = deepcopy(self.MOCK_FLIGHT_ATTENDANTS[0])
        data.create_employee(employee)

        voyage = deepcopy(self.VOYAGE_TEMPLATE)
        data.create_voyage(voyage)

        employee.assignments = [0]
        employee.id = 0
        employee_logic.update_employee(employee)

        self.assertListEqual(data.get_first_employee().assignments, [0])

    def test_update_flight_attendant_invalid_assignments(self):
        data = MockDataWrapper()
        employee_logic = EmployeeLogic(data)

        employee = deepcopy(self.MOCK_FLIGHT_ATTENDANTS[0])
        data.create_employee(employee)

        employee.assignments = [0]
        employee_logic.update_employee(employee)

        self.assertListEqual(data.get_first_employee().assignments, [])

    def test_delete_employee(self):
        data = MockDataWrapper()
        employee_logic = EmployeeLogic(data)

        for employee in self.MOCK_EMPLOYEES:
            data.create_employee(employee)

        id_to_delete = 2
        employee_logic.delete_employee(id_to_delete)
        expect = None
        self.assertEqual(expect, data.get_employee(2))
