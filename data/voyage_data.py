from model.voyage import Voyage
import csv
from tempfile import NamedTemporaryFile
import shutil

class VoyageData:
    def __init__(self) -> None:
        self.file_name = "files/voyages.csv"
    

    def create_voyage(self, voyage):
        """Writes new voyage into the storage file"""
        with open(self.file_name, 'a', newline='', encoding="utf-8") as csvfile:
            fieldnames = ["id", "sold_seats", "plane","pilots", "attendants", "departure_flight", "arrival_flight", "date", "status"]
            
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            id = self.get_new_id()
            
            writer.writerow({'id': id, 'sold_seats': voyage.sold_seats, 'plane': voyage.plane, 'pilots': voyage.pilots, 'attendants': voyage.flight_attendants, 'departure_flight': voyage.departure_flight, 'arrival_flight': voyage.arrival_flight, 'date': voyage.date, 'status': voyage.status})


    def get_new_id(self) -> int:
        """Returns a new id"""
        id = 0
        with open(self.file_name, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            
            for row in reader:
                id += 1

            return id


    def get_voyage(self, voyage_id):
        """Returns the requested voyage, if no voyage is found returns None"""
        with open(self.file_name, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            
            for row in reader:
                if int(row["id"]) == voyage_id:
                    return Voyage(row["id"], row["sold_seats"], row["plane"], row["pilots"], row["attendants"], row["departure_flight"], row["arrival_flight"], row["date"], row["status"])

            # If no voyage is found with the given id, return None
            return None


    def get_all_voyages(self):
        """Returns a list of all voyages"""
        ret_list = []
        
        with open(self.file_name, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            
            for row in reader:
                ret_list.append(Voyage(row["id"], row["sold_seats"], row["plane"], row["pilots"], row["attendants"], row["departure_flight"], row["arrival_flight"], row["date"], row["status"]))
        
        return ret_list


    def update_voyage(self, voyage):
        """Updates the voyage with the given id"""
        # Makes temporary file to not overwrite the original file
        tempfile = NamedTemporaryFile(mode='w', delete=False)
        
        with open(self.file_name, 'r', newline='', encoding="utf-8") as csvfile, tempfile:
            fieldnames = ["id", "sold_seats", "plane", "pilots", "attendants", "departure_flight", "arrival_flight", "date", "status"]
            
            reader = csv.DictReader(csvfile)
            writer = csv.DictWriter(tempfile, fieldnames=fieldnames)

            # Writes the csv header into the tempfile
            writer.writeheader()
            
            for row in reader:
                # Writes the plane with the new data into the temp file
                if int(row["id"]) == voyage.id:
                    writer.writerow({'id': voyage.id, 'sold_seats': voyage.sold_seats, 'plane': voyage.plane, 'pilots': voyage.pilots, 'attendants': voyage.flight_attendants, 'departure_flight': voyage.departure_flight, 'arrival_flight': voyage.arrival_flight, 'date': voyage.date, 'status': voyage.status})
                
                # Writes the other planes unchanged 
                else:
                    writer.writerow({'id': row["id"], 'sold_seats': row["sold_seats"], 'plane': row["plane"], 'pilots': row["pilots"], 'attendants': row["attendants"], 'departure_flight': row["departure_flight"], 'arrival_flight': row["arrival_flight"], 'date': row["date"], 'status': row["status"]})

            # Replaces the main file with the tempfile
            shutil.move(tempfile.name, self.file_name)

    def delete_voyage(self, voyage_id):
        pass

