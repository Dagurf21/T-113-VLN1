from logic import FlightLogic, VoyageLogic
from model import Flight, FlightStatus

class FlightUtilities:
    def __init__(self, data_connection):
        self.flight_logic = FlightLogic(data_connection)
        self.voyage_logic = VoyageLogic(data_connection)

    def get_flight_status(self, flight) -> Flight:
        '''Update's status on flight'''

        now = datetime.datetime.now()

        match now:
            case flight.date:
                return FlightStatus.InUse
            
            case other:
                return FlightStatus.Available

        raise NotImplementedError