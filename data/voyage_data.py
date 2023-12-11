from model.voyage import Voyage
import csv
from tempfile import NamedTemporaryFile
import shutil

class VoyageData:
    def __init__(self) -> None:
        self.file_name = "files/voyages.csv"
    

    def create_voyage(self, voyage) -> None:
        """Writes new voyage into the storage file"""
        with open(self.file_name, 'a', newline='', encoding="utf-8") as csvfile:
            fieldnames = ["id", "destination", "sold_seats", "plane","pilots", "attendants", "departure_flight", "arrival_flight", "date", "return_date", "status"]
            
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            id = self.get_new_id()
            
            writer.writerow({'id': id, 'destination': voyage.destination, 'sold_seats': voyage.sold_seats, 'plane': voyage.plane, 'pilots': voyage.pilots, 'attendants': voyage.flight_attendants, 'departure_flight': voyage.departure_flight, 'arrival_flight': voyage.arrival_flight, 'date': voyage.date, 'return_date': voyage.return_date, 'status': voyage.status})


    def get_new_id(self) -> int:
        """Returns a new id"""
        id = 0
        with open(self.file_name, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            
            for row in reader:
                id += 1

            return id


    def get_all_voyages(self) -> list["Voyage"]:
        """Returns a list of all voyages"""
        ret_list = []
        
        with open(self.file_name, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            
            for row in reader:
                ret_list.append(Voyage(id = int(row["id"]), destination = int(row["destination"]), sold_seats = int(row["sold_seats"]), plane = int(row["plane"]), pilots = row["pilots"], flight_attendants = row["attendants"], departure_flight = row["departure_flight"],arrival_flight = row["arrival_flight"], date = row["date"], return_date = row["return_date"], status = row["status"]))
        
        return ret_list


    def update_voyage(self, voyage) -> None:
        """Updates the voyage with the given id"""
        # Makes temporary file to not overwrite the original file
        tempfile = NamedTemporaryFile(mode='w', delete=False)
        
        with open(self.file_name, 'r', newline='', encoding="utf-8") as csvfile, tempfile:
            fieldnames = ["id", "destination", "sold_seats", "plane", "pilots", "attendants", "departure_flight", "arrival_flight", "date", "return_date", "status"]
            
            reader = csv.DictReader(csvfile)
            writer = csv.DictWriter(tempfile, fieldnames=fieldnames)

            # Writes the csv header into the tempfile
            writer.writeheader()
            
            for row in reader:
                # Writes the plane with the new data into the temp file
                if int(row["id"]) == voyage.id:
                    writer.writerow({'id': voyage.id, 'destination': voyage.destination, 'sold_seats': voyage.sold_seats, 'plane': voyage.plane, 'pilots': voyage.pilots, 'attendants': voyage.flight_attendants, 'departure_flight': voyage.departure_flight, 'arrival_flight': voyage.arrival_flight, 'date': voyage.date, 'return_date': voyage.return_date, 'status': voyage.status})
                
                # Writes the other planes unchanged 
                else:
                    writer.writerow({'id': row["id"], 'destination': row["destination"], 'sold_seats': row["sold_seats"], 'plane': row["plane"], 'pilots': row["pilots"], 'attendants': row["attendants"], 'departure_flight': row["departure_flight"], 'arrival_flight': row["arrival_flight"], 'date': row["date"], 'return_date': row["return_date"], 'status': row["status"]})

            # Replaces the main file with the tempfile
            shutil.move(tempfile.name, self.file_name)


    def cancel_voyage(self, voyage_id) -> None:
        """Cancels the voyage with the given id"""
        # Makes temporary file to not overwrite the original file
        tempfile = NamedTemporaryFile(mode='w', delete=False)

        with open(self.file_name, 'r', newline='', encoding="utf-8") as csvfile, tempfile:
            fieldnames = ["id", "destination", "sold_seats", "plane", "pilots", "attendants", "departure_flight", "arrival_flight", "date", "return_date", "status"]
            
            reader = csv.DictReader(csvfile)
            writer = csv.DictWriter(tempfile, fieldnames=fieldnames)
            
            # Writes the header to the tempfile
            writer.writeheader()

            # Looks for the voyage to cancel
            for row in reader:

                # If the voyage is found, it removes employees from voyage and changes status to cancelled
                if int(row["id"]) == voyage_id:
                    row = {'id': row["id"], 'destination': row["destination"], 'sold_seats': row["sold_seats"], 'plane': row["plane"], 'pilots': [], 'attendants': [], 'departure_flight': row["departure_flight"], 'arrival_flight': row["arrival_flight"], 'date': row["date"], 'return_date': row["return_date"], 'status': "Cancelled"}

                # Each row from the original file is written to the temporary file
                else:
                    row = {'id': row["id"], 'destination': row["destination"], 'sold_seats': row["sold_seats"], 'plane': row["plane"], 'pilots': row["pilots"], 'attendants': row["attendants"], 'departure_flight': row["departure_flight"], 'arrival_flight': row["arrival_flight"], 'date': row["date"], 'return_date': row["return_date"], 'status': row["status"]}
                
                writer.writerow(row)

        # The temporary file replaces the original file
        shutil.move(tempfile.name, self.file_name)
