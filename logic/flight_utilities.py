from logic import PlaneLogic, VoyageLogic
from model import Plane, PlaneStatus
import datetime

class FlightUtilities:
    def __init__(self, data_connection):
        self.plane_logic = PlaneLogic(data_connection)
        self.voyage_logic = VoyageLogic(data_connection)

    def get_plane_status(self, plane: Plane) -> PlaneStatus:
        """Returns the status of the plane"""

        now = datetime.datetime.now()

        for voyage_id in plane.voyages:
            voyage = self.voyage_logic.get_voyage(voyage_id)

            if not (voyage.departure_date <= now.date() <= voyage.return_date):
                continue

            if not (voyage.departure_time <= now.time() <= voyage.return_departure_time):
                continue

            return PlaneStatus.InUse

        return PlaneStatus.Available