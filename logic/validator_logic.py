import datetime


class Validator:
    """Class which handles.
    validation and return either
    true or false, or a valid version"""

    def __init__(self):
        """Empty init"""

    # General validation
    def phone_number(self, phone_number) -> bool:
        """Takes in a phonenumber and returns
        if it is valid(True) or invalid(False)"""

        try:
            compacted_number = phone_number[0:3] + phone_number[4:8]
            int(compacted_number)
            return True
        except ValueError:
            return False

    def date(self, date) -> bool:
        """Takes in a date and returns
        valid(True) or Invalid(False)"""

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
        if "@" not in email or "." not in email:
            return False
        return True

    # Pilot and flight attendant validations
    def liscense(self, liscense) -> bool:
        """uhhhhhh w.I.p"""
        pass

    def assignments(self, assignments) -> bool:
        """???"""
        pass

    # Voyage Validations
    def job_position(self, employee_list, job_title) -> bool:
        """Goes through a list of employees and verifies
        if all of them are the given job_title"""
        for employee in employee_list:
            if type(employee).__name__ != job_title:
                return False
        return True

    def status(self, status) -> bool:
        """Validates the status, returns either
        valid(True) or invalid(False)"""
        if status is not "Good":
            return "This is really bad"
        return "YAHOO!!"
