#import os
from data.data_wrapper import DataWrapper
from model.plane import Plane

class PlaneLogic:
    ''' '''

    def __init__(self):
        ''' '''
        self.plane = Plane()

    def create_plane(self, data) -> None:
        ''' '''
        
        

        pass

    def list_all_planes(self) -> list: # Plane
        ''' '''
        all_planes = DataWrapper.get_all_planes()
        return all_planes
    
    def list_plane(self, id): # Plane
        ''' '''
        plane = DataWrapper.get_plane(id)
        
        return plane

        return
    
    def update_plane(self, id) -> None:
        ''' '''
        pass
    
    def delete_plane(self, id) -> None:
        ''' '''
        pass
