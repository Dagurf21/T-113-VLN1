from model.flight import Flight
import csv
from tempfile import NamedTemporaryFile
import shutil
import datetime

class FlightData:
    def __init__(self) -> None:
        self.file_name = "files/flights.csv"
    

    def create_flight(self, flight) -> None:
        """Writes a new flight to the storage file"""
        with open(self.file_name, 'a', newline='', encoding="utf-8") as csvfile:
            fieldnames = ["flight_nr", "departure", "destination", "date", "departure_time", "arrival_time"]

            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writerow({'flight_nr': flight.flight_number, 
                             'departure': flight.departure, 
                             'destination': flight.destination, 
                             'date': flight.date, 
                             'departure_time': flight.departure_time, 
                             'arrival_time': flight.arrival_time})

            return flight.flight_number


    def get_all_flights(self) -> list["Flight"]:
        """Returns a list of all flights"""
        ret_list = []
        
        with open(self.file_name, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            
            for row in reader:
                year, month, day = self.split_date(row["date"])
                date = datetime.date(year = year, month = month, day = day)
                departure_hour, departure_minute = self.split_time(row["departure_time"])
                arrival_hour, arrival_minute = self.split_time(row["arrival_time"])
                ret_list.append(
                    Flight(
                        flight_number = row["flight_nr"], 
                        departure = int(row["departure"]), 
                        destination = int(row["destination"]), 
                        date = date, 
                        departure_time = datetime.time(hour = departure_hour, minute = departure_minute), 
                        arrival_time = datetime.time(hour = arrival_hour, minute = arrival_minute)))
        
        return ret_list


    def split_date(self, date) -> tuple[int, int, int]:
        """Splits date into year, month and day and returns them as ints"""
        year, month, day = date.split("-")
        return int(year), int(month), int(day)


    def split_time(self, time) -> tuple[int, int]:
        """Splits time into hour, minute and seconds
        and returns hour and minute as ints"""
        hour, minute, second = time.split(":")
        return int(hour), int(minute)


    def update_flight(self, flight) -> None:
        """Updates the flight with the given id"""
        # Makes temporary file to not overwrite the original file
        tempfile = NamedTemporaryFile(mode='w', delete=False)
        
        with open(self.file_name, 'r', newline='', encoding="utf-8") as csvfile, tempfile:
            fieldnames = ["flight_nr", "departure", "destination", "date", "departure_time", "arrival_time"]
            
            reader = csv.DictReader(csvfile)
            writer = csv.DictWriter(tempfile, fieldnames=fieldnames)

            writer.writeheader()
            for row in reader:
                # Writes the flight with the new data into the temp file
                if row["flight_nr"] == flight.flight_number:
                    writer.writerow({'flight_nr': flight.flight_number, 
                                     'departure': flight.departure, 
                                     'destination': flight.destination, 
                                     'departure_time': flight.departure_time, 
                                     'arrival_time': flight.arrival_time})
                
                # Writes the other flights unchanged 
                else:
                    writer.writerow({'flight_nr': row["flight_nr"], 
                                     'departure': row["departure"], 
                                     'destination': row["destination"], 
                                     'departure_time': row["departure_time"], 
                                     'arrival_time': row["arrival_time"]})

        # Replaces the main file with the tempfile
        shutil.move(tempfile.name, self.file_name)
