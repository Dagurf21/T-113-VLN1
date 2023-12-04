
class UIWidget:
    # TODO: Implement
    def _clear_screen(self):
        pass

    def _print_header(self, message = None):
        print("""
---------------------------------------------------------------------
|                     NaN AIR Management system                     |
---------------------------------------------------------------------""")
        if isinstance(message, str):
            padding_len = (69 - len(message)) // 2
            padding = " " * padding_len
            print(f"{padding}{message}{padding}")

