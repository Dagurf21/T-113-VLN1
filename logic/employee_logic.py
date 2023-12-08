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

    def create_employee(self, employee_data):
        """Takes in a employee object and forwards it to the data layer"""
        return self.data_wrapper.create_employee(employee)

    def list_all_employees(self) -> list:
        """Returns a list of all employees"""
        employee_list = self.data_wrapper.get_all_employees()
        return employee_list

    def get_employee(self, employee_id):
        """Returns the requested employee as the correct employee class type.
        If no employee with the id is found return None"""
        employee_list = self.list_all_employees()

        for employee in employee_list:
            if int(employee["id"]) == employee_id:
                return employee
        return None

    def get_employee_by_email(self, search_email):
        """Returns a employee object with the given id"""
        employee_list = self.list_all_employees()

        for employee in employee_list:
            if employee.email == search_email:
                return employee

    def get_employees_by_job(self, job_title):
        """Returns a employee object with the given id"""
        employee_list = self.list_all_employees()

        employees_with_the_job = []

        for employee in employee_list:
            if type(employee).__name__ == job_title:
                employees_with_the_job.append(employee)

        if employees_with_the_job is True:
            return employee_list
        else:
            return None

    def update_employee(self, employee):
        """Updates a employee object with the given id"""
        return self.data_wrapper.update_employee(employee)

    def delete_employee(self, id):
        """Deletes a employee object with the given id"""
        return self.data_wrapper.delete_employee(id)
