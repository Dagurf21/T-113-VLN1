from logic import VoyageLogic, PlaneLogic

class VoyageUtilities:
    def __init__(self, data_connection):
        self.voyage_logic = VoyageLogic(data_connection)
        self.plane_logic = PlaneLogic(data_connection)

    def assign_pilot_to_voyage(self, voyage_id, pilot_id):
        voyage = self.voyage_logic.get_voyage(voyage_id)
        voyage.pilots.append(pilot_id)
        self.voyage_logic.update_voyage(voyage)
        
    def assign_plane_to_voyage(self, plane_id, voyage_id):
        plane = self.plane_logic.get_plane(plane_id)
        plane.voyages.append(voyage_id)
        self.plane_logic.update_plane(plane)
        voyage = self.voyage_logic.get_voyage(voyage_id)
        voyage.plane = plane_id
        self.voyage_logic.update_voyage(voyage)

