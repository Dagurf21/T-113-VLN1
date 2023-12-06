import datetime


class EmployeeLogic:
    """This class is the logic layer for the employee class"""

    def __init__(self, data_connection):
        self.data_wrapper = data_connection

    def create_employee(self, employee_data):
        """Takes in a employee object and forwards it to the data layer"""
        return self.data_wrapper.create_employee(employee_data)

    def list_all_employees(self) -> list:
        """Returns a list of all employees"""
        employee_list = self.data_wrapper.get_all_employees()
        # Sorting and tomfoolery
        return employee_list

    def list_employee(self, id):
        """Returns a employee object with the given id"""
        employee = self.data_wrapper.get_employee(id)
        # Commence sorting!
        return employee

    def get_employee(self, id):
        """Returns a employee object with the given id"""
        employee = self.data_wrapper.get_employee(id)
        # Commence sorting!
        return employee

    def get_employee_by_email(self, email):
        """Returns a employee object with the given id"""
        employee = self.data_wrapper.get_employee_by_email(email)
        # Commence sorting!
        return employee

    def update_employee(self, employee):
        """Updates a employee object with the given id"""
        return self.data_wrapper.update_employee(employee)

    def delete_employee(self, id):
        """Deletes a employee object with the given id"""
        return self.data_wrapper.delete_employee(id)

    def validate_employee(self, employee):
        """Validates a given employee"""
        is_ssn_valid = self.validate_ssn(employee.ssn)
        is_mobile_phone_valid = self.validate_phone_number(employee.mobile_phone)
        is_email_valid = self.validate_email(employee.email)
        is_home_phone_valid = self.validate_phone_number(employee.home_phone)

    def validate_ssn(self, ssn) -> bool:
        """Take in a social security number
        and returns True if it is valid and
        False if it is not valid.

        A SSN must follow the below conditions:
            1. It displays a valid date and time in the first numbers
            2. The last number must either be 9(19 century) or 0(20 century)
            3. The SSN should only contain numbers"""
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

    def validate_email(self, email):
        """Checks if the given email is an email"""
        if "@" not in email or "." not in email:
            return False
        return True

    def validate_phone_number(self, phone_number) -> bool:
        """Takes in a phonenumber and returns
        if it is valid(True) or invalid(False)"""

        try:
            compacted_number = phone_number[0:3] + phone_number[4:8]
            int(compacted_number)
            return True
        except ValueError:
            return False

    def validate_liscense(self, liscense) -> bool:
        """uhhhhhh w.I.p"""
        pass

    def verify_assignments(self, assignments) -> bool:
        """???"""
        pass


#
#
#
#
