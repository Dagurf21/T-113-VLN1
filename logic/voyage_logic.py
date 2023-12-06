from model.voyage import Voyage


class VoyageLogic:
    """This class handles all the logic for the Voyage class."""

    def __init__(self, data_connection) -> None:
        self.data_wrapper = data_connection

    def create_voyage(self, voyage) -> None:
        """Takes in a voyage object and forwards it to the data layer"""
        seats_available = voyage.plane.capacity - voyage.seats_sold

        if seats_available <= 0:
            raise ValueError("Plane is FULL (0 available seats)")

        return self.data_wrapper.create_voyage(voyage)

    def list_all_voyages(self) -> list:
        """Returns a list of all voyages"""
        return self.data_wrapper.get_all_voyages()

    def list_voyage(self, id):
        """Returns a voyage object with the given id"""
        return self.data_wrapper.get_voyage(id)

    def update_voyage(self, voyage) -> None:
        """Updates a voyage object with the given id"""
        return self.data_wrapper.update_voyage(voyage)

    def delete_voyage(self, id) -> None:
        """Deletes a voyage object with the given id"""
        return self.data_wrapper.delete_voyage(id)

    def validate_voyage(self, voyage) -> Voyage:
        """Validates a voyage and return a validated
        voyage if possible, else None"""
        seats_available = voyage.plane.capacity - voyage.seats_sold

    def validate_job_position(self, employee_list, job_title) -> bool:
        """Goes through a list of employees and verifies
        if all of them are the given job_title"""
        for employee in employee_list:
            if type(employee).__name__ != job_title:
                return False
        return True


# Verify:
#
# if country is allowed based on assignment description
#
#
