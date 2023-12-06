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
        """Validates a given employee and returns
        an validated version of the given employee"""

    def validate_email(self, email):
        """Checks if the given email is an email"""
        if "@" not in email or "." not in email:
            return False
        return True

    def validate_ssn(self, ssn):
        day, month, year = ssn[0:2], ssn[2:4], ssn[4:6]
        try:
            datetime.date(day, month, year)
            return True
        except ValueError:
            return False

    def validate_phone_number(self, phone_number):
        pass


#
#
#
#
