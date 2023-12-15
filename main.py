import colorama
from ui import LoginUI
from logic import LogicWrapper

colorama.init()

while True:
    try:
        logic_wrapper = LogicWrapper()
        ui = LoginUI(logic_wrapper)
        ui.show()
    except KeyboardInterrupt:
        print()
        print("Stopping...")
    except:
        print("A fatal error has orrurred. Press enter to restart")
        input()
        continue

    break
