from model import Employee, Pilot, FlightAttendant, Manager, FlightManager
from tempfile import NamedTemporaryFile
import csv
import shutil

class EmployeeData:
    def __init__(self) -> None:
        self.file_name = "files/employees.csv"

    def get_all_employees(self) -> list["Employee"]:
        """Returns a list of all employees"""

        ret_list = []
        
        with open(self.file_name, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:

                # Assigns employees the appropriate employee subclass and append to ret_list
                match row["job_title"]:
                    case "Manager" | "Chuck Norris":
                        ret_list.append(Manager(
                            id = int(row["id"]), 
                            name = row["name"], 
                            password = row["password"], 
                            address = row["address"], 
                            ssn = row["ssn"], 
                            mobile_phone = row["mobile_phone"], 
                            email = row["email"], 
                            home_phone = row["home_phone"], 
                            work_phone = row["work_phone"]
                        ))
                
                    case "Pilot":
                        # Create a list of ints from the string seperated by '.'
                        assignment_list = [int(assignment) for assignment in row["assignments"].split(".") if assignment != ""]

                        ret_list.append(Pilot(
                            id = int(row["id"]), 
                            name = row["name"], 
                            password = row["password"], 
                            license = row["license"], 
                            address = row["address"], 
                            ssn = row["ssn"], 
                            mobile_phone = row["mobile_phone"], 
                            email = row["email"], 
                            home_phone = row["home_phone"], 
                            assignments = assignment_list
                        ))
                
                    case "Flight Attendant":
                        # Create a list of ints from the string seperated by '.'
                        assignment_list = [int(assignment) for assignment in row["assignments"].split(".") if assignment != ""]

                        ret_list.append(FlightAttendant(
                            id = int(row["id"]), 
                            name = row["name"], 
                            password = row["password"], 
                            address = row["address"], 
                            ssn = row["ssn"], 
                            mobile_phone = row["mobile_phone"], 
                            email = row["email"], 
                            home_phone = row["home_phone"], 
                            assignments = assignment_list
                        ))
                
                    case "Flight Manager":
                        ret_list.append(FlightManager(
                            id = int(row["id"]), 
                            name = row["name"], 
                            password = row["password"], 
                            address = row["address"], 
                            ssn = row["ssn"], 
                            mobile_phone = row["mobile_phone"], 
                            email = row["email"], 
                            home_phone = row["home_phone"], 
                            work_phone = row["work_phone"]
                        ))
                
                    case _:
                        pass

        return ret_list


    def create_employee(self, employee) -> int:
        """Writes new employee into the storage file"""
        with open(self.file_name, 'a', encoding="utf-8") as csvfile:
            fieldnames = [
                "id",
                "name",
                "job_title",
                "license",
                "password",
                "address",
                "ssn",
                "mobile_phone",
                "email",
                "home_phone",
                "work_phone",
                "assignments"
            ]
            
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            id = self.get_new_id()

            # For assigning required variables to different employee types.
            if isinstance(employee, Manager):
                job_title = "Manager"
                pilot_license = None
                work_phone = employee.work_phone
                assignments = None

            elif isinstance(employee, Pilot):
                job_title = "Pilot"
                pilot_license = employee.license
                work_phone = None
                assignments = ".".join(employee.assignments)

            elif isinstance(employee, FlightAttendant):
                job_title = "Flight Attendant"
                pilot_license = None
                work_phone = None
                assignments = ".".join(employee.assignments)

            elif isinstance(employee, FlightManager):
                job_title = "Flight Manager"
                pilot_license = None
                work_phone = employee.work_phone
                assignments = None

            # Writes the employee to the bottom of file
            writer.writerow({
                'id': id, 
                'name': employee.name, 
                'job_title': job_title, 
                'license': pilot_license, 
                'password': employee.password, 
                'address': employee.address, 
                'ssn': employee.ssn, 
                'mobile_phone': employee.mobile_phone, 
                'email': employee.email, 
                'home_phone': employee.home_phone, 
                'work_phone': work_phone, 
                'assignments': assignments
            })
            
            return id
            

    def get_new_id(self) -> int:
        """Returns the id for a new employee"""

        id = 0
        with open(self.file_name, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            
            for _ in reader:
                id += 1

            return id


    def update_employee(self, employee) -> None:
        """Updates the employee with the given id"""
        # Makes temporary file to not overwrite the original file
        tempfile = NamedTemporaryFile(mode='w', delete=False)
        
        with open(self.file_name, 'r', newline='', encoding="utf-8") as csvfile, tempfile:
            fieldnames = [
                "id",
                "name",
                "job_title",
                "license",
                "password",
                "address",
                "ssn",
                "mobile_phone",
                "email",
                "home_phone",
                "work_phone",
                "assignments"
            ]
        
            reader = csv.DictReader(csvfile)
            writer = csv.DictWriter(tempfile, fieldnames = fieldnames)

            # Writes the header into the tempfile
            writer.writeheader()

            # Looks for the employee to update
            for row in reader:

                # If the employee is found, the new data is written to the temporary file
                if int(row["id"]) == employee.id:
                    match row["job_title"]:
                        case "Manager" | "Chuck Norris" | "Flight Manager":
                            row = {
                                'id' : row["id"], 
                                'name' : row["name"], 
                                'job_title' : row["job_title"],
                                'license' : None, 
                                'password' : employee.password, 
                                'address' : employee.address, 
                                'ssn' : row["ssn"], 
                                'mobile_phone' : employee.mobile_phone, 
                                'email' : employee.email, 
                                'home_phone' : employee.home_phone, 
                                'work_phone' : employee.work_phone, 
                                'assignments' : None
                            }
                    
                        case "Pilot":
                            assignments = ".".join(str(id) for id in employee.assignments)
                            row = {
                                'id' : row["id"], 
                                'name' : row["name"], 
                                'job_title' : row["job_title"],
                                'license' : employee.license, 
                                'password' : employee.password, 
                                'address' : employee.address, 
                                'ssn' : row["ssn"], 
                                'mobile_phone' : employee.mobile_phone, 
                                'email' : employee.email, 
                                'home_phone' : employee.home_phone, 
                                'work_phone' : None, 
                                'assignments' : assignments
                            }

                        case "Flight Attendant":
                            assignments = ".".join(str(id) for id in employee.assignments)
                            row = {
                                'id' : row["id"], 
                                'name' : row["name"], 
                                'job_title' : row["job_title"],
                                'license' : None, 
                                'password' : employee.password, 
                                'address' : employee.address, 
                                'ssn' : row["ssn"], 
                                'mobile_phone' : employee.mobile_phone, 
                                'email' : employee.email, 
                                'home_phone' : employee.home_phone, 
                                'work_phone' : None, 
                                'assignments' : assignments
                            }

                # Each row from the original file is written to the temporary file
                writer.writerow(row)

        # The temporary file replaces the original file
        shutil.move(tempfile.name, self.file_name)
    

    def delete_employee(self, employee_id) -> None:
        """Deletes the employee with the given id"""

        # Makes temporary file to not overwrite the original file
        tempfile = NamedTemporaryFile(mode='w', delete=False)
        
        with open(self.file_name, 'r', newline='', encoding="utf-8") as csvfile, tempfile:
            fieldnames = [
                "id",
                "name",
                "job_title",
                "license",
                "password",
                "address",
                "ssn",
                "mobile_phone",
                "email",
                "home_phone",
                "work_phone",
                "assignments"
            ]
            
            reader = csv.DictReader(csvfile)
            writer = csv.DictWriter(tempfile, fieldnames=fieldnames)
            
            # Writes the header to the tempfile
            writer.writeheader()

            # Looks for the employee to delete
            for row in reader:

                # If the employee is found, Everything except id and name is erased
                if int(row["id"]) == employee_id:
                    row = {
                        'id' : row["id"], 
                        'name' : row["name"], 
                        'job_title' : None, 
                        'password' : None, 
                        'address' : None, 
                        'ssn' : None, 
                        'mobile_phone' : None, 
                        'email' : None, 
                        'home_phone' : None, 
                        'work_phone' : None, 
                        'assignments' : None
                    }

                # Each row from the original file is written to the temporary file
                else:
                    row = {
                        'id': row["id"], 
                        'name': row["name"], 
                        'job_title': row["job_title"], 
                        'license': row["license"], 
                        'password': row["password"], 
                        'address': row["address"], 
                        'ssn': row["ssn"], 
                        'mobile_phone': row["mobile_phone"], 
                        'email': row["email"], 
                        'home_phone': row["home_phone"], 
                        'work_phone': row["work_phone"], 
                        'assignments' : row["assignments"]
                    }
                
                writer.writerow(row)

        # The temporary file replaces the original file
        shutil.move(tempfile.name, self.file_name)
