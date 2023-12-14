from logic import FlightLogic, VoyageLogic
from model import Flight, FlightStatus

class FlightUtilities:
    def __init__(self, data_connection):
        self.flight_logic = FlightLogic(data_connection)
        self.voyage_logic = VoyageLogic(data_connection)

    def get_flight_status(self, flight) -> FlightStatus:
        '''Update's status on flight'''

        now = datetime.datetime.now()

        for voyage_id in flight.voyages:
            voyage = self.voyage_logic.get_voyage(voyage_id)

            if voyage.departure_date <= now.date() <= voyage.return_date:
                if voyage.departure_time <= now.time() <= voyage.return_departure_time:
                    return FlightStatus.InUse

        return FlightStatus.Available