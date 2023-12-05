from model.plane import Plane
import csv
from tempfile import NamedTemporaryFile
import shutil

class Plane_Data:
    def __init__(self) -> None:
        self.file_name = "files/planes.csv"
    

    def create_plane(self, plane):
        with open(self.file_name, 'a', newline='', encoding="utf-8") as csvfile:
            fieldnames = ["id", "name", "type", "manufacturer", "capacity", "flights"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            id = self.get_new_id()
            writer.writerow({'id': id, 'name': plane.name, 'type': plane.type, 'manufacturer': plane.manufacturer, 'capacity': plane.capacity, 'flights': plane.flights})


    def get_new_id(self) -> int:
        """Returns a new id"""
        id = 0
        with open(self.file_name, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                id += 1

            return id


    def get_plane(self, plane_id):
        with open(self.file_name, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if int(row["id"]) == plane_id:
                    return Plane(row["id"], row["plane_type"], row["manufacturer"], row["capacity"], row["flights"])
        
            # If no plane is found with the given id, return None
            return None


    def get_all_planes(self):
        ret_list = []
        with open(self.file_name, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                ret_list.append(Plane(row["id"], row["plane_type"], row["manufacturer"], row["capacity"], row["flights"]))
        return ret_list


    def update_plane(self, plane):
        """Updates the plane with the given id"""
        # Makes temporary file to not overwrite the original file
        tempfile = NamedTemporaryFile(mode='w', delete=False)
        with open(self.file_name, 'r', newline='', encoding="utf-8") as csvfile, tempfile:
            fieldnames = ["id", "name", "type", "manufacturer", "capacity", "flights"]
            reader = csv.DictReader(csvfile, fieldnames=fieldnames)
            writer = csv.DictWriter(tempfile, fieldnames=fieldnames)

            for row in reader:
                if int(row["id"]) == plane.id:
                    writer.writerow({'id': plane.id, 'name': plane.name, 'type': plane.type, 'manufacturer': plane.manufacturer, 'capacity': plane.capacity, 'flights': plane.flights})
                else:
                    writer.writerow({'id': row["id"], 'name': row["name"], 'type': row["type"], 'manufacturer': row["manufacturer"], 'capacity': row["capacity"], 'flights': row["flights"]})
        
        shutil.move(tempfile.name, self.file_name)


    def delete_plane(self, plane_id):
        pass


