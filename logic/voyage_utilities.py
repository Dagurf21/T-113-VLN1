from logic import VoyageLogic, PlaneLogic, EmployeeLogic
from data.data_wrapper import DataWrapper

class VoyageUtilities:
    def __init__(self, data_connection: DataWrapper):
        self.voyage_logic = VoyageLogic(data_connection)
        self.plane_logic = PlaneLogic(data_connection)
        self.employee_logic = EmployeeLogic(data_connection)

    def assign_pilot_to_voyage(self, voyage_id: int, pilot_id: int) -> None:
        """Assigns a pilot to a voyage"""
        voyage = self.voyage_logic.get_voyage(voyage_id)
        voyage.pilots.append(pilot_id)
        self.voyage_logic.update_voyage(voyage)

        pilot = self.employee_logic.get_employee(pilot_id)
        pilot.assignments.append(voyage_id)
        self.employee_logic.update_employee(pilot)

    def assign_flight_attendant_to_voyage(self, voyage_id: int, attendant_id: int) -> None:
        """Assigns a flight attendant to a voyage"""
        voyage = self.voyage_logic.get_voyage(voyage_id)
        voyage.flight_attendants.append(attendant_id)
        self.voyage_logic.update_voyage(voyage)

        attendant = self.employee_logic.get_employee(attendant_id)
        attendant.assignments.append(voyage_id)
        self.employee_logic.update_employee(attendant)
        
    def assign_plane_to_voyage(self, plane_id: int, voyage_id: int) -> None:
        """Assigns a plane to a voyage"""
        plane = self.plane_logic.get_plane(plane_id)
        plane.voyages.append(voyage_id)
        self.plane_logic.update_plane(plane)

        voyage = self.voyage_logic.get_voyage(voyage_id)
        voyage.plane = plane_id
        self.voyage_logic.update_voyage(voyage)

    def man_voyage(self, voyage_id: int, pilots: list[int], attendants: list[int], plane_id: int) -> None:
        """Assigns pilots, attendants and a plane to a voyage"""
        for pilot in pilots:
            self.assign_pilot_to_voyage(voyage_id, pilot)

        for attendant in attendants:
            self.assign_flight_attendant_to_voyage(voyage_id, attendant)

        self.assign_plane_to_voyage(plane_id, voyage_id)

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

