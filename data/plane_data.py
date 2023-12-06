from model.plane import Plane
import csv
from tempfile import NamedTemporaryFile
import shutil

class PlaneData:
    def __init__(self) -> None:
        self.file_name = "files/planes.csv"
    

    def create_plane(self, plane):
        """Writes the new plane into the storage file"""
        with open(self.file_name, 'a', newline='', encoding="utf-8") as csvfile:
            fieldnames = ["id", "name", "type", "manufacturer", "capacity", "flights"]
            
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            id = self.get_new_id()
            
            writer.writerow({'id': id, 'name': plane.name, 'type': plane.ty, 'manufacturer': plane.manufacturer, 'capacity': plane.capacity, 'flights': plane.flights})


    def get_new_id(self) -> int:
        """Returns a new id"""
        id = 0
        
        with open(self.file_name, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            
            for row in reader:
                id += 1

            return id


    def get_plane(self, plane_id):
        """Returns the requested plane, if no plane is found returns None"""
        with open(self.file_name, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            
            for row in reader:
                if int(row["id"]) == plane_id:
                    return Plane(int(row["id"]), row["plane_type"], row["manufacturer"], int(row["capacity"]), row["flights"])
        
            # If no plane is found with the given id, return None
            return None


    def get_all_planes(self):
        """Returns a list of all planes"""
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
                # Writes the plane with the new data into the temp file
                if int(row["id"]) == plane.id:
                    writer.writerow({'id': plane.id, 'name': plane.name, 'type': plane.ty, 'manufacturer': plane.manufacturer, 'capacity': plane.capacity, 'flights': plane.flights})
                
                # Writes the other planes unchanged 
                else:
                    writer.writerow({'id': row["id"], 'name': row["name"], 'type': row["type"], 'manufacturer': row["manufacturer"], 'capacity': row["capacity"], 'flights': row["flights"]})
        
        # Replaces the main file with the tempfile
        shutil.move(tempfile.name, self.file_name)


    def delete_plane(self, plane_id):
        pass


