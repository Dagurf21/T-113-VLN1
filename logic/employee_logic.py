from logic.logic_utilities import Validator

from model.employee import Employee
from model.pilot import Pilot
from model.flight_attendant import FlightAttendant
from model.manager import Manager
from model.flight_manager import FlightManager

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
                # Finds out what employee subclass email is
                match employee["job_title"]:
                    case "Manager" | "Chuck Norris":
                        return Manager(
                            id=int(employee["id"]),
                            name=employee["name"],
                            password=employee["password"],
                            address=employee["address"],
                            ssn=employee["ssn"],
                            mobile_phone=employee["mobile_phone"],
                            email=employee["email"],
                            home_phone=employee["home_phone"],
                            work_phone=employee["work_phone"],
                        )

                    case "Pilot":
                        assignment_list = employee["assignments"].split(".")
                        return Pilot(
                            id=int(employee["id"]),
                            name=employee["name"],
                            password=employee["password"],
                            license=employee["license"],
                            address=employee["address"],
                            ssn=employee["ssn"],
                            mobile_phone=employee["mobile_phone"],
                            email=employee["email"],
                            home_phone=employee["home_phone"],
                            assignments=assignment_list,
                        )

                    case "Flight Attendant":
                        assignment_list = employee["assignments"].split(".")
                        return FlightAttendant(
                            id=int(employee["id"]),
                            name=employee["name"],
                            password=employee["password"],
                            address=employee["address"],
                            ssn=employee["ssn"],
                            mobile_phone=employee["mobile_phone"],
                            email=employee["email"],
                            home_phone=employee["home_phone"],
                            assignments=assignment_list,
                        )

                    case "Flight Manager":
                        return FlightManager(
                            id=int(employee["id"]),
                            name=employee["name"],
                            password=employee["password"],
                            address=employee["address"],
                            ssn=employee["ssn"],
                            mobile_phone=employee["mobile_phone"],
                            email=employee["email"],
                            home_phone=employee["home_phone"],
                            work_phone=employee["work_phone"],
                        )

                    case _:
                        return None

        pass

    def get_employee_by_email(self, employee_email):
        """Returns a employee object with the given id"""
        employee_list = self.data_wrapper.get_employee_by_email(employee_email)

        for employee in employee_list:
            if employee["email"] == employee_email:
                # Finds out what employee subclass the employee is
                match employee["job_title"]:
                    case "Manager" | "Chuck Norris":
                        return Manager(
                            id=int(employee["id"]),
                            name=employee["name"],
                            password=employee["password"],
                            address=employee["address"],
                            ssn=employee["ssn"],
                            mobile_phone=employee["mobile_phone"],
                            email=employee["email"],
                            home_phone=employee["home_phone"],
                            work_phone=employee["work_phone"],
                        )

                    case "Pilot":
                        assignment_list = employee["assignments"].split(".")
                        return Pilot(
                            id=int(employee["id"]),
                            name=employee["name"],
                            password=employee["password"],
                            license=employee["license"],
                            address=employee["address"],
                            ssn=employee["ssn"],
                            mobile_phone=employee["mobile_phone"],
                            email=employee["email"],
                            home_phone=employee["home_phone"],
                            assignments=assignment_list,
                        )

                    case "Flight Attendant":
                        assignment_list = employee["assignments"].split(".")
                        return FlightAttendant(
                            id=int(employee["id"]),
                            name=employee["name"],
                            password=employee["password"],
                            address=employee["address"],
                            ssn=employee["ssn"],
                            mobile_phone=employee["mobile_phone"],
                            email=employee["email"],
                            home_phone=employee["home_phone"],
                            assignments=assignment_list,
                        )

                    case "Flight Manager":
                        return FlightManager(
                            id=int(employee["id"]),
                            name=employee["name"],
                            password=employee["password"],
                            address=employee["address"],
                            ssn=employee["ssn"],
                            mobile_phone=employee["mobile_phone"],
                            email=employee["email"],
                            home_phone=employee["home_phone"],
                            work_phone=employee["work_phone"],
                        )

                    # If ID is found but employee has been deleted
                    case _:
                        return None

    def get_employee_by_job(self, employee_email):
        """Returns a employee object with the given id"""
        employee = self.data_wrapper.get_employee_by_email(employee_email)

        pass

    def update_employee(self, employee):
        """Updates a employee object with the given id"""
        return self.data_wrapper.update_employee(employee)

    def delete_employee(self, id):
        """Deletes a employee object with the given id"""
        return self.data_wrapper.delete_employee(id)
