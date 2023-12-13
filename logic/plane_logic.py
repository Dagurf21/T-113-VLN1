# import os
from copy import deepcopy
from data.data_wrapper import DataWrapper
from logic.voyage_logic import VoyageLogic
from model.plane import Plane


class PlaneLogic:
    """This is a Logic class for Plane"""

    def __init__(self, data_wrapper: DataWrapper) -> None:
        """Intitiatets plane with data_wrapper"""
        self.data_wrapper = data_wrapper
        self.voyage_logic = VoyageLogic(data_wrapper)

    def create_plane(self, plane) -> None:
        """Takes in plane data checks if ID is valid and forwards it to data layer"""
        if plane.capacity < 0:
            return
        
        for voyage_id in plane.voyages:
            voyage = self.voyage_logic.get_voyage(voyage_id)
            if voyage is None:
                return

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

        plane_to_update = self.get_plane(plane.id)

        if plane_to_update is None:
            return

        voyages_correct = True
        for voyage_id in plane.voyages:
            voyage = self.voyage_logic.get_voyage(voyage_id)
            if voyage is None:
                voyages_correct = False
        
        if voyages_correct:
            plane_to_update.voyages = deepcopy(plane.voyages)
        
        if plane.capacity > 0:
            plane_to_update.capacity = plane.capacity

        return self.data_wrapper.update_plane(plane_to_update)

    def delete_plane(self, id) -> None:
        """Removes a plane with specific ID"""
        return self.data_wrapper.delete_plane(id)
