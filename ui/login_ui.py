from ui.widget import UIWidget


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
        pass

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

