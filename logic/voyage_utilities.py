from copy import copy
import datetime
from logic import VoyageLogic, PlaneLogic, EmployeeLogic
from data.data_wrapper import DataWrapper

class VoyageUtilities:
    def __init__(self, data_connection: DataWrapper):
        self.voyage_logic = VoyageLogic(data_connection)
        self.plane_logic = PlaneLogic(data_connection)
        self.employee_logic = EmployeeLogic(data_connection)

    def assign_plane_to_voyage(self, plane_id: int, voyage_id: int) -> None:
        """Assigns a plane to a voyage"""
        plane = self.plane_logic.get_plane(plane_id)
        plane.voyages.append(voyage_id)
        self.plane_logic.update_plane(plane)

        voyage = self.voyage_logic.get_voyage(voyage_id)
        voyage.plane = plane_id
        self.voyage_logic.update_voyage(voyage)

    def create_voyage(
        self,
        plane_id: int,
        destination_id: int,
        date: datetime.date,
        return_departure_date: datetime.date,
        departure_time: datetime.time,
        return_departure_time: datetime.time,
        sold_seats: int,
        flight_attendants: list[int],
        pilots: list[int],
    ) -> None:
        """Creates a voyage then assigns pilots, attendants and a plane to it"""

        voyage_id = self.voyage_logic.create_voyage(
            plane_id,
            destination_id,
            date,
            return_departure_date,
            departure_time,
            return_departure_time,
            sold_seats
        )

        for pilot in pilots:
            self.staff_voyage_pilot(voyage_id, pilot)

        for attendant in flight_attendants:
            self.staff_voyage_attendant(voyage_id, attendant)

        self.assign_plane_to_voyage(plane_id, voyage_id)
    
    def delete_voyage(self, voyage_id: int) -> None:
        """Unassigns all pilots, attendants and plane from the voyage and then deletes it"""
        voyage = self.voyage_logic.get_voyage(voyage_id)
        pilots = copy(voyage.pilots)
        attendants = copy(voyage.flight_attendants)

        for pilot in pilots:
            self.unstaff_voyage_pilot(pilot)

        for attendant in attendants:
            self.unstaff_voyage_attendant(attendant)

        plane = self.plane_logic.get_plane(voyage.plane)
        plane.voyages.remove(voyage_id)
        self.plane_logic.update_plane(plane)

        self.voyage_logic.delete_voyage(voyage_id)

    def staff_voyage_pilot(self, voyage_id: int, new_staff: int):
        """Adds a single pilot to a voyage"""
        voyage = self.voyage_logic.get_voyage(voyage_id)
        voyage.pilots.append(new_staff)
        self.logic_wrapper.update_voyage(voyage)

        assigned_pilot = self.logic_wrapper.get_employee(new_staff)
        assigned_pilot.assignments.append(voyage.id)
        self.logic_wrapper.update_employee(assigned_pilot)

    def staff_voyage_attendant(self, voyage_id: int, new_staff: int):
        """Adds a single attendant to a voyage"""
        voyage = self.voyage_logic.get_voyage(voyage_id)
        voyage.pilots.append(new_staff)
        self.logic_wrapper.update_voyage(voyage)

        assigned_attendant = self.logic_wrapper.get_employee(new_staff)
        assigned_attendant.assignments.append(voyage.id)
        self.logic_wrapper.update_employee(assigned_attendant)


    def unstaff_voyage_pilot(self, voyage_id: int, staff_to_remove: int):
        """Removed a pilot from a voyage"""
        voyage = self.voyage_logic.get_voyage(voyage_id)
        voyage.pilots.remove(int(staff_to_remove))
        self.logic_wrapper.update_voyage(voyage)

        assigned_pilot = self.logic_wrapper.get_employee(staff_to_remove)
        assigned_pilot.assignments.remove(voyage.id)
        self.logic_wrapper.update_employee(assigned_pilot)

    def unstaff_voyage_attendant(self, voyage_id, staff_to_remove: int):
        """Removes an attendant from a voyage"""
        voyage = self.voyage_logic.get_voyage(voyage_id)
        voyage.flight_attendants.remove(int(staff_to_remove))
        self.logic_wrapper.update_voyage(voyage)

        assigned_attendant = self.logic_wrapper.get_employee(staff_to_remove)
        assigned_attendant.assignments.remove(voyage.id)
        self.logic_wrapper.update_employee(assigned_attendant)

