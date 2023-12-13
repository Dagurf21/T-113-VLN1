# import os
from data.data_wrapper import DataWrapper
from logic.voyage_logic import VoyageLogic
from model.plane import Plane


class PlaneLogic:
    """This is a Logic class for Plane"""

    def __init__(self, data_wrapper: DataWrapper, voyage_logic: VoyageLogic) -> None:
        """Intitiatets plane with data_wrapper"""
        self.data_wrapper = data_wrapper
        self.voyage_logic = voyage_logic

    def create_plane(self, plane) -> None:
        """Takes in plane data checks if ID is valid and forwards it to data layer"""
        if plane.capacity < 0:
            return
        
        # TODO: Validate voyages

        if plane.id is None:
            self.data_wrapper.create_plane(plane)

    def get_all_planes(self) -> list[Plane]:
        """Gets list of all planes through data wrapper and forwards list of planes"""
        return self.data_wrapper.get_all_planes()

    def get_plane(self, search_id) -> Plane:
        """Gets info on a plane witha a specific ID and forwards data"""
        plane_list = self.get_all_planes()

        for plane in plane_list:
            if plane.id == search_id:
                return plane
        return None

    def update_plane(self, plane) -> None:
        """Updates information of a plane with a specific ID"""
        return self.data_wrapper.update_plane(plane)

    def delete_plane(self, id) -> None:
        """Removes a plane with specific ID"""
        return self.data_wrapper.delete_plane(id)
