from ui.widget import UIWidget
from ui.mainmenu_ui import MainMenuUI, Permissions
from model.employee import Employee

class LoginUI(UIWidget):
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

        # TODO: Get actual employee
        user = Employee(
            name="Chuck Norris",
            email="chucknorris@nanair.is",
            ssn="123456789",
            password_hash="lastdigitsofpi",
            address="everywhere",
            home_phone="12345678",
            mobile_phone="12345678",
        )

        main_menu = MainMenuUI(user, Permissions.Admin) # Temporary permission 0 -- Admin
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

