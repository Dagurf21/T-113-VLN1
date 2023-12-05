#import os
from data.data_wrapper import DataWrapper
from model.plane import Plane

class PlaneLogic:
    '''This is a Logic class for Plane'''

    def __init__(self, data_wrapper):
        '''Intitiatets plane with data_wrapper'''
        pass

    def create_plane(self, data) -> None:
        '''Takes in plane data checks if ID is valid and forwards it to data layer'''
        Plane = self.data_wrapper.plane

        if Plane.id == None:
            raise ValueError("Invalid Input")
        
        else:
            self.data_wrapper.create_plane(data)

    def list_all_planes(self) -> list[Plane]:
        '''Gets list of all planes through data wrapper and forwards list of planes'''
        return self.data_wrapper.get_all_planesS
    
    def list_plane(self, id) -> Plane:
        '''Gets info on a plane witha a specific ID and forwards data'''
        return self.data_wrapper.get_plane(id)
    
    def update_plane(self, id) -> None:
        '''Updates information of a plane with a specific ID'''
        self.data_wrapper.update_plane(id, data)
    
    def delete_plane(self, id) -> None:
        '''Removes a plane with specific ID'''
        self.data_wrapper.delete_plane
