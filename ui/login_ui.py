from ui.widget import UIWidget
from ui.mainmenu_ui import MainMenuUI
from model.employee import Employee
from logic.logic_wrapper import LogicWrapper

class LoginUI(UIWidget):
    def __init__(self):
        self.logic_wrapper = LogicWrapper()

    def show(self):
        while True:
            self._clear_screen()
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
        self._clear_screen()
        self._print_header()
        email = input("Input email: ")
        # TODO: Validation
        passwd = input("Input password: ")
        # TODO: More validation

        # TODO: Log in as an actual employee
        user = Employee(
            name="Chuck Norris",
            email="chucknorris@nanair.is",
            ssn="123456789",
            password="lastdigitsofpi",
            address="everywhere",
            home_phone="12345678",
            mobile_phone="12345678",
        )

        main_menu = MainMenuUI(user, self.logic_wrapper)
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

