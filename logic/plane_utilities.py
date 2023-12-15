from logic import PlaneLogic, VoyageLogic, DestinationLogic, FlightLogic
from model import Plane, PlaneStatus, Flight, Voyage
import datetime

class PlaneUtilities:
    def __init__(self, data_connection):
        self.plane_logic = PlaneLogic(data_connection)
        self.voyage_logic = VoyageLogic(data_connection)
        self.destination_logic = DestinationLogic(data_connection)
        self.flight_logic = FlightLogic(data_connection)

    def get_plane_status(self, plane: Plane) -> PlaneStatus:
        """Returns the status of the plane"""

        now = datetime.datetime.now()

        for voyage_id in plane.voyages:
            voyage = self.voyage_logic.get_voyage(voyage_id)

            if voyage.departure_date > now.date():
                continue

            if voyage.departure_date == now.date() and voyage.departure_time > now.time():
                continue

            if voyage.return_date < now.date():
                continue

            if voyage.return_date == now.date() and voyage.return_departure_time > now.time():
                continue
                
            destination = self.destination_logic.get_destination(voyage.destination)
            flight_time = datetime.timedelta(minutes=destination.flight_time)

            arrival_time = self.add_to_time(voyage.departure_time, flight_time)
            return_arrival_time = self.add_to_time(voyage.return_departure_time, flight_time)

            if voyage.departure_date == now.date() and voyage.departure_time <= now.time() <= arrival_time:
                return PlaneStatus.InFlight
            
            if voyage.return_date == now.date() and voyage.return_departure_time <= now.time() <= return_arrival_time:
                return PlaneStatus.InFlight

            return PlaneStatus.InUse

        return PlaneStatus.Available
    
    def get_plane_active_flight(self, plane: Plane) -> Flight | None:
        """Gets the current voyage the plane is on if any"""

        now = datetime.datetime.now()

        for voyage_id in plane.voyages:
            voyage = self.voyage_logic.get_voyage(voyage_id)

            if voyage.departure_date > now.date():
                continue

            if voyage.departure_date == now.date() and voyage.departure_time > now.time():
                continue

            if voyage.return_date < now.date():
                continue

            if voyage.return_date == now.date() and voyage.return_departure_time > now.time():
                continue
                
            destination = self.destination_logic.get_destination(voyage.destination)
            flight_time = datetime.timedelta(minutes=destination.flight_time)

            arrival_time = self.add_to_time(voyage.departure_time, flight_time)
            return_arrival_time = self.add_to_time(voyage.return_departure_time, flight_time)

            if voyage.departure_date == now.date() and voyage.departure_time <= now.time() <= arrival_time:
                return self.flight_logic.get_flight(voyage.departure_flight, voyage.departure_date)
            
            if voyage.return_date == now.date() and voyage.return_departure_time <= now.time() <= return_arrival_time:
                return self.flight_logic.get_flight(voyage.return_flight, voyage.return_date)

        return None

    def get_plane_active_voyage(self, plane: Plane) -> Voyage | None:
        """Gets the current voyage the plane is on if any"""

        now = datetime.datetime.now()

        for voyage_id in plane.voyages:
            voyage = self.voyage_logic.get_voyage(voyage_id)

            if voyage.departure_date > now.date():
                continue

            if voyage.departure_date == now.date() and voyage.departure_time > now.time():
                continue

            if voyage.return_date < now.date():
                continue

            if voyage.return_date == now.date() and voyage.return_departure_time > now.time():
                continue
                
            return voyage

        return None
    
    def add_to_time(self, time: datetime.time, time_delta: datetime.timedelta) -> datetime.datetime:
        as_datetime = datetime.datetime(1, 1, 1, time.hour, time.minute, time.second)
        return (as_datetime + time_delta).time()
