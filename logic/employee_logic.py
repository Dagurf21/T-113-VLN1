from logic.logic_utilities import Validator
from model.employee import Employee

class EmployeeLogic:
    """This class is the logic layer for the employee class"""
    def __init__(self, data_connection) -> None:
        self.data_wrapper = data_connection
        self.validate = Validator()


    def create_employee(self, employee) -> None:
        """Takes in a employee object and forwards it to the data layer"""
        return self.data_wrapper.create_employee(employee)


    def get_all_employees(self) -> list["Employee"]:
        """Returns a list of all employees"""
        return self.data_wrapper.get_all_employees()


    def get_employee(self, employee_id) -> "Employee":
        """Returns the requested employee as the correct employee class type.
        If no employee with the id is found return None"""
        employee_list = self.get_all_employees()

        for employee in employee_list:
            if employee.id == employee_id:
                return employee
        
        return None


    def get_employee_by_email(self, search_email) -> "Employee":
        """Returns a employee object with the given id"""
        employee_list = self.get_all_employees()

        for employee in employee_list:
            if employee.email == search_email:
                return employee
        
        return None


    def get_employees_by_job(self, job_title) -> list["Employee"]:
        """Returns a employee object with the given id"""
        employee_list = self.get_all_employees()

        employees_with_the_job = []

        for employee in employee_list:
            if type(employee).__name__ == job_title:
                employees_with_the_job.append(employee)

        return employees_with_the_job


    def update_employee(self, employee) -> None:
        """Updates a employee object with the given id"""
        return self.data_wrapper.update_employee(employee)


    def delete_employee(self, id) -> None:
        """Deletes a employee object with the given id"""
        return self.data_wrapper.delete_employee(id)
