from logic.logic_utilities import Validator

VALIDATION_ERRORS = (
    "Invalid SSN. ",
    "Invalid Phone Number. ",
    "Invalid Email. ",
    "Invalid Home Number. ",
)


class EmployeeLogic:
    """This class is the logic layer for the employee class"""

    def __init__(self, data_connection):
        self.data_wrapper = data_connection
        self.validate = Validator()

    def create_employee(self, employee):
        """Takes in a employee object and forwards it to the data layer"""
        return self.data_wrapper.create_employee(employee)

    def list_all_employees(self) -> list:
        """Returns a list of all employees"""
        employee_list = self.data_wrapper.get_all_employees()
        # Sorting and tomfoolery
        return employee_list

    def get_employee(self, id):
        """Returns a employee object with the given id"""
        employee_list = self.list_all_employees

        pass

    def get_employee_by_email(self, email):
        """Returns a employee object with the given id"""
        employee = self.data_wrapper.get_employee_by_email(email)

        pass

    def get_employee_by_job(self, email):
        """Returns a employee object with the given id"""
        employee = self.data_wrapper.get_employee_by_email(email)

        pass

    def update_employee(self, employee):
        """Updates a employee object with the given id"""
        return self.data_wrapper.update_employee(employee)

    def delete_employee(self, id):
        """Deletes a employee object with the given id"""
        return self.data_wrapper.delete_employee(id)
