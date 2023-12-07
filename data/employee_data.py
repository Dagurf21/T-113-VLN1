import csv
from model.employee import Employee
from model.pilot import Pilot
from model.flight_attendant import FlightAttendant
from model.manager import Manager
from model.flight_manager import FlightManager
from tempfile import NamedTemporaryFile
import shutil

class EmployeeData:
    def __init__(self):
        self.file_name = "files/employees.csv"


    def get_all_employees(self):
        """Returns a list of all employees"""
        ret_list = []
        
        with open(self.file_name, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:

                # Assigns employees the appropriate employee subclass and append to ret_list
                if row["job_title"] == "Manager" or row["job_title"] == "Chuck Norris":
                    ret_list.append(Manager(id = row["id"], name = row["name"], password = row["password"], address = row["address"], ssn = row["ssn"], mobile_phone = row["mobile_phone"], email = row["email"], home_phone = row["home_phone"], work_phone = row["work_phone"]))
                
                elif row["job_title"] == "Pilot":
                    assignment_list = row["assignments"].split(".")
                    ret_list.append(Pilot(id = row["id"], name = row["name"], password = row["password"], license = row["license"], address = row["address"], ssn = row["ssn"], mobile_phone = row["mobile_phone"], email = row["email"], home_phone = row["home_phone"], assignments = assignment_list))
                
                elif row["job_title"] == "Flight Attendant":
                    assignment_list = row["assignments"].split(".")
                    ret_list.append(FlightAttendant(id = row["id"], name = row["name"], password = row["password"], address = row["address"], ssn = row["ssn"], mobile_phone = row["mobile_phone"], email = row["email"], home_phone = row["home_phone"], assignments = assignment_list))
                
                elif row["job_title"] == "Flight Manager":
                    ret_list.append(FlightManager(id = row["id"], name = row["name"], password = row["password"], address = row["address"], ssn = row["ssn"], mobile_phone = row["mobile_phone"], email = row["email"], home_phone = row["home_phone"], work_phone = row["work_phone"]))
                
                else:
                    pass

        return ret_list


    def create_employee(self, employee):
        """Writes new employee into the storage file"""
        with open(self.file_name, 'a', encoding="utf-8") as csvfile:
            fieldnames = ["id", "name", "job_title", "license", "password", "address", "ssn", "mobile_phone", "email", "home_phone", "work_phone", "assignments"]
            
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
                assignments = ""
                for voyage in employee.assignments:
                    assignments += f"{voyage}."

            elif isinstance(employee, FlightAttendant):
                job_title = "Flight Attendant"
                pilot_license = None
                work_phone = None
                assignments = ""
                for voyage in employee.assignments:
                    assignments += f"{voyage}."

            elif isinstance(employee, FlightManager):
                job_title = "Flight Manager"
                pilot_license = None
                work_phone = employee.work_phone
                assignments = None

            # Writes the employee to the bottom of file
            writer.writerow({'id': id, 'name': employee.name, 'job_title': job_title, 'license': pilot_license, 'password': employee.password, 'address': employee.address, 'ssn': employee.ssn, 'mobile_phone': employee.mobile_phone, 'email': employee.email, 'home_phone': employee.home_phone, 'work_phone': work_phone, 'assignments': assignments})
            
    

    def get_new_id(self) -> int:
        """Returns the id for a new employee"""
        id = 0
        with open(self.file_name, newline='', encoding="utf-8") as csvfile:
            
            reader = csv.DictReader(csvfile)
            
            for row in reader:
                id += 1

            return id
    

    def get_employee(self, employee_id):
        """Returns the requested employee as the correct employee class type.
        If no employee with the id is found return None
        """
        with open(self.file_name, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                if int(row["id"]) == employee_id:

                    # Finds out what employee subclass email is
                    if row["job_title"] == "Manager" or row["job_title"] == "Chuck Norris":
                        return Manager(id = int(row["id"]), name = row["name"], password = row["password"], address = row["address"], ssn = row["ssn"], mobile_phone = row["mobile_phone"], email = row["email"], home_phone = row["home_phone"], work_phone = row["work_phone"])
                    
                    elif row["job_title"] == "Pilot":
                        assignment_list = row["assignments"].split(".")
                        return Pilot(id = int(row["id"]), name = row["name"], password = row["password"], license = row["license"], address = row["address"], ssn = row["ssn"], mobile_phone = row["mobile_phone"], email = row["email"], home_phone = row["home_phone"], assignments = assignment_list)
                    
                    elif row["job_title"] == "Flight Attendant":
                        assignment_list = row["assignments"].split(".")
                        return FlightAttendant(id = int(row["id"]), name = row["name"], password = row["password"], address = row["address"], ssn = row["ssn"], mobile_phone = row["mobile_phone"], email = row["email"], home_phone = row["home_phone"], assignments = assignment_list)
                    
                    elif row["job_title"] == "Flight Manager":
                        return FlightManager(id = int(row["id"]), name = row["name"], password = row["password"], address = row["address"], ssn = row["ssn"], mobile_phone = row["mobile_phone"], email = row["email"], home_phone = row["home_phone"], work_phone = row["work_phone"])
                    
                    else:
                        return None

            # If no employee is found with the given id, return None
            return None
        

    def get_employee_by_email(self, employee_email):
        """Returns the requested employee as the correct employee class type.
        If no employee with the email is found return None
        """
        with open(self.file_name, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                if row["email"] == employee_email:
                    
                    # Finds out what employee subclass the employee is
                    if row["job_title"] == "Manager" or row["job_title"] == "Chuck Norris":
                        return Manager(id = int(row["id"]), name = row["name"], password = row["password"], address = row["address"], ssn = row["ssn"], mobile_phone = row["mobile_phone"], email = row["email"], home_phone = row["home_phone"], work_phone = row["work_phone"])
                    
                    elif row["job_title"] == "Pilot":
                        assignment_list = row["assignments"].split(".")
                        return Pilot(id = int(row["id"]), name = row["name"], password = row["password"], license = row["license"], address = row["address"], ssn = row["ssn"], mobile_phone = row["mobile_phone"], email = row["email"], home_phone = row["home_phone"], assignments = assignment_list)
                    
                    elif row["job_title"] == "Flight Attendant":
                        assignment_list = row["assignments"].split(".")
                        return FlightAttendant(id = int(row["id"]), name = row["name"], password = row["password"], address = row["address"], ssn = row["ssn"], mobile_phone = row["mobile_phone"], email = row["email"], home_phone = row["home_phone"], assignments = assignment_list)
                    
                    elif row["job_title"] == "Flight Manager":
                        return FlightManager(id = int(row["id"]), name = row["name"], password = row["password"], address = row["address"], ssn = row["ssn"], mobile_phone = row["mobile_phone"], email = row["email"], home_phone = row["home_phone"], work_phone = row["work_phone"])
                    
                    else:
                        return None

            # If no employee is found with the given id, return None
            return None


    def update_employee(self, employee):
        """Updates the employee with the given id"""
        # Makes temporary file to not overwrite the original file
        tempfile = NamedTemporaryFile(mode='w', delete=False)
        
        with open(self.file_name, 'r', newline='', encoding="utf-8") as csvfile, tempfile:
            fieldnames = ["id", "name", "job_title", "license", "password", "address", "ssn", "mobile_phone", "email", "home_phone", "work_phone", "assignments"]
        
            reader = csv.DictReader(csvfile)
            writer = csv.DictWriter(tempfile, fieldnames = fieldnames)

            # Writes the header into the tempfile
            writer.writeheader()

            # Looks for the employee to update
            for row in reader:

                # If the employee is found, the new data is written to the temporary file
                if int(row["id"]) == employee.id:
                    if row["job_title"] == "Manager" or row["job_title"] == "Chuck Norris" or row["job_title"] == "Flight Manager":
                        row["password"], row["address"], row["mobile_phone"], row["email"], row["home_phone"], row["work_phone"] = employee.password, employee.address, employee.mobile_phone, employee.email, employee.home_phone, employee.work_phone
                    
                    elif row["job_title"] == "Pilot":
                        assignments = ""
                        for voyage in employee.assignments:
                            assignments += f"{voyage}."
                        row["license"], row["password"], row["address"], row["mobile_phone"], row["email"], row["home_phone"], row["assignments"]  = employee.password, employee.address, employee.mobile_phone, employee.email, employee.home_phone, assignments
                    
                    elif row["job_title"] == "Flight Attendant":
                        assignments = ""
                        for voyage in employee.assignments:
                            assignments += f"{voyage}."
                        row["password"], row["address"], row["mobile_phone"], row["email"], row["home_phone"], row["assignments"]  = employee.password, employee.address, employee.mobile_phone, employee.email, employee.home_phone, assignments
                
                # Each row from the original file is written to the temporary file
                row = {'id': row["id"], 'name': row["name"], 'job_title': row["job_title"], 'license': row["license"], 'password': row["password"], 'address': row["address"], 'ssn': row["ssn"], 'mobile_phone': row["mobile_phone"], 'email': row["email"], 'home_phone': row["home_phone"], 'work_phone': row["work_phone"]}
                writer.writerow(row)

        # The temporary file replaces the original file
        shutil.move(tempfile.name, self.file_name)
    

    def delete_employee(self, employee_id):
        """Deletes the employee with the given id"""
        # Makes temporary file to not overwrite the original file
        tempfile = NamedTemporaryFile(mode='w', delete=False)
        
        with open(self.file_name, 'r', newline='', encoding="utf-8") as csvfile, tempfile:
            fieldnames = ["id", "name", "job_title", "license", "password", "address", "ssn", "mobile_phone", "email", "home_phone", "work_phone", "assignments"]
            
            reader = csv.DictReader(csvfile)
            writer = csv.DictWriter(tempfile, fieldnames=fieldnames)
            
            # Writes the header to the tempfile
            writer.writeheader()

            # Looks for the employee to delete
            for row in reader:

                # If the employee is found, Everything except id and name is erased
                if int(row["id"]) == employee_id:
                    row = {'id' : row["id"], 'name' : row["name"], 'job_title' : None, 'password' : None, 'address' : None, 'ssn' : None, 'mobile_phone' : None, 'email' : None, 'home_phone' : None, 'work_phone' : None, 'assignments' : None}

                # Each row from the original file is written to the temporary file
                else:
                    row = {'id': row["id"], 'name': row["name"], 'job_title': row["job_title"], 'license': row["license"], 'password': row["password"], 'address': row["address"], 'ssn': row["ssn"], 'mobile_phone': row["mobile_phone"], 'email': row["email"], 'home_phone': row["home_phone"], 'work_phone': row["work_phone"], 'assignments' : row["assignments"]}
                
                writer.writerow(row)

        # The temporary file replaces the original file
        shutil.move(tempfile.name, self.file_name)
