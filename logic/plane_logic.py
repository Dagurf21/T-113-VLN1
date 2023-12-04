#import os
from data.data_wrapper import Data_Wrapper

class Plane_logic(Data_Wrapper):

    def __init__(self):
        
        self.id: int
        self.name: str
        self.__password: str
        self.address: str
        self.ssn: str
        self.mobil_phone: str
        self.email: str
        self.home_phone:str  # Optional

        pass

    def create_plane(self, data) -> None:
        
        pass

    def list_all_planes(self) -> list: # Plane
        Data_Wrapper.get_all_planes()
        return []
    
    def list_plane(self, id): # Plane
        return
    
    def update_plane(self, id) -> None:
        pass
    
    def delete_plane(self, id) -> None:
        pass
