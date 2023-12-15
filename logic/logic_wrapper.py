# import os
from logic import (
    Validator,
    Utilities,
    PlaneLogic,
    VoyageLogic,
    DestinationLogic,
    FlightLogic,
    EmployeeLogic,
    PlaneUtilities,
    VoyageUtilities,
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
    PlaneStatus,
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
        self.plane_logic = PlaneLogic(self.data_wrapper)
        self.plane_utilities = PlaneUtilities(self.data_wrapper)
        self.voyage_utilities = VoyageUtilities(self.data_wrapper)
        self.validate = Validator()
        self.utility = Utilities()

    # Employee Class
    def create_employee(self, employee: Employee) -> None:
        """Takes in a employee object and forwards it to the create_employee function"""
        return self.employee_logic.create_employee(employee)

    def get_all_employees(self) -> list[Employee]:
        """For wards list of employees from logic"""
        return self.employee_logic.get_all_employees()

    def get_employee(self, id: int) -> Employee:
        """Returns a employee with input ID"""
        return self.employee_logic.get_employee(id)

    def get_employee_by_email(self, email: str) -> list[Employee]:
        """Fetches a employee with input email"""
        return self.employee_logic.get_employee_by_email(email)

    def get_employees_by_job(self, job: str) -> list[Employee]:
        """Fetches a list of employees that fit the job title"""
        return self.employee_logic.get_employees_by_job(job)

    def get_employee_by_workday(self, date: datetime) -> list[Employee]:
        """Retrieves a list of employees that are working on a specific date"""
        return self.employee_logic.get_employee_by_workday(date)

    def is_working(self, employee_id: int, date: datetime) -> bool:
        """Checks and returns if employee is working on given date"""
        return self.employee_logic.is_working(employee_id, date)

    def get_employee_by_not_workday(self, date: datetime) -> list[Employee]:
        """Retrieves a list of employees that are working on a specific date"""
        return self.employee_logic.get_employee_by_not_workday(date)

    def get_all_pilots(self) -> list[Pilot]:
        """Fetches all pilots and returns them in a list"""
        return self.get_all_pilots()

    def get_pilots_by_license(self, license: str) -> list[Pilot]:
        """Retrieves a list of pilots which have the given license"""
        return self.get_pilots_by_license(license)

    def get_all_flight_attendants(self) -> list[Pilot]:
        """Fetches all pilots and returns them in a list"""
        return self.get_employees_by_job("FlightAttendants")

    def update_employee(self, employee: Employee) -> None:
        """Updates info about a employee"""
        return self.employee_logic.update_employee(employee)

    def delete_employee(self, id: int) -> None:
        """Erases an employee from the record/ via ID"""
        return self.employee_logic.delete_employee(id)

    # Flight Class
    def create_flight(self, data: Flight) -> None:
        """Creates an flight"""
        return self.flight_logic.create_flight(data)

    def get_all_flight(self) -> list[Flight]:  # Flight
        """Returns a list of all flight routes"""
        return self.flight_logic.get_all_flights()

    def get_flight(self, flight_number: str, date: datetime.date) -> Flight:  # Flight
        """Returns a specific flight route/ via ID"""
        return self.flight_logic.get_flight(flight_number, date)

    def update_flight(self, id: int, data: Flight) -> None:
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
        return self.voyage_utilities.create_voyage(
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

    def get_all_voyages(self) -> list[Voyage]:
        """Returns a list of all current voyages"""
        return self.voyage_logic.get_all_voyages()

    def get_voyage(self, id: int) -> Voyage:
        """Returns a voyage/ via ID"""
        return self.voyage_logic.get_voyage(id)

    def update_voyage(self, voyage: Voyage) -> None:
        """Updates info on voyage"""
        return self.voyage_logic.update_voyage(voyage)

    def delete_voyage(self, id: int) -> None:
        """Erases voyage/ via ID"""
        return self.voyage_utilities.delete_voyage(id)

    def validate_departure_time(
        self, departure_date: datetime.date, departure_time: datetime.time
    ) -> bool:
        """Validates that two flights dont depart at the same time"""
        return self.voyage_logic.validate_departure_time(departure_date, departure_time)

    def get_voyages_on_date(self, date: datetime.date) -> list[Voyage]:
        '''returns Voyage on given date'''
        return self.voyage_logic.get_voyage_by_date(date)

    # Destination class
    def create_destination(self, data: Destination) -> None:
        """Creates a new destination"""
        return self.destination_logic.create_destination(data)

    def get_all_destinations(self) -> list[Destination]:
        """Returns a list of all destinations"""
        return self.destination_logic.get_all_destinations()

    def get_destination(self, id: int) -> Destination:
        """Returns a Destination/ via ID"""
        return self.destination_logic.get_destination(id)

    def update_destination(self, destination: Destination) -> None:
        """Updates information about a destination"""
        return self.destination_logic.update_destination(destination)

    def delete_destination(self, id: int) -> None:
        """Erases a destination"""
        return self.destination_logic.delete_destination(id)

    # Plane Class
    def create_plane(self, data: Plane) -> None:
        """Creates a plane in the system"""
        return self.plane_logic.create_plane(data)

    def get_all_planes(self) -> list[Plane]:
        """Returns a list of all planes"""
        return self.plane_logic.get_all_planes()

    def get_plane(self, id: int) -> Plane:
        """Returns a plane/ via ID"""
        return self.plane_logic.get_plane(id)

    def update_plane(self, id: int) -> None:
        """updates information on plane"""
        return self.plane_logic.update_plane(id)

    def delete_plane(self, id: int) -> None:
        """Erases plane from the data"""
        return self.plane_logic.delete_plane(id)

    # Validator class
    ## General validation
    def validate_phone_number(self, phone_nr_data: str) -> bool:
        """Validates phonenumber and returns bool"""
        return self.validate.phone_number(phone_nr_data)

    ## Destination Validation

    ## Employee Validation
    def validate_ssn(self, ssn_data: str) -> bool:
        '''Validates ssn (social security number)'''
        return self.validate.ssn(ssn_data)

    def validate_email(self, email_data: str) -> bool:
        '''validates email returns bool'''
        return self.validate.email(email_data)

    ### Pilot Validation
    def validate_license(self, license_data: str) -> bool:
        '''validates licens and returns bool'''
        return self.validate.license(self.data_wrapper, license_data)

    def pilot_has_license(self, pilot_id: int, plane_id: int) -> bool:
        '''validate if pilot has license and returns bool'''
        return self.employee_logic.pilot_has_license(pilot_id, plane_id)

    ### Pilot & Flight Attendant Validation
    def validate_assignments(self, assignments_data: list[int]) -> bool:
        '''Validate assignments and returns bool'''
        return self.validate.assignments(assignments_data)

    # Voyage Validation
    def seats_available(self, voyage_data: Voyage) -> bool:
        '''Validates available seats and returns bool'''
        return self.validate.seats_available(voyage_data)

    def check_job_position(self, employee_id: int, job_title: str) -> bool:
        '''Validates job position and returns bool'''
        return self.employee_logic.check_job_position(employee_id, job_title)

    def validate_voyage_staff(self, voyage: Voyage):
        '''Validates Voyage'''
        return self.validate.voyage_staff(voyage)

    def validate_status(self, voyage: Voyage) -> None:
        '''Validates status of Voyage'''
        return self.voyage_logic.validate_status(voyage)

    def voyage_contains_date_and_time(self, voyage: Voyage, date: datetime.date, time: datetime.time ) -> bool:
        '''Checks if voyage has datetime.date'''
        return self.voyage_logic.contains_date_and_time(voyage, date, time)

    def voyage_contains_overlap(self, voyage1: Voyage, voyage2: Voyage) -> bool:
        '''Validates if there is an overlap'''
        return self.voyage_logic.contains_overlap(voyage1, voyage2)

    ### Utilities
    # Password Utility
    def password_encoder(self, password: str) -> str:
        '''Encodes password using bcrypt'''
        return self.utility.password_encoder(password)

    def check_password(self, email: str, given_password: str) -> bool:
        '''Checks password and returns bool'''
        employee = self.employee_logic.get_employee_by_email(email)
        return self.utility.check_password(employee, given_password)

    # Voyage Utilities

    def staff_voyage_pilot(self, voyage_id: int, new_staff: int) -> None:
        '''adds pilot to voyage'''
        return self.voyage_utilities.staff_voyage_pilot(voyage_id, new_staff)

    def staff_voyage_attendant(self, voyage_id: int, new_staff: int) -> None:
        '''adds attendant to voyage'''
        return self.voyage_utilities.staff_voyage_attendant(voyage_id, new_staff)

    def unstaff_voyage_pilot(self, voyage_id, staff_to_remove: int) -> None:
        '''Removes pilot from voyage'''
        return self.voyage_utilities.unstaff_voyage_pilot(voyage_id, staff_to_remove)

    def unstaff_voyage_attendant(self, voyage_id, staff_to_remove: int) -> None:
        '''Removes attendant from voyage'''
        return self.voyage_utilities.unstaff_voyage_attendant(voyage_id, staff_to_remove)

    # Plane Utilities

    def get_plane_status(self, plane: Plane) -> PlaneStatus:
        '''Gets plane status'''
        return self.plane_utilities.get_plane_status(plane)

    def get_plane_active_flight(self, plane: Plane) -> Flight | None:
        '''gets current flight if plane is on any active voyages'''
        return self.plane_utilities.get_plane_active_flight(plane)

    def get_plane_active_voyage(self, plane: Plane) -> Voyage | None:
        '''gets current Voyage if plane is on any active voyages'''
        return self.plane_utilities.get_plane_active_voyage(plane)

    def validate_plane_availability(self, plane: Plane, when: datetime.datetime) -> bool:
        '''validate if plane is available and returns bool'''
        return self.plane_utilities.validate_plane_availability(plane, when)

    # General Utilities

    def make_datetime(
        self, date: datetime.date, time: datetime.time
    ) -> datetime.datetime:
        '''Makes datetime'''
        return Utilities.make_datetime(date, time)
