from model.destination import Destination
import csv
from tempfile import NamedTemporaryFile
import shutil

class DestinationData:
    def __init__(self) -> None:
        self.file_name = "files/destinations.csv"

    
    def create_destination(self, destination) -> int:
        """Writes new destination to storage file"""
        with open(self.file_name, 'a', newline='', encoding="utf-8") as csvfile:
            fieldnames = ["id", "country", "airport", "distance", "flight_time", "representative", "emergency_number"]
        
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            id = self.get_new_id()
            
            writer.writerow({'id': id, 
                             'country': destination.country, 
                             'airport': destination.airport, 
                             'distance': destination.distance_km, 
                             'flight_time': destination.flight_time, 
                             'representative': destination.representative, 
                             'emergency_number': destination.emergency_number})
            
            return id


    def get_new_id(self) -> int:
        """Returns a new id"""
        id = 0
        
        with open(self.file_name, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            
            for row in reader:
                id += 1

            return id
    

    def get_all_destinations(self) -> list["Destination"]:
        """Returns a list of all destinations"""
        ret_list = []
        
        with open(self.file_name, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            
            for row in reader:
                if row["airport"]:
                    ret_list.append(Destination(
                        id = int(row["id"]), 
                        country = row["country"], 
                        airport = row["airport"], 
                        flight_time = int(row["flight_time"]), 
                        distance_km = int(row["distance"]), 
                        representative = row["representative"], 
                        emergency_number = row["emergency_number"]))
        
        return ret_list
    

    def update_destination(self, destination) -> None:
        """Updates the destination with the given id"""
        # Makes temporary file to not overwrite the original file
        tempfile = NamedTemporaryFile(mode='w', delete=False)

        with open(self.file_name, 'r', newline='', encoding="utf-8") as csvfile, tempfile:
            fieldnames = ["id", "country", "airport", "flight_time", "distance", "representative", "emergency_number"]
            
            reader = csv.DictReader(csvfile)
            writer = csv.DictWriter(tempfile, fieldnames=fieldnames)

            writer.writeheader()
            for row in reader:
                if int(row["id"]) == destination.id:
                    writer.writerow({'id': row["id"], 
                                     'country': destination.country, 
                                     'airport': destination.airport, 
                                     'distance': destination.distance_km, 
                                     'flight_time': destination.flight_time, 
                                     'representative': destination.representative, 
                                     'emergency_number': destination.emergency_number})
                else:
                    writer.writerow({'id': row["id"], 
                                     'country': row["country"], 
                                     'airport': row["airport"], 
                                     'distance': row["distance"], 
                                     'flight_time': row["flight_time"], 
                                     'representative': row["representative"], 
                                     'emergency_number': row["emergency_number"]})

        shutil.move(tempfile.name, self.file_name)
    

    def delete_destination(self, destination_id) -> None:
        """Deletes the plane with the given id"""
        # Makes temporary file to not overwrite the original file
        tempfile = NamedTemporaryFile(mode='w', delete=False)

        with open(self.file_name, 'r', newline='', encoding="utf-8") as csvfile, tempfile:
            fieldnames = ["id", "country", "airport", "distance", "flight_time", "representative", "emergency_number"]
            
            reader = csv.DictReader(csvfile)
            writer = csv.DictWriter(tempfile, fieldnames=fieldnames)
            
            # Writes the header to the tempfile
            writer.writeheader()

            # Looks for the plane to delete
            for row in reader:

                # If the plane is found, Everything except the id and name is erased
                if int(row["id"]) == destination_id:
                    row = {'id': row["id"], 
                           'country': row["country"], 
                           'airport': None, 
                           'distance': None, 
                           'flight_time': None, 
                           'representative': row["representative"], 
                           'emergency_number': row["emergency_number"]}

                # Each row from the original file is written to the temporary file
                else:
                    row = {'id': row["id"], 
                           'country': row["country"], 
                           'airport': row["airport"], 
                           'distance': row["distance"], 
                           'flight_time': row["flight_time"], 
                           'representative': row["representative"], 
                           'emergency_number': row["emergency_number"]}

                writer.writerow(row)

        # The temporary file replaces the original file
        shutil.move(tempfile.name, self.file_name)
