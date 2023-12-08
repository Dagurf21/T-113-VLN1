# import os
from data.data_wrapper import DataWrapper
from model.plane import Plane

class PlaneLogic:
    """This is a Logic class for Plane"""

    def __init__(self, data_wrapper: DataWrapper):
        """Intitiatets plane with data_wrapper"""
        self.data_wrapper = data_wrapper

    def create_plane(self, plane) -> None:
        """Takes in plane data checks if ID is valid and forwards it to data layer"""
        
        if plane.id is None:
            self.data_wrapper.create_plane(plane)

        else:
            raise ValueError("Invalid Input")

    def list_all_planes(self) -> list[Plane]:
        """Gets list of all planes through data wrapper and forwards list of planes"""
        
        list_all_planes = self.data_wrapper.get_all_planes()

        return list_all_planes 

    def list_plane(self, id) -> Plane:
        """Gets info on a plane witha a specific ID and forwards data"""
        return self.data_wrapper.get_plane(id)

    def update_plane(self, id, plane) -> None:
        """Updates information of a plane with a specific ID"""

        plane.id = id

        return self.data_wrapper.update_plane(plane)

    def delete_plane(self, id) -> None:
        """Removes a plane with specific ID"""

        if True:
            return self.data_wrapper.delete_plane(id)

        else:
            raise ValueError("404 Invalid ID")
