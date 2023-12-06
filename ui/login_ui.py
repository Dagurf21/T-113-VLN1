from ui.widget import UIWidget
from ui.mainmenu_ui import MainMenuUI
from model.employee import Employee
from logic.logic_wrapper import LogicWrapper

class LoginUI(UIWidget):
    def __init__(self):
        self.logic_wrapper = LogicWrapper()

    def show(self):
        while True:
            self._print_header()
            self._print_plane()

            command = input("> ").lower()

            match command:
                case "q": # Exit the application
                    break

                case "l": # Prompt credentials and open main menu
                    self.login()
                
                case _: # For invalid input, reprompt
                    pass

    def login(self):
        self._print_header()
        while True:
            email = input("Input email: ")
            employee = self.logic_wrapper.get_employee_by_email(email)

            if employee != None:
                break

            self._print_header(message=f"No employee with email: {email}")
                
        self._print_header(message=f"Log in as {employee.email}")

        passwd_attempts_remaining = 3
        while True:
            passwd = input("Input password: ")

            if employee.password == passwd:
                break

            passwd_attempts_remaining -= 1
            if passwd_attempts_remaining == 0:
                return

            self._print_header(message=f"Invalid password ({passwd_attempts_remaining} attempts remaining)")

        main_menu = MainMenuUI(employee, self.logic_wrapper)
        main_menu.show()

    def _print_plane(self):
        print("""\
|            ______                                                 |
|            _\ _~-\___                                             |
|    =  = ==(_NaN AIR__D                                            |
|                \_____\___________________,-~~~~~~~`-.._           |
|                /     o O o o o o O O o o o o o o O o  |\_         |
|                `~-.__        ___..----..                  )       |
|                      `---~~\___________/------------`````         |
|                      =  ===(_________D                            |
|                                                                   |
-----------------------------  NaN Air  -----------------------------
|                                                                   |
|                       [L]og in  -  [Q]uit                         |
|                                                                   |
---------------------------------------------------------------------""")

