from validator_logic import Validator


class EmployeeLogic:
    """This class is the logic layer for the employee class"""

    def __init__(self, data_connection):
        self.data_wrapper = data_connection
        self.validate = Validator()

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
        is_ssn_valid = self.validate.ssn(employee.ssn)
        is_mobile_phone_valid = self.validate.phone_number(employee.mobile_phone)
        is_email_valid = self.validate.email(employee.email)
        is_home_phone_valid = self.validate.phone_number(employee.home_phone)
