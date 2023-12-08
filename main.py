import colorama
from ui import LoginUI
from logic import LogicWrapper

colorama.init()

logic_wrapper = LogicWrapper()

try:
    ui = LoginUI(logic_wrapper)
    ui.show()
except KeyboardInterrupt:
    print()
    print("Stopping...")

