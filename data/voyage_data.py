from model.voyage import Voyage
import csv
from tempfile import NamedTemporaryFile
import shutil

class VoyageData:
    def __init__(self) -> None:
        self.file_name = "files/voyages.csv"
    

    def create_voyage(self, voyage):
        with open(self.file_name, 'a', newline='', encoding="utf-8") as csvfile:
            fieldnames = ["id", "sold_seats", "plane", "departure_flight", "arrival_flight", "date"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            id = self.get_new_id()
            writer.writerow({'id': id, 'sold_seats': voyage.sold_seats, 'plane': voyage.plane, 'departure_flight': voyage.departure_flight, 'arrival_flight': voyage.arrival_flight, 'date': voyage.date})


    def get_new_id(self) -> int:
        """Returns a new id"""
        id = 0
        with open(self.file_name, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                id += 1

            return id


    def get_voyage(self, voyage_id):
        with open(self.file_name, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if int(row["id"]) == voyage_id:
                    return Voyage(row["id"], row["sold_seats"], row["plane"], row["departure_flight"], row["arrival_flight"], row["date"])

            # If no voyage is found with the given id, return None
            return None

    def get_all_voyages(self):
        ret_list = []
        with open(self.file_name, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                ret_list.append(Voyage(row["id"], row["sold_seats"], row["plane"], row["departure_flight"], row["arrival_flight"], row["date"]))
        return ret_list


    def update_voyage(self, voyage):
        """Updates the voyage with the given id"""
        # Makes temporary file to not overwrite the original file
        tempfile = NamedTemporaryFile(mode='w', delete=False)
        with open(self.file_name, 'r', newline='', encoding="utf-8") as csvfile, tempfile:
            fieldnames = ["id", "sold_seats", "plane", "departure_flight", "arrival_flight", "date"]
            reader = csv.DictReader(csvfile, fieldnames=fieldnames)
            writer = csv.DictWriter(tempfile, fieldnames=fieldnames)

            for row in reader:
                if int(row["id"]) == voyage.id:
                    writer.writerow({'id': voyage.id, 'sold_seats': voyage.sold_seats, 'plane': voyage.plane, 'departure_flight': voyage.departure_flight, 'arrival_flight': voyage.arrival_flight, 'date': voyage.date})
                else:
                    writer.writerow({'id': row["id"], 'sold_seats': row["sold_seats"], 'plane': row["plane"], 'departure_flight': row["departure_flight"], 'arrival_flight': row["arrival_flight"], 'date': row["date"]})


    def delete_voyage(self, voyage_id):
        pass

