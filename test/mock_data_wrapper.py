from model import *
from copy import deepcopy


class MockDataWrapper:
    def __init__(self):
        self.employees: list[Employee] = []
        self.flights: list[Flight] = []
        self.destinations: list[Destination] = []
        self.voyages: list[Voyage] = []
        self.planes: list[Plane] = []

    def get_all_employees(self) -> list[Employee]:
        return deepcopy(self.employees)

    def create_employee(self, employee: Employee) -> None:
        employee = deepcopy(employee)
        employee.id = len(self.employees) - 1
        self.employees.append(employee)

    def update_employee(self, employee: Employee) -> None:
        try:
            idx = self.get_employee_index(employee.id)
            if idx is None:
                return None
            self.employees[idx] = deepcopy(employee)
        except ValueError:
            pass

    def delete_employee(self, id: int) -> None:
        employees = self.get_all_employees()
        for i, employee in enumerate(employees):
            if employee.id == id:
                self.employees[i] = None

    def create_destination(self, destination: Destination) -> None:
        destination = deepcopy(destination)
        destination.id = len(self.destinations) - 1
        self.destinations.append(destination)

    def get_all_destinations(self) -> list[Destination]:
        return deepcopy(self.destinations)

    def update_destination(self, destination: Destination) -> None:
        try:
            idx = self.get_destination_index(destination.id)
            if idx is None:
                return None
            self.destinations[idx] = deepcopy(destination)
        except ValueError:
            pass

    def delete_destination(self, destination_id: int) -> None:
        destinations = self.get_all_destinations()
        for i, destination in enumerate(destinations):
            if destination.id == destination_id:
                self.destinations[i] = None

    def create_plane(self, plane: Plane) -> None:
        plane = deepcopy(plane)
        plane.id = len(self.planes) - 1
        self.planes.append(plane)

    def get_all_planes(self: Plane) -> list[Plane]:
        return deepcopy(self.planes)

    def update_plane(self, plane: Plane) -> None:
        try:
            idx = plane.id
            if idx is None:
                return
            self.planes[idx] = deepcopy(plane)
        except ValueError:
            pass

    def delete_plane(self, plane_id: int) -> None:
        planes = self.get_all_planes()
        for i, plane in enumerate(planes):
            if plane.id == plane_id:
                self.planes[i] = None

    def create_voyage(self, voyage: Voyage) -> None:
        voyage = deepcopy(voyage)
        voyage.id = len(self.voyages) - 1
        self.voyages.append(voyage)

    def get_all_voyages(self) -> list[Voyage]:
        return deepcopy(self.voyages)

    def update_voyage(self, voyage: Voyage) -> None:
        try:
            idx = self.get_voyage_index(voyage.id)
            if idx is None:
                return
            self.voyages[idx] = deepcopy(voyage)
        except ValueError:
            pass

    def cancel_voyage(self, voyage_id: int) -> None:
        voyages = self.get_all_voyages()
        for i, voyage in enumerate(voyages):
            if voyage.id == voyage_id:
                self.voyages[i] = None

    def create_flight(self, flight: Flight) -> None:
        flight = deepcopy(flight)
        flight.id = len(self.flights) - 1
        self.flights.append(flight)

    def get_all_flights(self) -> list[Flight]:
        return deepcopy(self.flights)

    def update_flight(self, flight: Flight) -> None:
        try:
            idx = self.get_flight_index(flight)
            if idx is None:
                return
            self.flights[idx] = deepcopy(flight)
        except ValueError:
            pass

    # Testing utility functions

    def get_employee(self, id: int) -> list[Employee]:
        for elem in self.employees:
            if elem.id == id:
                return elem
        return None

    def get_destination(self, id: int) -> list[Destination]:
        for elem in self.destinations:
            if elem.id == id:
                return elem
        return None

    def get_plane(self, id: int) -> list[Plane]:
        for elem in self.planes:
            if elem.id == id:
                return elem
        return None

    def get_voyage(self, id: int) -> list[Voyage]:
        for elem in self.voyages:
            if elem.id == id:
                return elem
        return None

    def get_flight(self, id: int) -> list[Flight]:
        for elem in self.flights:
            if elem.id == id:
                return elem
        return None

    def get_first_employee(self) -> Employee:
        if len(self.employees) > 0:
            return deepcopy(self.employees[0])
        else:
            return None

    def get_first_destination(self) -> Destination:
        if len(self.destinations) > 0:
            return deepcopy(self.destinations[0])
        else:
            return None

    def get_first_plane(self) -> Plane:
        if len(self.planes) > 0:
            return deepcopy(self.planes[0])
        else:
            return None

    def get_first_voyage(self) -> Voyage:
        if len(self.voyages) > 0:
            return deepcopy(self.voyages[0])
        else:
            return None

    def get_first_flight(self) -> Flight:
        if len(self.flights) > 0:
            return deepcopy(self.flights[0])
        else:
            return None
    
    def get_employee_index(self, id: int) -> int:
        for i, elem in enumerate(self.employees):
            if elem.id == id:
                return i
        return None

    def get_destination_index(self, id: int) -> int:
        for i, elem in enumerate(self.destinations):
            if elem.id == id:
                return i
        return None

    def get_plane_index(self, id: int) -> int:
        for i, elem in enumerate(self.planes):
            if elem.id == id:
                return i
        return None

    def get_voyage_index(self, id: int) -> int:
        for i, elem in enumerate(self.voyages):
            if elem.id == id:
                return i
        return None

    def get_flight_index(self, flight: Flight) -> int:
        for i, elem in enumerate(self.flights):
            if elem.flight_number == flight.flight_number and elem.date == flight.date:
                return i
        return None
