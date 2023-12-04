
UI_WIDTH = 69

class UIWidget:
    # TODO: Implement
    def _clear_screen(self):
        pass
    
    def _print_options_list(self, lst: [str], numbered: bool = False):
        largest_option = max(map(len, lst))
        padding_len = (UI_WIDTH - largest_option) // 2
        padding = " " * padding_len

        for i, option in enumerate(lst):
            if numbered:
                print(f"{padding}{i+1:>2} {option}{padding}")
            else:
                print(f"{padding}{option}{padding}")

    def _print_header(self, message = None):
        print("""
---------------------------------------------------------------------
|                     NaN AIR Management system                     |
---------------------------------------------------------------------""")
        if isinstance(message, str):
            padding_len = (UI_WIDTH - len(message)) // 2
            padding = " " * padding_len
            print(f"{padding}{message}{padding}")

