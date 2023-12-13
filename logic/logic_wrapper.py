# import os
from logic import (
    Validator,
    Utilities,
    PlaneLogic,
    VoyageLogic,
    DestinationLogic,
    FlightLogic,
    EmployeeLogic,
)
from model import (
    Destination,
    Employee,
    Flight,
    FlightAttendant,
    FlightManager,
    Manager,
    Pilot,
    Plane,
    Voyage,
)
from data.data_wrapper import DataWrapper
import datetime


class LogicWrapper(object):
    """This is the logic wrapper class. It is used to call the logic layer classes"""

    def __init__(self):
        """Constructor for LogicWrapper"""
        self.data_wrapper = DataWrapper()
        self.employee_logic = EmployeeLogic(self.data_wrapper)
        self.flight_logic = FlightLogic(self.data_wrapper)
        self.destination_logic = DestinationLogic(self.data_wrapper)
        self.voyage_logic = VoyageLogic(self.data_wrapper)
        self.plane_logic = PlaneLogic(self.data_wrapper, self.voyage_logic)
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

    def get_employee_by_email(self, email) -> list[Employee]:
        """Fetches a employee with input email"""
        return self.employee_logic.get_employee_by_email(email)

    def get_employees_by_job(self, job) -> list[Employee]:
        """Fetches a list of employees that fit the job title"""
        return self.employee_logic.get_employees_by_job(job)

    def get_employee_by_workday(self, date) -> list[Employee]:
        """Retrieves a list of employees that are working on a specific date"""
        return self.employee_logic.get_employee_by_workday(date)

    def get_employee_by_not_workday(self, date) -> list[Employee]:
        """Retrieves a list of employees that are working on a specific date"""
        return self.employee_logic.get_employee_by_not_workday(date)

    def get_all_pilots(self) -> list[Pilot]:
        """Fetches all pilots and returns them in a list"""
        return self.get_all_pilots()

    def get_pilots_by_license(self, license) -> list[Pilot]:
        """Retrieves a list of pilots which have the given license"""
        return self.get_pilots_by_license(license)

    def get_all_flight_attendants(self) -> list[Pilot]:
        """Fetches all pilots and returns them in a list"""
        return self.get_employees_by_job("FlightAttendants")

    def update_employee(self, employee) -> None:
        """Updates info about a employee"""
        return self.employee_logic.update_employee(employee)

    def delete_employee(self, id) -> None:
        """Erases an employee from the record/ via ID"""
        return self.employee_logic.delete_employee(id)

    # Flight Class
    def create_flight(self, data) -> None:
        """Creates an flight"""
        return self.flight_logic.create_flight(data)

    def get_all_flight(self) -> list[Flight]:  # Flight
        """Returns a list of all flight routes"""
        return self.flight_logic.get_all_flights()

    def get_flight(self, flight_number: str, date: datetime.date) -> Flight:  # Flight
        """Returns a specific flight route/ via ID"""
        return self.flight_logic.get_flight(flight_number, date)

    def update_flight(self, id, data) -> None:
        """Updates info on flight routes"""
        return self.flight_logic.update_flight(id, data)

    # Voyage Class
    def create_voyage(
        self,
        plane_id: int,
        destination_id: int,
        date: datetime.date,
        return_departure_date: datetime.date,
        departure_time: datetime.time,
        return_departure_time: datetime.time,
        sold_seats: int,
        flight_attendants: list[int],
        pilots: list[int],
    ) -> None:
        """Creates a voyage"""
        return self.voyage_logic.create_voyage(
            plane_id,
            destination_id,
            date,
            return_departure_date,
            departure_time,
            return_departure_time,
            sold_seats,
            flight_attendants,
            pilots,
        )

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
    def validate_license(self, license_data):
        return self.validate.license(self.data_wrapper, license_data)

    def pilot_has_license(self, pilot, plane):
        return self.validate.pilot_has_license(pilot, plane)

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

    def validate_voyage_staff(self, voyage):
        return self.validate.voyage_staff(voyage)

    ### Utilities
    # Password Utility
    def password_encoder(self, password):
        return self.utility.password_encoder(password)

    def check_password(self, email, given_password):
        employee = self.employee_logic.get_employee_by_email(email)
        return self.utility.check_password(employee, given_password)
