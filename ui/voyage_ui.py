from ui.widget import UIWidget, UICancelException
from model.voyage import Voyage
from model.employee import Employee
from logic.logic_wrapper import LogicWrapper

class VoyageUI(UIWidget):
    def __init__(self, user: Employee, logic_wrapper: LogicWrapper):
        self.user = user
        self.logic_wrapper = logic_wrapper
    
    def show(self):
        while True:
            try:
                option = self._display_selection(
                    [
                        "Create Voyage",
                        "List voyages - Finished not working bc. data layer", # !!! NOTICE !!!
                        "List voyage",
                        "Update voyage",
                        "Cancel voyage",
                        "Duplicate voyage", 
                    ],
                    header_title="Voyages"
                )
            except UICancelException:
                return

            match option:
                case 0: #Creating new voyage
                    self.create_voyage()
                    self._print_header(message="completed")
                case 1: # Listing all voyages
                    self.list_voyages()
                    self._print_header(message="Completed Successfully")
                
                case 2: # Listing a single voyage
                    self.list_voyage()
                    self._print_header(message="Completed Successfully")

                case 3: # Update Voyage
                    self.update_voyage()
                    self._print_header(message="Completed Successfully")

                case 4: # Cancel a voyage
                    self.cancel_voyage()
                    self._print_header(message="Completed Successfully")
                
                case 5: # Duplicating voyage
                    self.duplicate_voyage()
                    self._print_header(message="Completed Successfully")

    def create_voyage(self):
        try:
            plane              = self._prompt("Enter plane ID",                 header_title="Create voyage", opt_instruction="Leave empty to cancel")
            departure_flight   = self._prompt("Enter departing flight Number",  header_title="Create voyage", opt_instruction="Leave empty to cancel")
            arrival_flight     = self._prompt("Enter arrival flight Number",    header_title="Create voyage", opt_instruction="Leave empty to cancel")
            date               = self._prompt("Enter date of voyage",           header_title="Create voyage", opt_instruction="Leave empty to cancel")
            status             = self._prompt("Enter status of voyage",         header_title="Create voyage", opt_instruction="Leave empty to cancel")
            sold_seats         = self._prompt("Enter the amount of sold seats", header_title="Create voyage", opt_instruction="Leave empty to cancel")
            flight_attendants  = self._prompt("Enter flight_attendants ID",     header_title="Create voyage", opt_instruction="Leave empty to cancel (optional: n to skip)")
            pilots             = self._prompt("Enter lead pilot ID's",          header_title="Create voyage", opt_instruction="First ID is head pilot. Leave empty to cancel (optional: n to skip)", )        

            if flight_attendants.lower() == "n":
                flight_attendants = None
            
            if pilots.lower() == "n":
                pilots = None

            voyage = Voyage(
                plane=plane,
                departure_flight=departure_flight,
                arrival_flight=arrival_flight,
                date=date,
                status=status,
                sold_seats=sold_seats,
                flight_attendants=flight_attendants,
                pilots=pilots
            )

            self.logic_wrapper.create_voyage(voyage)

            return # TODO

        except UICancelException:
            return

    def list_voyages(self):
        voyages = self.logic_wrapper.list_all_voyages()
        voyage_data = []

        for voyage in voyages:
            voyage_data.append([
                voyage.id,
                voyage.sold_seats,
                voyage.departure_flight,
                voyage.arrival_flight,
                voyage.date
            ])
        
        self._display_interactive_datalist(
            { "id": 3, "From": 4, "DEST": 4, "Seats": 3, "Date": 8 },
            voyage_data,
            title="Voyages"
        )
    
    def list_voyage(self):
        self._print_header(
            message="List a voyage",
            add_extra_newline=True)
        
        while True:
            try:
                voyage_id = self._prompt(
                    "Enter voyage id", 
                    opt_instruction="Leave empty to cancel",
                    clear_screen=False
                )
            except UICancelException:
                return
            
            try: 
                voyage_id = int(voyage_id)
            except ValueError:
                self._print_header("List voyage", add_extra_newline=True)
                self._print_centered("ID has to be a number", add_newline_after=True)
                continue
        
            voyage = self.logic_wrapper.list_voyage(voyage_id)

            if voyage == None:
                self._print_header("List voyage", add_extra_newline=True)
                self._print_centered(f"Voyage with id {voyage_id} doesn't exist", add_newline_after=True)
                continue

            self._print_header(f"List Voyage [ID:{voyage_id}]", add_extra_newline=True)
            self._print_list([
                f"ID:     {voyage.id}",
                f"Plane:  {voyage.plane}",
                f"Pilot:  {voyage.pilot}",
                f"Seats:  {voyage.sold_seats}",
                f"From:   {voyage.departure_flight}",
                f"To:     {voyage.arrival_flight}",
                f"Date:   {voyage.date}",
            ], add_newline_after=True)

    def update_voyage(self):
        self._print_header(
            "Update Voyage",
            add_extra_newline=True
        )

        while True:
            try: 
                voyage_id = self._prompt(
                    "Enter Voygae ID",
                    opt_instruction="Leave empty to cancel",
                    clear_screen=False
                )
                voyage_id = int(voyage_id)
            except UICancelException:
                return
            except ValueError:
                self._print_header("List voyage", add_extra_newline=True)
                self._print_centered("ID has to be a number", add_newline_after=True)
                continue

            try:
                voyage = self.logic_wrapper.list_voyage(voyage_id)

                if voyage == None:
                    self._print_header("List Voyage", add_extra_newline=True)
                    self._print_centered(f"Voyage with ID {voyage_id} doesn't exist", add_newline_after=True)
                    continue

                voyage_fields = [
                    "Seats sold", 
                    "Plane", 
                    "Pilots", 
                    "Attendants",
                    "Departure Flight",
                    "Arrival Flight", 
                    "Date of flight", 
                    "Status of voyage"
                ]

                field_to_update = self._display_selection(
                    voyage_fields, 
                    header_title=f"Update voyage with ID [{voyage.id}]"
                )

                match field_to_update:
                    case 0: #Seats sold
                        voyage.sold_seats = self._prompt(
                            "Enter new amount of sold seats",
                            opt_instruction="Leave empty to cancel"
                        )
                    case 1: # Plane
                        voyage.plane = self._prompt(
                            "Enter new plane ID",
                            opt_instruction="Leave empty to cancel"
                        )
                    case 2: # Pilots
                        voyage.pilots = self._prompt(
                            "Enter ID's of pilots, first ID is head pilot, must enter at least 2",
                            opt_instruction="Leave empty to cancel - Format is {id}.{id}"
                        )
                    case 3: # Attendants
                        voyage.attendants = self._prompt(
                            "Enter ID's of attendants",
                            opt_instruction="Leave empty to cancel"
                        )
                    case 4: # Departure flight
                        voyage.departure_flight = self._prompt(
                            "Enter new flight number for departure flight",
                            opt_instruction="Leave empty to cancel"
                        )
                    case 5: # Arrival flight
                        voyage.arrival_flight = self._prompt(
                            "Enter new flight number for arrival flight",
                            opt_instruction="Leave empty to cancel"
                        )
                    case 6: # Date of flight
                        voyage.date = self._prompt(
                            "Enter new date for voyage",
                            opt_instruction="Leave empty to cancel"
                        )
                    case 7: # Status of voyage
                        voyage.status = self._prompt(
                            "Enter new status for voyage",
                            opt_instruction="Leave empty to cancel (Status options: Finished, Landed abroad, In the Air, Not started, Cancelled )"
                        )

                self.logic_wrapper.update_voyage(voyage)

                return
            except UICancelException:
                return
                
    def cancel_voyage(self):
        self._print_header(
            message="Cancel a voyage", 
            add_extra_newline=True
            )
        
    
    def duplicate_voyage(self):
        self._print_header(message="Duplicate Voyage")

