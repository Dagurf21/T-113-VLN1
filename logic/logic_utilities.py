import datetime
import bcrypt
import re

from model import Voyage


class Validator:
    """Class which handles.
    validation and return either
    true or false, or a valid version"""

    # General validation
    def phone_number(self, phone_number) -> bool:
        """Takes in a phonenumber and returns
        if it is valid(True) or invalid(False)"""

        try:
            phone_number = phone_number.replace("-", "")
            if len(phone_number) != 7:
                raise IndexError
            compacted_number = phone_number[:3] + phone_number[-4:]
            int(compacted_number)
            return True

        except (ValueError, IndexError):
            return False

    def date(self, date) -> bool:
        """Takes in a date and returns
        valid(True) or Invalid(False)"""

        # Think that Datetime module has this as a feature

    def distance_km(self, km: int) -> bool:
        """Returns true if distance is not under zero"""
        try:
            return int(km) >= 0

        except ValueError:
            return False

    def flight_time(self, time: int) -> bool:
        """Returns true if time in minutes is not under zero"""
        try:
            return time >= 0

        except ValueError:
            return False


    # Employee validation
    def ssn(self, ssn) -> bool:
        """Take in a social security number
        and returns True if it is valid and
        False if it is not valid.

        A SSN must follow the below conditions:
            1. It displays a valid date and time in the first numbers
            2. The last number must either be 9(19 century) or 0(20 century)
            3. The SSN should only contain numbers
            4. Only contains 10 digits"""
        day, month, year, century = (
            ssn[0:2],
            ssn[2:4],
            ssn[4:6],
            ssn[-1],
        )

        if century > "5":
            year = "1" + century + year

        else:
            year = "2" + century + year

        try:
            if len(ssn) != 10:
                raise Exception("SSN too long or too short")
            int(ssn)  # Checks if the ssn only contains numbers
            datetime.date(
                int(year), int(month), int(day)
            )  # Check if it is a valid time
            return True

        except (ValueError, Exception):
            return False

    def email(self, email):
        """Checks if the given email is an email"""

        # Regex email validation
        #  [^@]+    Anything but @ symbol
        #  @        @ symbol
        #  [^@]+    Anything but @ synbol
        #  \.       . symbol
        #  [^@]+    Anything but @ symbol
        return re.match("[^@]+@[^@]+\.[^@]+", email)


    # Pilot and flight attendant validations
    def license(self, data_wrapper, planelicense) -> bool:
        """Verifies if the plane license is valid by getting the list of planes"""
        for plane in data_wrapper.get_all_planes():
            if planelicense == plane.ty:
                return True
        return False


    def pilot_has_license(self, pilot, plane):
        return pilot.license == plane.type


    def assignments(self, assignments) -> bool:
        """Validates the assignments
        for example, if the same assignment comes up twice"""
        cleaned_assignments = []
        
        for assignment in assignments:
            if assignment not in cleaned_assignments:
                cleaned_assignments.append(assignment)
        
        assignments.sort()
        cleaned_assignments.sort()

        is_same_assignment_twice = cleaned_assignments == assignments
        return is_same_assignment_twice

    # Flight validation

    # Plane validation

    # Voyage Validations
    def seats_available(self, voyage) -> bool:
        """Checks if seats are available
        in the voyage"""
        plane_seats = voyage.plane.capacity
        available_seats = plane_seats - voyage.sold_seats
        return 1 > available_seats


    def flight_times(self, voyage) -> bool:
        """Compares the times and check
        if they do not cause conflicts"""
        flight_times = [
            voyage.departure_flight.departure_time,
            voyage.departure_flight.arrival_time,
            voyage.departure_flight.departure_time,
            voyage.deprature_flight.arrival_time,
        ]
        return all(map(self.flight_time, flight_times))


    def status(self, status) -> bool:
        """Validates the status, returns either
        valid(True) or invalid(False)"""
        return False


    def pilot_validator(self, data):
        """Validates that there aren't to many pilots"""

        if len(data.get_all_flights.pilots) == 2:
            return False

        else:
            return True

    def voyage_staff(self, voyage) -> Voyage:
        """Validates a voyage and return a validated
        voyage if possible, else None"""
        are_pilots_valid = self.job_position(voyage.pilots, "Pilot")
        are_flight_attendants_valid = self.job_position(
            voyage.flight_attendants, "FlightAttendants"
        )
        return are_pilots_valid and are_flight_attendants_valid


class Utilities:
    """A class which contains
    a bunch of logic utilities"""

    def password_encoder(self, password):
        """Takes in a password and encodes it"""
        encoded_password = password.encode("utf-8")
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(encoded_password, salt)
        return hashed_password.decode("utf-8")

    def check_password(self, employee, given_password):
        """Takes in a password check if it is the password."""
        try:
            inputted_password = given_password.encode("utf-8")
            encoded_employee_password = employee.password.encode("utf-8")
            result = bcrypt.checkpw(inputted_password, encoded_employee_password)
            return result
        except ValueError:
            return None
