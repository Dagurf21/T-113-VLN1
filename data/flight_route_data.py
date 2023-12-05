from model.flight_route import FlightRoute
import csv
from tempfile import NamedTemporaryFile
import shutil

class FlightRouteData:
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
        id = 0
        with open(self.file_name, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                id += 1

            return id


    def get_flight_route(self, flight_route_id):
        with open(self.file_name, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if int(row["id"]) == flight_route_id:
                    return FlightRoute(row["id"], row["flight_nr"], row["departure"], row["destination"], row["departure_time"], row["arrival_time"])

            # If no flight_route is found with the given id, return None
            return None


    def get_all_flight_routes(self):
        ret_list = []
        with open(self.file_name, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                ret_list.append(FlightRoute(row["id"], row["flight_nr"], row["departure"], row["destination"], row["departure_time"], row["arrival_time"]))
        return ret_list


    def update_flight_route(self, flight_route):
        """Updates the flight_route with the given id"""
        # Makes temporary file to not overwrite the original file
        tempfile = NamedTemporaryFile(mode='w', delete=False)
        with open(self.file_name, 'r', newline='', encoding="utf-8") as csvfile, tempfile:
            fieldnames = ["id", "flight_nr", "departure", "destination", "departure_time", "arrival_time"]
            reader = csv.DictReader(csvfile, fieldnames=fieldnames)
            writer = csv.DictWriter(tempfile, fieldnames=fieldnames)

            for row in reader:
                if int(row["id"]) == flight_route.id:
                    writer.writerow({'id': flight_route.id, 'flight_nr': flight_route.flight_nr, 'departure': flight_route.departure, 'destination': flight_route.destination, 'departure_time': flight_route.departure_time, 'arrival_time': flight_route.arrival_time})
                else:
                    writer.writerow({'id': row["id"], 'flight_nr': row["flight_nr"], 'departure': row["departure"], 'destination': row["destination"], 'departure_time': row["departure_time"], 'arrival_time': row["arrival_time"]})

        shutil.move(tempfile.name, self.file_name)


    def delete_flight_route(self, flight_route_id):
        pass


