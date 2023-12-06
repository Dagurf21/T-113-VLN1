from ui.login_ui import LoginUI
from logic.logic_wrapper import LogicWrapper

try:
    login_ui = LoginUI()
    login_ui.show()
except KeyboardInterrupt:
    print()
    print("Stopping...")

