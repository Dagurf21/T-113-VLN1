from model.plane import Plane
import csv
from tempfile import NamedTemporaryFile
import shutil

class PlaneData:
    def __init__(self) -> None:
        self.file_name = "files/planes.csv"
    

    def create_plane(self, plane) -> int:
        """Writes the new plane into the storage file"""
        with open(self.file_name, 'a', newline='', encoding="utf-8") as csvfile:
            fieldnames = ["id", "name", "type", "manufacturer", "capacity", "voyages"]
            
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            id = self.get_new_id()

            voyages = ".".join(str(id) for id in plane.voyages)
            writer.writerow({'id': id, 
                             'name': plane.name, 
                             'type': plane.ty, 
                             'manufacturer': plane.manufacturer, 
                             'capacity': plane.capacity, 
                             'voyages': '.'.join(voyages)
                            })
            
            return id


    def get_new_id(self) -> int:
        """Returns a new id"""
        id = 0
        
        with open(self.file_name, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            
            for row in reader:
                id += 1

            return id


    def get_all_planes(self) -> list["Plane"]:
        """Returns a list of all planes"""
        ret_list = []
        with open(self.file_name, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            
            for row in reader:
                if row["type"]:
                    voyages = [int(voyage) for voyage in row["voyages"].split(".") if voyage != ""]
                    
                    ret_list.append(Plane(
                        id = int(row["id"]), 
                        name = row["name"], 
                        ty = row["type"], 
                        manufacturer = row["manufacturer"], 
                        capacity = int(row["capacity"]), 
                        voyages = voyages))
    
        return ret_list


    def update_plane(self, plane) -> None:
        """Updates the plane with the given id"""
        # Makes temporary file to not overwrite the original file
        tempfile = NamedTemporaryFile(mode='w', delete=False)
        
        with open(self.file_name, 'r', newline='', encoding="utf-8") as csvfile, tempfile:
            fieldnames = ["id", "name", "type", "manufacturer", "capacity", "voyages"]
           
            reader = csv.DictReader(csvfile)
            writer = csv.DictWriter(tempfile, fieldnames=fieldnames)

            writer.writeheader()
            for row in reader:
                # Writes the plane with the new data into the temp file
                if int(row["id"]) == plane.id:
                    voyages = ".".join(str(id) for id in plane.voyages)

                    writer.writerow({'id': row["id"], 
                                     'name': plane.name, 
                                     'type': plane.ty, 
                                     'manufacturer': plane.manufacturer, 
                                     'capacity': plane.capacity, 
                                     'voyages': voyages})
                
                # Writes the other planes unchanged 
                else:
                    writer.writerow({'id': row["id"], 
                                     'name': row["name"], 
                                     'type': row["type"], 
                                     'manufacturer': row["manufacturer"], 
                                     'capacity': row["capacity"], 
                                     'voyages': row["voyages"]})
        
        # Replaces the main file with the tempfile
        shutil.move(tempfile.name, self.file_name)


    def delete_plane(self, plane_id) -> None:
        """Deletes the plane with the given id"""
        # Makes temporary file to not overwrite the original file
        tempfile = NamedTemporaryFile(mode='w', delete=False)

        with open(self.file_name, 'r', newline='', encoding="utf-8") as csvfile, tempfile:
            fieldnames = ["id", "name", "type", "manufacturer", "capacity", "voyages"]
            
            reader = csv.DictReader(csvfile)
            writer = csv.DictWriter(tempfile, fieldnames=fieldnames)
            
            # Writes the header to the tempfile
            writer.writeheader()

            # Looks for the plane to delete
            for row in reader:

                # If the plane is found, Everything except the id and name is erased
                if int(row["id"]) == plane_id:
                    row = {'id' : row["id"], 
                           'name' : row["name"], 
                           'type' : None, 
                           'manufacturer' : None, 
                           'capacity' : None, 
                           'voyages' : None}

                # Each row from the original file is written to the temporary file
                else:
                    row = {'id': row["id"], 
                           'name': row["name"], 
                           'type': row["type"], 
                           'manufacturer': row["manufacturer"], 
                           'capacity': row["capacity"], 
                           'voyages': row["voyages"]}
                
                writer.writerow(row)

        # The temporary file replaces the original file
        shutil.move(tempfile.name, self.file_name)
