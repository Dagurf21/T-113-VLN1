from model.flight_route import FlightRoute
import csv

class FlightRoute_Data:
    def __init__(self):
        self.file_name = "files/flight_routes.csv"
    

    def create_flight_route(self, flight_route):
        with open(self.file_name, 'a', newline='', encoding="utf-8") as csvfile:
            fieldnames = ["id", "flight_nr", "departure", "destination", "departure_time", "arrival_time"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            id = self.get_new_id()
            writer.writerow({'id': id, 'flight_nr': flight_route.flight_nr, 'departure': flight_route.departure, 'destination': flight_route.destination, 'departure_time': flight_route.departure_time, 'arrival_time': flight_route.arrival_time})

    
    def get_new_id(self) -> int:
        """Returns a new id"""
        pass


    def get_flight_route(self, flight_route_id):
        pass


    def get_all_flight_routes(self):
        pass


    def update_flight_route(self, flight_route_id):
        pass


    def delete_flight_route(self, flight_route_id):
        pass


