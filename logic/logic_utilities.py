import datetime
import bcrypt

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
            compacted_number = phone_number[0:3] + phone_number[4:8]
            int(compacted_number)
            return True

        except (ValueError, IndexError):
            return False

    def date(self, date) -> bool:
        """Takes in a date and returns
        valid(True) or Invalid(False)"""

        # Think that Datetime module has this as a feature

    def distance_km(self, km) -> bool:
        """"""
        try:
            return int(km) > 0

        except ValueError:
            return False

    def flight_time(self, time) -> bool:
        """"""
        try:
            return int(time) > 0

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

        if century == "9":
            year = "19" + year

        elif century == "0":
            year = "20" + year

        else:
            year = "INVALID"  # This is done to make the ssn not pass the datetime check

        try:
            int(ssn)  # Checks if the ssn only contains numbers
            datetime.date(
                int(year), int(month), int(day)
            )  # Check if it is a valid time
            return True

        except ValueError:
            return False

    def email(self, email):
        """Checks if the given email is an email"""
        email = email.split("@")

        try:
            email[1] = email[1].split(".")

            if "" in email or "" in email[1]:
                raise Exception("One of the email fields is empty")
            return True

        except (IndexError, Exception):
            return False

    # Pilot and flight attendant validations
    def liscense(self, liscense) -> bool:
        """uhhhhhh w.I.p"""
        pass

    def assignments(self, assignments) -> bool:
        """???"""
        pass

    # Flight validation

    # Plane validation

    # Voyage Validations
    def seats_available(self, voyage) -> bool:
        """Checks if seats are available
        in the voyage"""
        plane_seats = voyage.plane.capacity
        available_seats = plane_seats - voyage.sold_seats
        return 1 > available_seats

    def job_position(self, employee_list, job_title) -> bool:
        """Goes through a list of employees and verifies
        if all of them are the given job_title"""
        for employee in employee_list:
            if type(employee).__name__ != job_title:
                return False

        return True

    def flight_times(self, voyage) -> bool:
        """Compares the times and check
        if they do not cause conflicts"""
        flight_times = [
            voyage.departure_flight.departure_time,
            voyage.departure_flight.arrival_time,
            voyage.departure_flight.departure_time,
            voyage.deprature_flight.arrival_time,
        ]
        are_flight_times_valid = False  # W.i.P

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

    def flight_number_validator(self, data):
        """Validates flight plans and assignes a flight number"""

        voyages_list = self.data_wrapper.get_all_voyages()
        flights_list = self.data_wrapper.get_all_flights()

        if data.arrival_flight.day == flights_list[-1].arrival_flight.day:
            voyage_num += 1

        else:
            voyage_num = 0

        data.flight_number = f"NA0{data.destination}{voyage_num}"

    def validate_voyage(self, voyage) -> Voyage:
        """Validates a voyage and return a validated
        voyage if possible, else None"""
        are_seats_available = self.validate.seats_available(voyage)
        are_pilots_valid = self.validate.job_position(voyage.pilots, "Pilot")
        are_attendants_valid = self.validate.job_position(
            voyage.flight_attendants, "FlightAttendant"
        )


class Utilities:
    """A class which contains
    a bunch of logic utilities"""

    def password_encoder(self, password):
        """Takes in a password and encodes it"""
        encoded_password = password.encode("utf-8")
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(encoded_password, salt)
        return hashed_password

    def check_password(self, hashed_password, given_password):
        """Takes in a password check if it is the password."""
        inputted_password = given_password.encode("utf-8")
        result = bcrypt.checkpw(inputted_password, hashed_password)
        return result
