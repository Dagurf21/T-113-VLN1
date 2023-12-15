from data.employee_data import EmployeeData
from data.destination_data import DestinationData
from data.flight_data import FlightData
from data.plane_data import PlaneData
from data.voyage_data import VoyageData

from model import Employee, Destination, Voyage, Flight, Plane

class DataWrapper:
    """Connect the data layer and logic layer"""

    def __init__(self):
        """Initiates data_wrapper"""

        self.employee_data = EmployeeData()
        self.destination_data = DestinationData()
        self.flight_data = FlightData()
        self.plane_data = PlaneData()
        self.voyage_data = VoyageData()

    def get_all_employees(self) -> list[Employee]:
        """Returns a list of every stored employee"""
        return self.employee_data.get_all_employees()

    def create_employee(self, employee: Employee) -> int:
        """Stores employee into a file"""
        return self.employee_data.create_employee(employee)
    
    def update_employee(self, employee: Employee) -> None:
        """Updates the stored employee"""
        return self.employee_data.update_employee(employee)
        
    def delete_employee(self, employee_id: int) -> None:
        """Removes the employee from the storage"""
        return self.employee_data.delete_employee(employee_id)

    def create_destination(self, destination: Destination) -> int:
        """Stores destination into a file"""
        return self.destination_data.create_destination(destination)

    def get_all_destinations(self) -> list[Destination]:
        """Returns a list of every stored destination"""
        return self.destination_data.get_all_destinations()

    def update_destination(self, destination: Destination) -> None:
        """Updates the stored destination"""
        return self.destination_data.update_destination(destination)
        
    def delete_destination(self, destination_id: int) -> None:
        """Removes the employee from the storage"""
        return self.destination_data.delete_destination(destination_id)

    def create_plane(self, plane: Plane) -> int:
        """Stores plane into a file"""
        return self.plane_data.create_plane(plane)

    def get_all_planes(self) -> list[Plane]:
        """Returns a list of every stored plane"""
        return self.plane_data.get_all_planes()

    def update_plane(self, plane: Plane) -> None:
        """Updates the stored plane"""
        return self.plane_data.update_plane(plane)

    def delete_plane(self, plane_id: int) -> None:
        """Removes the plane from the storage"""
        return self.plane_data.delete_plane(plane_id)

    def create_voyage(self, voyage: Voyage) -> int:
        """Stores voyage into a file"""
        return self.voyage_data.create_voyage(voyage)

    def get_all_voyages(self) -> list[Voyage]:
        """Returns a list of every stored voyage"""
        return self.voyage_data.get_all_voyages()

    def update_voyage(self, voyage: Voyage) -> None:
        """Updates the stored voyage"""
        return self.voyage_data.update_voyage(voyage)

    def cancel_voyage(self, voyage_id: int) -> None:
        """Removes the voyage from the storage"""
        return self.voyage_data.cancel_voyage(voyage_id)

    def create_flight(self, flight: Flight) -> None:
        """Stores flight into a file"""
        return self.flight_data.create_flight(flight)

    def get_all_flights(self) -> list[Flight]:
        """Returns a list of every stored flight"""
        return self.flight_data.get_all_flights()

    def update_flight(self, flight: Flight) -> None:
        """Removes the flight from the storage"""
        return self.flight_data.update_flight(flight)
