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
        if self.validate_employee(employee):
            employee.password = self.utility.password_encoder(employee.password)
            return self.data_wrapper.create_employee(employee)
        else:
            return None

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

    def get_employee_by_workday(self, workdate) -> list["Employee"]:
        """Returns a list of employees that are working on a specific day"""
        employee_return_list = []
        list_of_voyages = self.data_wrapper.get_all_voyages()
        for voyage in list_of_voyages:
            if voyage.departure_date == workdate or voyage.date == workdate:
                try:
                    for pilot in voyage.pilots:
                        if employee_return_list in employee_return_list:
                            ...
                        else:
                            employee_return_list.append(pilot)
                except TypeError:
                    ...
                try:
                    for flight_attendant in voyage.flight_attendants:
                        if employee_return_list in employee_return_list:
                            ...
                        else:
                            employee_return_list.append(flight_attendant)
                except TypeError:
                    ...
        return employee_return_list

    def get_employee_by_not_workday(self, workdate) -> list["Employee"]:
        """Returns a list of employees that are working on a specific day"""
        employee_return_list = []
        list_of_voyages = self.data_wrapper.get_all_voyages()
        for voyage in list_of_voyages:
            if voyage.departure_date != workdate and voyage.date != workdate:
                try:
                    for pilot in voyage.pilots:
                        if employee_return_list in employee_return_list:
                            ...
                        else:
                            employee_return_list.append(pilot)
                except TypeError:
                    ...
                try:
                    for flight_attendant in voyage.flight_attendants:
                        if employee_return_list in employee_return_list:
                            ...
                        else:
                            employee_return_list.append(flight_attendant)
                except TypeError:
                    ...
        return employee_return_list

    def get_all_pilots(self) -> list["Employee"]:
        """Returns a sorted list of pilots"""
        pilot_list = self.get_employees_by_job("Pilot")
        pilot_list.sort()
        return pilot_list

    def get_pilots_by_license(self, planelicense) -> list["Pilot"]:
        """Returns a list of pilots with the given license"""
        pilot_list = self.get_all_pilots()

        pilots_with_the_license = []

        for pilot in pilot_list:
            if planelicense == pilot.license:
                pilots_with_the_license.append(pilot)

        return pilots_with_the_license

    def update_employee(self, employee) -> None:
        """Updates a employee object with the given id"""
        change_employee = self.get_employee(employee.id)

        if change_employee != None:
            employee.name = change_employee.name
            employee.ssn = change_employee.ssn
            return self.data_wrapper.update_employee(employee)
        else:
            return None

    def delete_employee(self, employee_id) -> None:
        """Deletes a employee object with the given id"""
        return self.data_wrapper.delete_employee(employee_id)

    def get_plane_licenses(self) -> list:
        """Returns a list of plane types"""
        plane_list = self.data_wrapper.get_all_planes()
        license_list = []
        for plane in plane_list:
            license_list.append(plane.type)
        return license_list

    def validate_employee(self, employee):
        """Validates a given employee"""
        employee_job_title = type(employee).__name__

        is_employee_valid = True
        is_ssn_valid = self.validate.ssn(employee.ssn)
        is_mobile_phone_valid = self.validate.phone_number(employee.mobile_phone)
        is_phone_valid = self.validate.phone_number(employee.mobile_phone)
        is_email_valid = self.validate.email(employee.email)
        if employee.home_phone is not None:
            is_phone_valid = is_phone_valid and self.validate.phone_number(
                employee.home_phone
            )

        if employee_job_title == "Manager" or employee_job_title == "FlightManager":
            is_phone_valid = is_phone_valid and self.validate.phone_number(
                employee.work_phone
            )

        if employee_job_title == "Pilot" or employee_job_title == "FlightAttendant":
            try:
                is_license_valid = self.validate.licenses(
                    employee.license, self.get_plane_licenses()
                )
                is_employee_valid = is_employee_valid and is_license_valid
                raise Exception("Pilot verify over")
            except (AttributeError, Exception):
                is_assignments_valid = self.validate.assignments(employee.assignments)
                is_employee_valid = is_employee_valid and is_assignments_valid

        return (
            is_employee_valid
            and is_ssn_valid
            and is_mobile_phone_valid
            and is_email_valid
            and is_phone_valid
        )


    def check_job_position(self, employee_id, job_title) -> bool:
        """Validates if the employee is the job title"""
        employee = self.get_employee(employee_id)
        print(type(employee).__name__)
        if type(employee).__name__ == job_title:

                return True

        return False
