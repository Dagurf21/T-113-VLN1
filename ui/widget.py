import os

UI_WIDTH = 69

class UICancelException(Exception):
    pass

class UIWidget:
    def _clear_screen(self):
        """Clears the screen using the systems clear command"""
        os.system('cls' if os.name == 'nt' else 'clear')

    def _display_prompt(self, prompt: str, opt_instruction: str = None, clear_screen: bool = True, header_title: str = "", enable_cancel: bool = True):
        """
        Displays a prompt to input text into.

        Options:
            - clear_screen: Clears the screen and prints the header
            - opt_instruction: Displays an instruction right above the prompt
            - header_title: Title of the header used when clear_screen is enabled
            - enable_cancel: Throws a UICancelException when the input is blank
        """

        if clear_screen:
            self._print_header(
                message=header_title,
                add_extra_newline=True
            )

        if isinstance(opt_instruction, str):
            self._print_centered(opt_instruction,
                add_newline_after=True,
                add_newline_before=False
            )

        inp = input(f"{prompt}: ")

        if enable_cancel and inp == "":
            raise UICancelException
        
        return inp
    
    def _prompt_number(self, prompt: str, header_title: str, opt_instruction: str = None, enable_cancel: bool = True): 
        """
        Displays a prompt where the input has to be a number

        Options:
            - opt_instruction: Displays an instruction right above the prompt
            - enable_cancel: Throws a UICancelException when the input is blank
        """

        while True:
            inp = self._display_prompt(
                prompt,
                opt_instruction,
                header_title,
                enable_cancel
            )

            try:
                num = int(inp)
                return num
            except ValueError:
                self._print_header(
                    header_title,
                    add_extra_newline=True
                )
                self._print_centered(
                    "Input has to be a number",
                    add_newline_after=True
                )

    def _display_selection(self, options: [str], opt_instruction: str = None, header_title: str = "", include_back: bool = True) -> int:
        """
        Displays an interactive menu to select one of the provided options.

        Options:
            - opt_instruction: Displays an instruction between the selection list and the input prompt
            - header_title: Specifies the title of the header used when clear_screen is enabled
            - include_back: Adds an option to return that throws a UICancelException when pressed
        """

        if include_back:
            options.append("Back")

        while True:
            self._print_header(
                message=header_title,
                add_extra_newline=True
            )
            self._print_options_list(options,
                numbered=True,
                add_newline_after=True
            )

            option = self._display_prompt("Choose an option",
                opt_instruction=opt_instruction,
                clear_screen=False
            )

            try:
                option = int(option) - 1
                option_count = len(options)
            except ValueError:
                self._clear_screen()
                self._print_header(message="Invalid option", add_extra_newline=True)

            # Display error for out of bounds input and reprompts
            if option < 0 or option >= option_count:
                self._clear_screen()
                self._print_header(
                    message="Invalid option",
                    add_extra_newline=True
                )

            # Back is always the last option so if back is enabled and the user selects it
            # then the exception is thrown
            if include_back and option == option_count - 1:
                raise UICancelException

            return option


    def _prompt_interactive_datalist(self, headers: {str: int}, data: [[str]], title: str = ""):
        """
        Displays an interactive table of data where the data is divided into pages
        and the user can flip between the pages

        Options:
            - title: The title used for the header
        """

        while True:
            self._clear_screen()
            self._print_header(message=title, add_extra_newline=True)
            self._print_datalist(headers, data)
            self._print_centered("q: return - n: next page - p: prev page", add_newline_after=True, add_newline_before=True)

            # TODO: Page data

            opt = input("Choose an option: ")
            match opt:
                case "q": # Return
                    break
                
                case "n": # Next page
                    continue

                case "p": # Prev page
                    continue

                case _: # Unknown option
                    continue

    def _print_options_list(self, lst: [str], numbered: bool = False, add_newline_after: bool = False):
        """
        Prints a list of options centered around the ui width. List can optionally be numbered

        Options:
            - numbered: Adds the number of the element before each element
            - add_newline_after: Adds an additional newline after the option list
            - 
        """

        # Calculate the padding necessary to center the list
        largest_option = max(map(len, lst))
        padding_len = (UI_WIDTH - largest_option) // 2
        padding = " " * padding_len

        # Print each element
        for i, option in enumerate(lst):
            if numbered:
                print(f"{padding}{i+1:>2} {option}")
            else:
                print(f"{padding}{option}")

        if add_newline_after:
            print()

    def _print_centered(self, text: str, add_newline_before: bool = False, add_newline_after: bool = False):
        """
        Prints the provided text centered horizontally in the ui
        
        Options:
            - add_newline_before: Adds an additional newline before the text
            - add_newline_after: Adds an additional newline after the text
        """

        if add_newline_before:
            print()

        print(text.center(UI_WIDTH))

        if add_newline_after:
            print()

    def _print_datalist(self, headers: {str: int}, data: [[str]]):
        """
        Prints a centered table of data with headers.
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
        """
        Prints the NaN AIR application header

        Options:
            - message: Additional text underneath the header for labeling pages and status
            - add_extra_newline: Add an additional newline after the header and label
            - clear_screen: Clear the screen before printing the header
        """

        if clear_screen:
            self._clear_screen()

        print("""
---------------------------------------------------------------------
|                     NaN AIR Management system                     |
---------------------------------------------------------------------""")

        if isinstance(message, str):
            self._print_centered(message)

        if add_extra_newline:
            print()

