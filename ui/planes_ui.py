from ui.widget import UIWidget, UICancelException
from model.plane import Plane # Dont think we need this ??
from model.employee import Employee
from logic.logic_wrapper import LogicWrapper

class PlaneUI(UIWidget):
    def __init__(self, user: Employee, logic_wrapper: LogicWrapper):
        self.user = user
        self.logic_wrapper = logic_wrapper

    def show(self):
        self._clear_screen()
        self._print_header(add_extra_newline=True)

        while True:
            self._print_options_list([
                "List planes",
                "List plane",
                "Register plane", 
                "Remove plane", 
                "Back",
            ], numbered=True)

            option = input("Choose an option: ")

            match option:
                case "1": # List Planes
                    self.display_plane_list()
                    self._clear_screen()
                    self._print_header(add_extra_newline=True)
                    
                case "2": # List a plane
                    self._clear_screen()
                    self._print_header(message="List a singular plane")
                    self.list_plane()
                    self._clear_screen()
                    self._print_header(message="Completed Successfully") # Not sure, may change

                case "3": # Register plane
                    self._clear_screen()
                    self._print_header(message="Register a plane")
                    self.register_plane()
                    self._clear_screen()
                    self._print_header(message="Completed Successfully") # Not sure, may change

                case "4": # Remove plane
                    self._clear_screen()
                    self._print_header(message="Removing a plane")
                    self.remove_plane()
                    self._clear_screen()
                    self._print_header(message="Completed Successfully") # Not sure, may change

                case "5": # Back
                    break

                case _: # Unkown option, reprompt
                    self._clear_screen()
                    self._print_header(message="Unknown option", add_extra_newline=True)

    def display_plane_list(self):
        planes = self.logic_wrapper.list_all_planes()
        planes_data = []

        for plane in planes:
            planes_data.append([
                plane.id,
                plane.name, 
                plane.type,
                plane.manufacturer,
                plane.capacity,
                plane.flight
            ])

        self._prompt_interactive_datalist(
            { "ID": 3, "name": 12, "Type": 4, "Availability": 12, "Destination": 14, "Flight ID": 10},
            planes_data
        )
        # Should work, not sure about the spacing

    def display_plane(self):
        self._print_header("List plane", add_extra_newline=True)

        while True:
            try: 
                plane_id = self._display_prompt("Enter plane id", opt_instruction="Leave empty to cancel", clear_screen=False)
                plane_id = int(plane_id)

                plane = self.logic_wrapper.list_plane(plane_id)

                if plane == None:
                    self._print_header("List Plane", add_extra_newline=True)
                    self._print_centered(f"Plane with ID {plane_id} does not exist", add_newline_after=True)
                    continue
                
                self._print_header(f"List Plane [id: {plane_id}]", add_extra_newline=True)
                self._print_options_list([
                    f"ID:           {plane.id}",
                    f"Name:         {plane.name}",
                    f"Type:         {plane.ty}",
                    f"Manufacturer: {plane.manufacturer}",
                    f"Capacity:     {plane.flights}"
                ], add_newline_after=True)

            
            except ValueError:
                self._print_header("List Plane", add_extra_newline=True)
                self._print_centered("ID has to be a number", add_newline_after=True)
                continue
            except UICancelException:
                return

    def register_plane(self):
        print ("We are registering a single plane here")
        try:
            name          = self._display_prompt("Enter name",            header_title="Register Plane", opt_instruction="Leave empty to cancel")
            plane_type    = self._display_prompt("Enter type",            header_title="Register Plane", opt_instruction="Leave empty to cancel")
            manufacturer  = self._display_prompt("Enter manufacturer",            header_title="Register Plane", opt_instruction="Leave empty to cancel")
            capacity      = self._display_prompt("Enter capacity",            header_title="Register Plane", opt_instruction="Leave empty to cancel")
            #flights       = self._display_prompt("Enter ",            header_title="Register Plane", opt_instruction="Leave empty to cancel")
            # Not sure if we add flights now or later

            plane = Plane(
                name=name,
                ty=plane_type,
                manufacturer=manufacturer, 
                capacity=capacity
            )

            self.logic_wrapper.create_plane(plane)
        except UICancelException:
            return


    def remove_plane(self):
        print ("We are removing a plane here")
