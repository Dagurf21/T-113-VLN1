import colorama
from ui.login_ui import LoginUI
from logic.logic_wrapper import LogicWrapper

colorama.init()

logic_wrapper = LogicWrapper()

try:
    ui = LoginUI(logic_wrapper)
    ui.show()
except KeyboardInterrupt:
    print()
    print("Stopping...")

