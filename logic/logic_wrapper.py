# import os
from logic.employee_logic import EmployeeLogic
from logic.flight_logic import FlightLogic
from logic.destination_logic import DestinationLogic
from logic.voyage_logic import VoyageLogic
from logic.plane_logic import PlaneLogic
from logic.logic_utilities import Validator
from logic.logic_utilities import Utilities

from model.destination import Destination
from model.employee import Employee
from model.flight import Flight
from model.flight_attendant import FlightAttendant
from model.flight_manager import FlightManager
from model.manager import Manager
from model.pilot import Pilot
from model.plane import Plane
from model.voyage import Voyage

from data.data_wrapper import DataWrapper


class LogicWrapper(object):
    """This is the logic wrapper class. It is used to call the logic layer classes"""

    def __init__(self):
        """Constructor for LogicWrapper"""
        self.data_wrapper = DataWrapper()
        self.employee_logic = EmployeeLogic(self.data_wrapper)
        self.flight_logic = FlightLogic(self.data_wrapper)
        self.destination_logic = DestinationLogic(self.data_wrapper)
        self.voyage_logic = VoyageLogic(self.data_wrapper)
        self.plane_logic = PlaneLogic(self.data_wrapper)
        self.validate = Validator()
        self.utility = Utilities()

    # Employee Class
    def create_employee(self, employee) -> None:
        """Takes in a employee object and forwards it to the create_employee function"""
        return self.employee_logic.create_employee(employee)

    def get_all_employees(self) -> list[Employee]:
        """For wards list of employees from logic"""
        return self.employee_logic.get_all_employees()

    def get_employee(self, id) -> Employee:
        """Returns a employee with input ID"""
        return self.employee_logic.get_employee(id)

    def get_employee_by_email(self, email) -> Employee:
        """Fetches a employee with input email"""
        return self.employee_logic.get_employee_by_email(email)

    def get_employees_by_job(self, job) -> list:
        """Fetches a list of employees that fit the job title"""
        return self.employee_logic.get_employees_by_job(job)

    def get_all_pilots(self) -> list:
        """Fetches all pilots and returns them in a list"""
        return self.get_all_pilots()

    def get_pilots_by_liscense(self, liscense) -> list:
        """Retrieves a list of pilots which have the given liscense"""
        return self.get_pilots_by_liscense(liscense)

    def get_all_flight_attendants(self) -> list:
        """Fetches all pilots and returns them in a list"""
        return self.get_employees_by_job("FlightAttendants")

    def update_employee(self, employee) -> None:
        """Updates info about a employee"""
        return self.employee_logic.update_employee(employee)

    def delete_employee(self, id) -> None:
        """Erases an employee from the record/ via ID"""
        return self.employee_logic.delete_employee(id)

    def is_employee_manager(self, employee):
        """Checks if the given employee is a manager"""
        return self.employee_logic.is_employee_manager(employee)

    def is_employee_flight_manager(self, employee):
        """Check if a given employee is a flight manager"""
        return self.employee_logic.is_employee_flight_manager(employee)

    # Flight Class
    def create_flight(self, data) -> None:
        """Creates an flight"""
        return self.flight_logic.create_flight(data)

    def get_all_flight(self) -> list[Flight]:  # Flight route
        """Returns a list of all flight routes"""
        return self.flight_logic.get_all_flights()

    def get_flight(self, id) -> Flight:  # Flight route
        """Returns a specific flight route/ via ID"""
        return self.flight_logic.get_flight(id)

    def update_flight(self, id, data) -> None:
        """Updates info on flight routes"""
        return self.flight_logic.update_flight(id, data)

    def delete_flight(self, id) -> None:
        """Erases a flight"""
        return self.flight_logic.delete_flight(id)

    def assign_pilot(self, id, pilot) -> None:
        """Assigns pilot to a flight"""
        return self.flight_logic.assign_pilot(id, pilot)

    # Voyage Class
    def create_voyage(self, data) -> None:
        """Creates a voyage"""
        return self.voyage_logic.create_voyage(data)

    def get_all_voyages(self) -> list:
        """Returns a list of all current voyages"""
        return self.voyage_logic.get_all_voyages()

    def get_voyage(self, id) -> list[Destination]:
        """Returns a voyage/ via ID"""
        return self.voyage_logic.get_voyage(id)

    def update_voyage(self, voyage) -> None:
        """Updates info on voyage"""
        return self.voyage_logic.update_voyage(voyage)

    def delete_voyage(self, id) -> None:
        """Erases voyage/ via ID"""
        return self.voyage_logic.delete_voyage(id)

    # Destination class
    def create_destination(self, data) -> None:
        """Creates a new destination"""
        return self.destination_logic.create_destination(data)

    def get_all_destinations(self) -> list[Destination]:
        """Returns a list of all destinations"""
        return self.destination_logic.get_all_destinations()

    def get_destination(self, id) -> Destination:
        """Returns a Destination/ via ID"""
        return self.destination_logic.get_destination(id)

    def update_destination(self, destination) -> None:
        """Updates information about a destination"""
        return self.destination_logic.update_destination(destination)

    def delete_destination(self, id) -> None:
        """Erases a destination"""
        return self.destination_logic.delete_destination(id)

    # Plane Class
    def create_plane(self, data) -> None:
        """Creates a plane in the system"""
        return self.plane_logic.create_plane(data)

    def get_all_planes(self) -> list[Plane]:
        """Returns a list of all planes"""
        return self.plane_logic.get_all_planes()

    def get_plane(self, id) -> Plane:
        """Returns a plane/ via ID"""
        return self.plane_logic.get_plane(id)

    def update_plane(self, id) -> None:
        """updates information on plane"""
        return self.plane_logic.update_plane(id)

    def delete_plane(self, id) -> None:
        """Erases plane from the data"""
        return self.plane_logic.delete_plane(id)

    # Validator class
    ## General validation
    def validate_phone_number(self, phone_nr_data):
        """"""
        return self.validate.phone_number(phone_nr_data)

    def validate_date(self, date_data):
        """w.i.p"""
        return self.validate.date(date_data)

    ## Destination Validation

    ## Employee Validation
    def validate_ssn(self, ssn_data):
        return self.validate.ssn(ssn_data)

    def validate_email(self, email_data):
        return self.validate.email(email_data)

    ### Pilot Validation
    def validate_liscense(self, liscense_data):
        return self.validate.liscense(liscense_data)

    ### Pilot & Flight Attendant Validation
    def validate_assignments(self, assignments_data):
        return self.validate.assignments(assignments_data)

    # Voyage Validation
    def seats_available(self, voyage_data):
        return self.validate.seats_available(voyage_data)

    def validate_job_position(self, employee_list, job_title):
        return self.validate.job_position(employee_list, job_title)

    def validate_status(self, status_data):
        return self.validate.status(status_data)

    ### Utilities
    # Password Utility
    def password_encoder(self, password):
        return self.utility.password_encoder(password)

    def check_password(self, email, given_password):
        employee = self.employee_logic.get_employee_by_email(email)
        return self.utility.check_password(employee, given_password)
