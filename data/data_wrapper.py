from data.employee_data import EmployeeData
from data.destination_data import DestinationData
from data.flight_route_data import FlightRouteData
from data.plane_data import PlaneData
from data.voyage_data import VoyageData

class DataWrapper:
    def __init__(self):
        self.employee_data = EmployeeData()
        self.destination_data = DestinationData()
        self.flight_route_data = FlightRouteData()
        self.plane_data = PlaneData()
        self.voyage_data = VoyageData()

    def get_all_employees(self):
        return self.employee_data.get_all_employees()

    def create_employee(self, employee):
        return self.employee_data.create_employee(employee)
    
    def get_employee(self, employee_id):
        return self.employee_data.get_employee(employee_id)

    def update_employee(self, employee):
        return self.employee_data.update_employee(employee)
        
    def delete_employee(self, employee_id):
        pass

    def create_destination(self, destination):
        return self.destination_data.create_destination(destination)

    def get_all_destinations(self):
        return self.destination_data.get_all_destinations()

    def get_destination(self, destination_id):
        return self.destination_data.get_destination(destination_id)

    def update_destination(self, destination):
        return self.destination_data.update_destination(destination)
        
    def delete_destination(self, destination_id):
        pass

    def create_plane(self, plane):
        return self.plane_data.create_plane(plane)

    def get_all_planes(self):
        return self.plane_data.get_all_planes()

    def get_plane(self, plane_id):
        return self.plane_data.get_plane(plane_id)

    def update_plane(self, plane):
        return self.plane_data.update_plane(plane)

    def delete_plane(self, plane_id):
        pass

    def create_voyage(self, voyage):
        return self.voyage_data.create_voyage(voyage)

    def get_all_voyages(self):
        return self.voyage_data.get_all_voyages()

    def get_voyage(self, voyage_id):
        return self.voyage_data.get_voyage(voyage_id)

    def update_voyage(self, voyage):
        return self.voyage_data.update_voyage(voyage)

    def delete_voyage(self, voyage_id):
        pass

    def create_flight_route(self, flight_route):
        return self.flight_route_data.create_flight_route(flight_route)

    def get_all_flight_routes(self):
        return self.flight_route_data.get_all_flight_routes()
    
    def get_flight_route(self, flight_route_id):
        return self.flight_route_data.get_flight_route(flight_route_id)

    def update_flight_route(self, flight_route):
        return self.flight_route_data.update_flight_route(flight_route)

    def delete_flight_route(self, flight_route_id):
        pass