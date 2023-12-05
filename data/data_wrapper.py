from data.employee_data import Employee_Data

class DataWrapper:
    def __init__(self):
        self.employee_data = Employee_Data()

    def get_all_employees(self):
        return self.employee_data.read_all_employees()

    def create_employee(self, employee):
        return self.employee_data.create_employee(employee)
    
    def get_employee(self, employee_id):
        pass

    def update_employee(self, employee_id):
        pass

    def delete_employee(self, employee_id):
        pass

    def create_destination(self, destination):
        pass

    def get_all_destinations(self):
        pass

    def get_destination(self, destination_id):
        pass

    def update_destination(self, destination_id):
        pass

    def delete_destination(self, destination_id):
        pass

    def create_plane(self, plane):
        pass

    def get_all_planes(self):
        pass

    def get_plane(self, plane_id):
        pass

    def update_plane(self, plane_id):
        pass

    def delete_plane(self, plane_id):
        pass

    def create_voyage(self, voyage):
        pass

    def get_all_voyages(self):
        pass

    def get_voyage(self, voyage_id):
        pass

    def update_voyage(self, voyage_id):
        pass

    def delete_voyage(self, voyage_id):
        pass

    def create_flight(self, flight):
        pass

    def get_all_flights(self):
        pass
    
    def get_flight(self, flight_id):
        pass

    def update_flight(self, flight_id):
        pass

    def delete_flight(self, flight_id):
        pass