from logic.validator_logic import Validator

VALIDATION_ERRORS = (
    "Invalid Destination or Airport. ",
    "Invalid Distance. ",
    "Invalid Flight Time. ",
    "Invalid Emergency Number. ",
)


class DestinationLogic:
    """This class is the logic layer for the destination class"""

    def __init__(self, data_connection):
        self.data_wrapper = data_connection
        self.validate = Validator()

    def create_destination(self, destination):
        """Takes in a destination object and forwards it to the data layer"""
        error_check = self.validate_destination(destination)
        if error_check is "":
            return self.data_wrapper.create_destination(destination)
        else:
            raise ValueError(error_check)

    def list_all_destinations(self) -> list:  # List of Destinations
        """Returns a list of all destinations"""
        # sorting tomfoolery
        return self.data_wrapper.get_all_destinations()

    def get_destination(self, id):  # Destination
        """Returns a destination object with the given id"""
        destination = self.data_wrapper.get_destination(id)
        return destination

    def update_destination(self, destination) -> None:
        """Updates a destination object with the given id"""
        error_check = self.validate_destination(destination)
        if error_check is "":
            return self.data_wrapper.update_destination(destination)
        else:
            raise ValueError(error_check)

    def delete_destination(self, id) -> None:
        """Deletes a destination object with the given id"""
        return self.data_wrapper.delete_destination(id)

    def validate_destination(self, destination):
        """Validates"""
        list_of_outcomes = []
        list_of_outcomes.append(self.validate.country_and_airport(destination))
        list_of_outcomes.append(self.validate.distance_km(destination.distance_km))
        list_of_outcomes.append(self.validate.flight_time(destination.flight_time))
        list_of_outcomes.append(
            self.validate.phone_number(destination.emergency_number)
        )
        error_message = ""

        for x in range(4):
            if list_of_outcomes[x] is False:
                error_message += VALIDATION_ERRORS[x]

        return error_message


# Verify:
#
# if country is allowed based on assignment description (DING!!)
#
# Flighttime?Distance?
#
# Emergency number
#
#
