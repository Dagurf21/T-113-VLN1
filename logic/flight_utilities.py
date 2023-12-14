from logic import FlightLogic, VoyageLogic
from model import Flight, FlightStatus

class FlightUtilities:
    def __init__(self, data_connection):
        self.flight_logic = FlightLogic(data_connection)
        self.voyage_logic = VoyageLogic(data_connection)

