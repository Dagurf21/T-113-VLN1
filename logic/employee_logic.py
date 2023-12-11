from logic import Validator, Utilities
from model import Employee, Pilot


class EmployeeLogic:
    """This class is the logic layer for the employee class"""

    def __init__(self, data_connection) -> None:
        self.data_wrapper = data_connection
        self.validate = Validator()
        self.utility = Utilities()

    def create_employee(self, employee) -> None:
        """Takes in a employee object and forwards it to the data layer"""
        employee.password = self.utility.password_encoder(employee.password)
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

    def get_all_pilots(self) -> list["Employee"]:
        """Returns a sorted list of pilots"""
        pilot_list = self.get_employees_by_job("Pilot")
        pilot_list.sort()
        return pilot_list

    def get_pilots_by_liscense(self, liscense) -> list["Pilot"]:
        """Returns a list of pilots with the given liscense"""
        pilot_list = self.get_all_pilots()

        pilots_with_the_liscense = []

        for pilot in pilot_list:
            if type(pilot).__name__ == liscense:
                pilots_with_the_liscense.append(pilot)

        return pilots_with_the_liscense

    def update_employee(self, employee) -> None:
        """Updates a employee object with the given id"""
        return self.data_wrapper.update_employee(employee)

    def delete_employee(self, employee_id) -> None:
        """Deletes a employee object with the given id"""
        return self.data_wrapper.delete_employee(employee_id)

    def is_employee_manager(self, employee) -> None:
        """Checks if the given employee is manager"""
        manager_list = self.get_employees_by_job("Manager")
        if employee in manager_list:
            return True
        return False

    def is_employee_flight_manager(self, employee) -> None:
        """Checks if the given employee is manager"""
        flight_manager_list = self.get_employees_by_job("FlightManager")
        if employee in flight_manager_list:
            return True
        return False
