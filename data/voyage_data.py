from model.voyage import Voyage
import csv
from tempfile import NamedTemporaryFile
import shutil
import datetime

class VoyageData:
    def __init__(self) -> None:
        self.file_name = "files/voyages.csv"
    

    def create_voyage(self, voyage: Voyage) -> int:
        """Writes new voyage into the storage file"""
        with open(self.file_name, 'a', newline='', encoding="utf-8") as csvfile:
            fieldnames = [
                "id",
                "destination",
                "sold_seats",
                "plane",
                "pilots",
                "attendants",
                "departure_time",
                "departure_flight",
                "arrival_departure_time",
                "arrival_flight",
                "date",
                "return_date",
                "status"
            ]
            
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            id = self.get_new_id()
            pilots_csv_list = ".".join(str(id) for id in voyage.pilots)
            attendants_csv_list = ".".join(str(id) for id in voyage.flight_attendants)
            writer.writerow({
				'id': id,
				'destination': voyage.destination,
				'sold_seats': voyage.sold_seats,
				'plane': voyage.plane,
				'pilots': pilots_csv_list,
				'attendants': attendants_csv_list,
				'departure_time': voyage.departure_time,
				'departure_flight': voyage.departure_flight,
				'arrival_departure_time': voyage.return_departure_time,
				'arrival_flight': voyage.return_flight,
				'date': voyage.departure_date,
				'return_date': voyage.return_date,
				'status': voyage.status
            })
            
            return id


    def get_new_id(self) -> int:
        """Returns a new id"""
        id = 0
        with open(self.file_name, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            
            for _ in reader:
                id += 1

            return id


    def get_all_voyages(self) -> list["Voyage"]:
        """Returns a list of all voyages"""
        ret_list = []
        
        with open(self.file_name, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                dep_year, dep_month, dep_day = self.split_date(row["date"])
                ret_year, ret_month, ret_day = self.split_date(row["return_date"])

                dep_hour, dep_minute = self.split_time(row["departure_time"])
                ret_hour, ret_minute = self.split_time(row["arrival_departure_time"])

                pilots_list = [int(pilot) for pilot in row["pilots"].split(".") if pilot != ""]
                attendants_list = [int(attendant) for attendant in row["attendants"].split(".") if attendant != ""]

                ret_list.append(Voyage(
                    id = int(row["id"]), 
                    destination = int(row["destination"]), 
                    sold_seats = int(row["sold_seats"]), 
                    plane = int(row["plane"]), 
                    pilots = pilots_list, 
                    flight_attendants = attendants_list, 
                    departure_time = datetime.time(hour = dep_hour, minute = dep_minute), 
                    departure_flight = row["departure_flight"], 
                    return_departure_time = datetime.time(hour = ret_hour, minute = ret_minute), 
                    return_flight = row["arrival_flight"], 
                    departure_date = datetime.date(year = dep_year, month = dep_month, day = dep_day), 
                    return_date = datetime.date(year = ret_year, month = ret_month, day = ret_day), 
                    status = row["status"],
                ))
        
        return ret_list


    def split_date(self, date: str) -> (int, int, int):
        """Splits the date string into year, month and day integers"""
        year, month, day = date.split("-")

        return int(year), int(month), int(day)


    def split_time(self, time: str) -> (int, int):
        """Splits the time string into hour, minute and second 
        and returns the hour and minute as int"""
        hour, minute, second = time.split(":")

        return int(hour), int(minute)


    def update_voyage(self, voyage: Voyage) -> None:
        """Updates the voyage with the given id"""
        # Makes temporary file to not overwrite the original file
        tempfile = NamedTemporaryFile(mode='w', delete=False)
        
        with open(self.file_name, 'r', newline='', encoding="utf-8") as csvfile, tempfile:
            fieldnames = [
                "id",
                "destination",
                "sold_seats",
                "plane",
                "pilots",
                "attendants",
                "departure_time",
                "departure_flight",
                "arrival_departure_time",
                "arrival_flight",
                "date",
                "return_date",
                "status"
            ]
            
            reader = csv.DictReader(csvfile)
            writer = csv.DictWriter(tempfile, fieldnames = fieldnames)

            # Writes the csv header into the tempfile
            writer.writeheader()
            
            for row in reader:
                # Writes the plane with the new data into the temp file
                if int(row["id"]) == voyage.id:
                    pilots_csv_list = ".".join(str(id) for id in voyage.pilots)
                    attendants_csv_list = ".".join(str(id) for id in voyage.flight_attendants)
                    
                    row = {
                        'id': row["id"],
                        'destination': voyage.destination,
                        'sold_seats': voyage.sold_seats,
                        'plane': voyage.plane,
                        'pilots': pilots_csv_list,
                        'attendants': attendants_csv_list,
                        'departure_time': voyage.departure_time,
                        'departure_flight': voyage.departure_flight,
                        'arrival_departure_time': voyage.return_departure_time,
                        'arrival_flight': voyage.return_flight,
                        'date': voyage.departure_date,
                        'return_date': voyage.return_date,
                        'status': voyage.status
                    }

                # Writes the other planes unchanged 
                else:
                    row = {
                        'id': row["id"],
                        'destination': row["destination"],
                        'sold_seats': row["sold_seats"],
                        'plane': row["plane"],
                        'pilots': row["pilots"],
                        'attendants': row["attendants"],
                        'departure_time': row["departure_time"],
                        'departure_flight': row["departure_flight"],
                        'arrival_departure_time': row["arrival_departure_time"],
                        'arrival_flight': row["arrival_flight"],
                        'date': row["date"],
                        'return_date': row["return_date"],
                        'status': row["status"]
                    }

                writer.writerow(row)

        # Replaces the main file with the tempfile
        shutil.move(tempfile.name, self.file_name)


    def cancel_voyage(self, voyage_id) -> None:
        """Cancels the voyage with the given id"""
        # Makes temporary file to not overwrite the original file
        tempfile = NamedTemporaryFile(mode='w', delete=False)

        with open(self.file_name, 'r', newline='', encoding="utf-8") as csvfile, tempfile:
            fieldnames = [
                "id",
                "destination",
                "sold_seats",
                "plane",
                "pilots",
                "attendants",
                "departure_time",
                "departure_flight",
                "arrival_departure_time",
                "arrival_flight",
                "date",
                "return_date",
                "status"
            ]
            
            reader = csv.DictReader(csvfile)
            writer = csv.DictWriter(tempfile, fieldnames=fieldnames)
            
            # Writes the header to the tempfile
            writer.writeheader()

            # Looks for the voyage to cancel
            for row in reader:

                # If the voyage is found, it removes employees from voyage and changes status to cancelled
                if int(row["id"]) == voyage_id:
                    row = {
                        'id': row["id"],
                        'destination': row["destination"],
                        'sold_seats': row["sold_seats"],
                        'plane': row["plane"],
                        'pilots': [],
                        'attendants': [],
                        'departure_time': row["departure_time"],
                        'departure_flight': row["departure_flight"],
                        'arrival_departure_time': row["arrival_departure_time"],
                        'arrival_flight': row["arrival_flight"],
                        'date': row["date"],
                        'return_date': row["return_date"],
                        'status': "Cancelled"
                    }

                # Each row from the original file is written to the temporary file
                else:
                    row = {
                        'id': row["id"],
                        'destination': row["destination"],
                        'sold_seats': row["sold_seats"],
                        'plane': row["plane"],
                        'pilots': row["pilots"],
                        'attendants': row["attendants"],
                        'departure_time': row["departure_time"],
                        'departure_flight': row["departure_flight"],
                        'arrival_departure_time': row["arrival_departure_time"],
                        'arrival_flight': row["arrival_flight"],
                        'date': row["date"],
                        'return_date': row["return_date"],
                        'status': row["status"]
                    }
                
                writer.writerow(row)

        # The temporary file replaces the original file
        shutil.move(tempfile.name, self.file_name)
