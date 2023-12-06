from model.destination import Destination
import csv
from tempfile import NamedTemporaryFile
import shutil

class DestinationData:
    def __init__(self) -> None:
        self.file_name = "files/destinations.csv"

    
    def create_destination(self, destination):
        """Writes new destination to storage file"""
        with open(self.file_name, 'a', newline='', encoding="utf-8") as csvfile:
            fieldnames = ["id", "country", "airport", "flight_time", "distance", "representative", "emergency_number"]
        
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            id = self.get_new_id()
            
            writer.writerow({'id': id, 'country': destination.country, 'airport': destination.airport, 'flight_time': destination.flight_time, 'distance': destination.distance_km, 'representative': destination.representative, 'emergency_number': destination.emergency_number})


    def get_new_id(self) -> int:
        """Returns a new id"""
        id = 0
        
        with open(self.file_name, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            
            for row in reader:
                id += 1

            return id
    

    def get_destination(self, destination_id) -> "Destination":
        """Returns the requested destination, if no destination is found return None"""
        with open(self.file_name, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            
            for row in reader:
                
                if int(row["id"]) == destination_id:
                    return Destination(row["id"], row["country"], row["airport"], row["flight_time"], row["distance"], row["representative"], row["emergency_number"])
            
            # If no destination is found with the given id, return None
            return None
    

    def get_all_destinations(self) -> list["Destination"]:
        """Returns a list of all destinations"""
        ret_list = []
        
        with open(self.file_name, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            
            for row in reader:
                ret_list.append(Destination(row["id"], row["country"], row["airport"], row["flight_time"], row["distance"], row["representative"], row["emergency_number"]))
        
        return ret_list
    

    def update_destination(self, destination):
        """Updates the destination with the given id"""
        # Makes temporary file to not overwrite the original file
        tempfile = NamedTemporaryFile(mode='w', delete=False)

        with open(self.file_name, 'r', newline='', encoding="utf-8") as csvfile, tempfile:
            fieldnames = ["id", "country", "airport", "flight_time", "distance", "representative", "emergency_number"]
            
            reader = csv.DictReader(csvfile, fieldnames=fieldnames)
            writer = csv.DictWriter(tempfile, fieldnames=fieldnames)

            for row in reader:
                if int(row["id"]) == destination.id:
                    writer.writerow({'id': destination.id, 'country': destination.country, 'airport': destination.airport, 'flight_time': destination.flight_time, 'distance': destination.distance_km, 'representative': destination.representative, 'emergency_number': destination.emergency_number})
                else:
                    writer.writerow({'id': row["id"], 'country': row["country"], 'airport': row["airport"], 'flight_time': row["flight_time"], 'distance': row["distance"], 'representative': row["representative"], 'emergency_number': row["emergency_number"]})

        shutil.move(tempfile.name, self.file_name)
    

    def delete_destination(self, destination_id):
        pass