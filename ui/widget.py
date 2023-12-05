import os

UI_WIDTH = 69

class UICancelException(Exception):
    pass

class UIWidget:
    def _clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def _display_prompt(self, prompt: str, opt_instruction: str = None, clear_screen: bool = True, header_title: str = "", enable_cancel: bool = True):
        if clear_screen:
            self._print_header(message=header_title, add_extra_newline=True)

        if isinstance(opt_instruction, str):
            self._print_centered(opt_instruction, add_newline_after=True, add_newline_before=False)

        inp = input(f"{prompt}: ")
        if enable_cancel and inp == "":
            raise UICancelException
        
        return inp
    
    def _display_selection(self, options: [str], opt_instruction: str = None, header_title: str = "", include_back: bool = True) -> int:
        if include_back:
            options.append("Back")

        while True:
            self._print_header(message = header_title, add_extra_newline=True)
            self._print_options_list(options, numbered=True)
            option = self._display_prompt("Choose an option", opt_instruction=opt_instruction, clear_screen=False)

            try:
                option = int(option) - 1
                if option < 0 or option >= len(options):
                    self._clear_screen()
                    self._print_header(message="Invalid option", add_extra_newline=True)

                if include_back and option == len(options) - 1:
                    raise UICancelException

                return option
            except ValueError:
                self._clear_screen()
                self._print_header(message="Invalid option", add_extra_newline=True)

    def _print_options_list(self, lst: [str], numbered: bool = False):
        """Prints a list of options centered around the ui width. List can optionally be numbered"""
        largest_option = max(map(len, lst))
        padding_len = (UI_WIDTH - largest_option) // 2
        padding = " " * padding_len

        for i, option in enumerate(lst):
            if numbered:
                print(f"{padding}{i+1:>2} {option}")
            else:
                print(f"{padding}{option}")

    def _print_centered(self, text: str, add_newline_before: bool = False, add_newline_after: bool = False):
        if add_newline_before:
            print()
        print(text.center(UI_WIDTH))
        if add_newline_after:
            print()

    def _print_datalist(self, headers: {str: int}, data: [[str]]):
        """Prints a centered table of data with headers.
        Header format: { "label": col_size }
        Data format: [ row1, row2, row3 ]
        """

        # Print headers
        header_labels = [header.ljust(headers[header]) for header in headers]
        print(" | ".join(header_labels).center(UI_WIDTH))

        # Print rows
        header_sizes = [headers[header] for header in headers]
        for row in data:
            # Left pad with defined column size and make sure the data can't surpass that size
            data_row = []
            for i, elem in enumerate(row):
                column_size = header_sizes[i]
                elem = elem.ljust(column_size)

                if len(elem) > column_size:
                    elem = elem[:column_size - 1] + "."

                data_row.append(elem)

            print(" | ".join(data_row).center(UI_WIDTH))

    def _print_header(self, message = None, add_extra_newline: bool = False, clear_screen: bool = True):
        if clear_screen:
            self._clear_screen()
        print("""
---------------------------------------------------------------------
|                     NaN AIR Management system                     |
---------------------------------------------------------------------""")
        if isinstance(message, str):
            padding_len = (UI_WIDTH - len(message)) // 2
            padding = " " * padding_len
            print(f"{padding}{message}{padding}")

        if add_extra_newline:
            print()

