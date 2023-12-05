#import os
from data.data_wrapper import DataWrapper
from model.plane import Plane

class PlaneLogic:
    ''' '''

    def __init__(self, data_wrapper):
        ''' '''
        pass

    def create_plane(self, data) -> None:
        ''' '''
        
        Plane = self.data_wrapper.plane

        if Plane.id == None:
            raise ValueError("Invalid Input")
        
        else:
            self.data_wrapper.create_plane(data)

        pass

    def list_all_planes(self) -> list: # Plane
        ''' '''
        all_planes = DataWrapper.get_all_planes()
        return all_planes
    
    def list_plane(self, id): # Plane
        ''''''
        return self.data_wrapper.get_all_planes
    
    def update_plane(self, id) -> None:
        ''' '''
        pass
    
    def delete_plane(self, id) -> None:
        ''' '''
        pass
