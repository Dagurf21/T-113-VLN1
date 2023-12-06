from model.flight import Flight
import csv
from tempfile import NamedTemporaryFile
import shutil

class FlighData:
    def __init__(self):
        self.file_name = "files/flights.csv"
    

    def create_flight(self, flight):
        """Writes a new flight to the storage file"""
        with open(self.file_name, 'a', newline='', encoding="utf-8") as csvfile:
            fieldnames = ["id", "flight_nr", "departure", "destination", "departure_time", "arrival_time"]
            
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            id = self.get_new_id()
            
            writer.writerow({'id': id, 'flight_nr': flight.flight_nr, 'departure': flight.departure, 'destination': flight.destination, 'departure_time': flight.departure_time, 'arrival_time': flight.arrival_time})

    
    def get_new_id(self) -> int:
        """Returns a new id"""
        id = 0
        with open(self.file_name, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            
            for row in reader:
                id += 1

            return id


    def get_flight(self, flight_id):
        """Returns the requested flight, if flight is not found returns None"""
        with open(self.file_name, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            
            for row in reader:
                
                if int(row["id"]) == flight_id:
                    return Flight(row["id"], row["flight_nr"], row["departure"], row["destination"], row["departure_time"], row["arrival_time"])

            # If no flight is found with the given id, return None
            return None


    def get_all_flights(self):
        """Returns a list of all flights"""
        ret_list = []
        
        with open(self.file_name, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            
            for row in reader:
                ret_list.append(Flight(row["id"], row["flight_nr"], row["departure"], row["destination"], row["departure_time"], row["arrival_time"]))
        
        return ret_list


    def update_flight(self, flight):
        """Updates the flight with the given id"""
        # Makes temporary file to not overwrite the original file
        tempfile = NamedTemporaryFile(mode='w', delete=False)
        
        with open(self.file_name, 'r', newline='', encoding="utf-8") as csvfile, tempfile:
            fieldnames = ["id", "flight_nr", "departure", "destination", "departure_time", "arrival_time"]
            
            reader = csv.DictReader(csvfile)
            writer = csv.DictWriter(tempfile, fieldnames=fieldnames)

            writer.writeheader()
            for row in reader:
                # Writes the flight with the new data into the temp file
                if int(row["id"]) == flight.id:
                    writer.writerow({'id': flight.id, 'flight_nr': flight.flight_nr, 'departure': flight.departure, 'destination': flight.destination, 'departure_time': flight.departure_time, 'arrival_time': flight.arrival_time})
                
                # Writes the other flights unchanged 
                else:
                    writer.writerow({'id': row["id"], 'flight_nr': row["flight_nr"], 'departure': row["departure"], 'destination': row["destination"], 'departure_time': row["departure_time"], 'arrival_time': row["arrival_time"]})

        # Replaces the main file with the tempfile
        shutil.move(tempfile.name, self.file_name)


    def delete_flight(self, flight_id):
        pass


