from model import *
from copy import deepcopy


class MockDataWrapper:
    def __init__(self):
        self.employees: list[Employee] = []
        self.flights: list[Flight] = []
        self.destinations: list[Destination] = []
        self.voyages: list[Voyage] = []
        self.planes: list[Plane] = []

        self.employee_id_mark = 0
        self.flight_id_mark = 0
        self.destination_id_mark = 0
        self.voyage_id_mark = 0
        self.plane_id_mark = 0

    def get_all_employees(self) -> list[Employee]:
        return deepcopy(self.employees)

    def create_employee(self, employee: Employee) -> None:
        employee = deepcopy(employee)
        employee.id = self.employee_id_mark
        self.employee_id_mark += 1
        self.employees.append(employee)

    def update_employee(self, employee: Employee) -> None:
        try:
            idx = self.employees.index(employee)
            self.employees[idx] = deepcopy(employee)
        except ValueError:
            pass

    def delete_employee(self, id: int) -> None:
        employees = self.get_all_employees()
        for employee in employees:
            if employee.id == id:
                self.employees.remove(employee)

    def create_destination(self, destination: Destination) -> None:
        destination = deepcopy(destination)
        destination.id = self.employee_id_mark
        self.employee_id_mark += 1
        self.destinations.append(destination)

    def get_all_destinations(self) -> list[Destination]:
        return deepcopy(self.destinations)

    def update_destination(self, destination: Destination) -> None:
        try:
            idx = destination.id
            self.destinations[idx] = deepcopy(destination)
        except ValueError:
            pass

    def delete_destination(self, destination_id: int) -> None:
        destinations = self.get_all_destinations()
        for destination in destinations:
            if destination.id == destination_id:
                self.destinations.remove(destination)

    def create_plane(self, plane: Plane) -> None:
        plane = deepcopy(plane)
        plane.id = self.plane_id_mark
        self.plane_id_mark += 1
        self.planes.append(plane)

    def get_all_planes(self: Plane) -> list[Plane]:
        return deepcopy(self.planes)

    def update_plane(self, plane: Plane) -> None:
        try:
            idx = self.planes.index(plane)
            self.planes[idx] = deepcopy(plane)
        except ValueError:
            pass

    def delete_plane(self, plane_id: int) -> None:
        planes = self.get_all_planes()
        for plane in planes:
            if plane.id == plane_id:
                self.planes.remove(plane)

    def create_voyage(self, voyage: Voyage) -> None:
        voyage = deepcopy(voyage)
        voyage.id = self.voyage_id_mark
        self.voyage_id_mark += 1
        self.voyages.append(voyage)

    def get_all_voyages(self) -> list[Voyage]:
        return deepcopy(self.voyages)

    def update_voyage(self, voyage: Voyage) -> None:
        try:
            idx = self.voyages.index(voyage)
            self.voyages[idx] = deepcopy(voyage)
        except ValueError:
            pass

    def cancel_voyage(self, voyage_id: int) -> None:
        voyages = self.get_all_voyages()
        for voyage in voyages:
            if voyage.id == voyage_id:
                self.voyages.remove(voyage)

    def create_flight(self, flight: Flight) -> None:
        flight = deepcopy(flight)
        flight.id = self.flight_id_mark
        self.flight_id_mark += 1
        self.flights.append(flight)

    def get_all_flights(self) -> list[Flight]:
        return deepcopy(self.flights)

    def update_flight(self, flight: Flight) -> None:
        try:
            idx = self.flights.index(flight)
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
