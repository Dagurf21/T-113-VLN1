from logic.logic_wrapper import LogicWrapper
from ui.widget import UIWidget
from ui.mainmenu_ui import MainMenuUI
from colorama import Fore, Style

class LoginUI(UIWidget):
    def __init__(self, logic_wrapper: LogicWrapper):
        self.logic_wrapper = logic_wrapper

    def show(self):
        while True:
            self._print_header()
            self._print_plane()

            command = self._prompt("Enter command", clear_screen=False, enable_cancel=False)

            match command.lower():
                case "q": # Exit the application
                    break

                case "l": # Prompt credentials and open main menu
                    self.login()
                
                case _: # For invalid input, reprompt
                    pass

    def login(self):
        email = self._prompt("Input email", validator=self._validate_email, enable_cancel=False)
        employee = self.logic_wrapper.get_employee_by_email(email)
        password = self._prompt("Input email", header_title=f"Log in as {employee.email}", enable_cancel=False, validator=lambda e: self._validate_password(employee, e))

        main_menu = MainMenuUI(employee, self.logic_wrapper)
        main_menu.show()
    
    def _validate_email(self, email):
        # TODO: FOR DEBUG PURPOSES ONLY -- REMOVE IN PROD.
        if email == "":
            return None

        if not self.logic_wrapper.validate_email(email):
            return "Invalid email"
        
        if self.logic_wrapper.get_employee_by_email(email) == None:
            return f"No user with email '{email}' found"
        
        return None

    def _validate_password(self, user, password):
        if user.password == password:
            return None
        
        return "Invalid password"

    def _print_plane(self):
        print(f"""\
|             ______                                                  |
|             _\ _~-\___                                              |
|     =  = ==(_NaN AIR__D                                             |
|                 \_____\___________________,-~~~~~~~`-.._            |
|                 /     o O o o o o O O o o o o o o O o  |\_          |
|                 `~-.__        ___..----..                  )        |
|                       `---~~\___________/------------`````          |
|                       =  ===(_________D                             |
|                                                                     |
-------------------------------  NaN Air  -----------------------------
|                                                                     |
|                        [{Fore.GREEN}L{Style.RESET_ALL}]og in  -  [{Fore.RED}Q{Style.RESET_ALL}]uit                          |
|                                                                     |
-----------------------------------------------------------------------""")

