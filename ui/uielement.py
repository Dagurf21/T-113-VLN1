import os
from collections.abc import Callable
from colorama import Fore, Style, ansi
import cursor
import getch

UI_WIDTH = 97

class UICancelException(Exception):
    pass

class UIElement:
    def _clear_screen(self):
        """Clears the screen using the systems clear command"""
        os.system('cls' if os.name == 'nt' else 'clear')

    def _prompt(self, prompt: str, opt_instruction: str = None, clear_screen: bool = True, header_title: str = "", enable_cancel: bool = True, validator: Callable[[str], str] = lambda e: None):
        """
        Displays a prompt to input text into.

        Options:
            - clear_screen: Clears the screen and prints the header
            - opt_instruction: Displays an instruction right above the prompt
            - header_title: Title of the header used when clear_screen is enabled
            - enable_cancel: Throws a UICancelException when the input is blank
            - validator: Function to validate input. clear_screen must be enabled
                in  -> string input
                out <- None if valid, string error message if invalid
        """

        if clear_screen:
            self._print_header(
                message=header_title,
                add_extra_newline=True
            )

        while True:
            if isinstance(opt_instruction, str):
                self._print_centered(opt_instruction,
                    add_newline_after=True,
                    add_newline_before=False
                )

            inp = input(f"{Fore.RED}{prompt}: {Style.RESET_ALL}")

            if enable_cancel and inp == "":
                raise UICancelException

            if clear_screen:
                invalid = validator(inp)
                if invalid != None:
                    self._print_header(
                        message=header_title,
                        add_extra_newline=True
                    )
                    self._print_centered(invalid,
                        add_newline_after=True,
                        add_newline_before=False,
                        color=Fore.RED
                    )
                    continue

            break
        
        return inp

    def _prompt_list(self, prompt: str, header_title: str, enable_cancel: bool = True, element_display: Callable[[str], str] = lambda e: str(e), validator: Callable[[str], str] = lambda e: None, max_elements: int = 0):
        """
        Prompts the user for a list of elements

        Options:
            - enable_cancel: Allows the user to cancel by inputting 'q' which throws a UICancelException
            - element_display: Function to convert the user input into another string for element based formatting
                in  -> element
                out <- string representation
            - validator: Function to validate elements before they are added to the list
                in  -> element
                out <- None if valid or string with error message if invalid
        """

        elems = []
        self._print_header(message=header_title, add_extra_newline=True)
        while True:
            self._print_list([element_display(elem) for elem in elems], add_newline_after=True)
            try:
                elem = self._prompt(prompt, clear_screen=False, opt_instruction="Leave empty to finish (b: back)")
            except UICancelException:
                break

            if enable_cancel and elem == 'q':
                raise UICancelException

            if elem == 'b' and len(elems) > 0:
                elems.pop()
                self._print_header(message=header_title, add_extra_newline=True)
                continue

            invalid = validator(elem)
            if invalid != None:
                self._print_header(message=header_title, add_extra_newline=True)
                self._print_centered(invalid, add_newline_after=True, color=Fore.RED)
                continue

            elems.append(elem)
            if max_elements != 0:
                self._print_header(message=header_title, add_extra_newline=True)
            else:
                self._print_header(message=f"{header_title} ({max_elements - len(elems)})", add_extra_newline=True)
            
                if max_elements != 0 and len(elems) >= max_elements:
                    break

        return elems
    
    def _display_selection(self, options: [str], opt_instruction: str = None, header_title: str = "", include_back: bool = True, allow_cancel: bool = False, allow_back_shortcut: bool = True, back_title: str = "Back") -> str:
        """
        Displays an interactive menu to select one of the provided options.

        Options:
            - opt_instruction: Displays an instruction between the selection list and the input prompt
            - header_title: Specifies the title of the header used when clear_screen is enabled
            - include_back: Adds an option to return that throws a UICancelException when pressed
            - allow_cancel: Allow the user to leave the option empty and throw a UICancelException
            - allow_back_shortcut: Allows the user to press 'q' to go back
            - back_title: Specifies the name of the back option if include_back is true
        """

        if include_back:
            options.append(back_title)

        while True:
            self._print_header(
                message=header_title,
                add_extra_newline=True
            )
            self._print_list(options,
                numbered=True,
                add_newline_after=True
            )

            option = self._getkey()

            if include_back and allow_back_shortcut and option == 'q':
                raise UICancelException

            try:
                option = int(option) - 1
                option_count = len(options)
            except ValueError:
                self._clear_screen()
                self._print_header(message="Invalid option", add_extra_newline=True)
                continue

            # Display error for out of bounds input and reprompts
            if option < 0 or option >= option_count:
                self._clear_screen()
                self._print_header(
                    message="Invalid option",
                    add_extra_newline=True
                )
                continue

            # Back is always the last option so if back is enabled and the user selects it
            # then the exception is thrown
            if include_back and option == option_count - 1:
                raise UICancelException

            return options[option]

    def _display_interactive_datalist(self, headers: {str: int}, data: [[str]], title: str = "", rows_per_page: int = 10, return_msg: str = "return"):
        """
        Displays an interactive table of data where the data is divided into pages
        and the user can flip between the pages

        Options:
            - title: The title used for the header
            - rows_per_page: The amount of rows displayed per page
        """

        page_count = len(data) // rows_per_page
        current_page = 0

        while True:
            # Clamp current page between 0 and page_count
            current_page = min(max(current_page, 0), page_count)

            self._print_header(message=f"{title} [{current_page+1}/{page_count+1}]", add_extra_newline=True)
            self._print_datalist(headers, data[current_page * rows_per_page:current_page*rows_per_page+rows_per_page])
            self._print_centered(f"{Fore.BLACK}q: {return_msg} - n: next page - p: prev page{Style.RESET_ALL}", add_newline_after=True, add_newline_before=True)

            opt = self._getkey()

            match opt:
                case "q": # Return
                    break
                
                case "n": # Next page
                    current_page += 1

                case "p": # Prev page
                    current_page -= 1

                case _: # Unknown option
                    continue

    def _print_list(self, lst: [str], numbered: bool = False, add_newline_after: bool = False):
        """
        Prints a list of options centered around the ui width. List can optionally be numbered

        Options:
            - numbered: Adds the number of the element before each element
            - add_newline_after: Adds an additional newline after the option list
        """

        if len(lst) == 0:
            if add_newline_after:
                print()

            return

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

    def _print_centered(self, text: str, add_newline_before: bool = False, add_newline_after: bool = False, color: ansi.AnsiCodes = Style.RESET_ALL):
        """
        Prints the provided text centered horizontally in the ui
        
        Options:
            - add_newline_before: Adds an additional newline before the text
            - add_newline_after: Adds an additional newline after the text
            - color: Color of the text
        """

        if add_newline_before:
            print()

        print(f"{color}{text.center(UI_WIDTH)}{Style.RESET_ALL}")

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
        print(Fore.BLACK + " | ".join(header_labels).center(UI_WIDTH) + Style.RESET_ALL)

        # Print rows
        header_sizes = [headers[header] for header in headers]
        for row in data:
            # Left pad with defined column size and make sure the data can't surpass that size
            data_row = []
            for i, elem in enumerate(row):
                column_size = header_sizes[i]
                elem = str(elem).ljust(column_size)

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
+-----------------------------------------------------------------------------------------------+
|                                   NaN AIR Management system                                   |
+-----------------------------------------------------------------------------------------------+""")

        if isinstance(message, str):
            self._print_centered(message, color=Fore.LIGHTYELLOW_EX)

        if add_extra_newline:
            print()

    def _getkey(self) -> str:
        with cursor.HiddenCursor():
            c = getch.getch()

            if isinstance(c, bytes): # Windows
                if c == b'\x03':
                    raise KeyboardInterrupt

                if c == b'\x0d':
                    return ''

                try:
                    return c.decode('utf-8')
                except:
                    return None
            else: # *nix
                if ord(c) == 3:
                    raise KeyboardInterrupt

                if ord(c) == 13:
                    return ''
                
                return c

