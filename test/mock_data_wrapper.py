from model import *

class MockDataWrapper:
    def __init__(self):
        self.employees = []
        self.flights = []
        self.destinations = []
        self.voyages = []
        self.planes = []

    # Employee Class
    def get_all_employees(self) -> None:
        return self.employees[:]

    def create_employee(self, employee) -> None:
        self.employees.append(employee)

    def update_employee(self, employee) -> None:
        try:
            idx = self.employees.index(employee)
            self.employees[idx] = employee
        except ValueError:
            pass

    def delete_employee(self, id) -> None:
        employees = self.get_all_employees()
        for employee in employees:
            if employee.id == id:
                self.employees.remove(employee)

    def create_destination(self, destination):
        self.destinations.append(destination)

    def get_all_destinations(self):
        return self.destinations[:]

    def update_destination(self, destination):
        try:
            idx = self.destinations.index(destination)
            self.destinations[idx] = destination
        except ValueError:
            pass
        
    def delete_destination(self, destination_id):
        destinations = self.get_all_destinations()
        for destination in destinations:
            if destination.id == id:
                self.destinations.remove(destination)

    def create_plane(self, plane):
        self.planes.append(plane)

    def get_all_planes(self):
        return self.planes[:]

    def update_plane(self, plane):
        try:
            idx = self.planes.index(plane)
            self.planes[idx] = plane
        except ValueError:
            pass

    def delete_plane(self, plane_id):
        planes = self.get_all_planes()
        for plane in planes:
            if plane.id == id:
                self.planes.remove(plane)

    def create_voyage(self, voyage):
        self.voyages.append(voyage)

    def get_all_voyages(self):
        return self.voyages[:]

    def update_voyage(self, voyage):
        try:
            idx = self.voyages.index(voyage)
            self.voyages[idx] = voyage
        except ValueError:
            pass

    def cancel_voyage(self, voyage_id):
        voyages = self.get_all_voyages()
        for voyage in voyages:
            if voyage.id == id:
                self.voyages.remove(voyage)
    
    def create_flight(self, flight):
        self.flights.append(flight)

    def get_all_flights(self):
        return self.flights[:]

    def update_flight(self, flight):
        try:
            idx = self.flights.index(flight)
            self.flights[idx] = flight
        except ValueError:
            pass

