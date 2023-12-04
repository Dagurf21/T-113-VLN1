
UI_WIDTH = 69

class UIWidget:
    # TODO: Implement
    def _clear_screen(self):
        # TEMPORARY!!!!!
        for _ in range(50): print()
    
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

    def _print_header(self, message = None, add_extra_newline: bool = False):
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

