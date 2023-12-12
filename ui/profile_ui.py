from ui import UIWidget, UICancelException
from model import Employee, Pilot, Manager, FlightAttendant, FlightManager, Voyage, Destination, Flight
from logic import LogicWrapper

class Profile(UIWidget):
    def __init__(self, user: Employee, logic_wrapper: LogicWrapper):
        self.user = user
        self.logic_wrapper = logic_wrapper

    def show(self):
        while True:
            try:
                pass
            except UICancelException:
                return
            
    def get_voyages_in_this_week():
        pass