import os

def input_formatting(self):
    self.lower_limit = ""
    self.upper_limit = ""

def check_file_name_input():
    while True:
        print_filename_prompt()
        file_name = input("Enter \">q\" or \">Q\" to quit: ")
        if os.path.exists(file_name):
            confirmation_input_message("Target file: ", file_name)
            break
        if file_name.lower() == '>q':
            print("\nThe program is now exiting... GOODBYE!")
            exit()
        else: print(f'ERROR: TARGET FILE NAME {file_name} IS NOT VALID!')
    return file_name

def check_file_mode_input():
    while True:
        print_filemode_prompt()
        file_mode = input("Mode -> ")
        if file_mode in ["r","w","x","a"]:
            confirmation_input_message("Target file: ", file_mode)
            break
        if file_mode.lower() == '>q':
            print("\nThe program is now exiting... GOODBYE!")
            exit()
        else: print(f'ERROR: TARGET FILE MODE {file_mode} IS NOT VALID!')
    return file_mode

def check_attribute_input():
    while True:
        print_attribute_prompt()
        filter_mode = input(">> ")
        if filter_mode in ["1","2"]:
            break
        if filter_mode == '3':
            print("\nThe program is now exiting... GOODBYE!")
            exit()
        else: print(f'ERROR: TARGET FILE MODE {filter_mode} IS NOT VALID!')
    return filter_mode

def check_lower_limit_input(self, attribute_obj):
    while True:
        self.lower_limit = input(f"Enter the LOWER limit (inclusive) for the meteor's "f""
                                       f"{attribute_obj.get_filter_label()} (\">Q\" to "f"QUIT): ")
        try:
            if float(self.lower_limit) >= 0: break
        except (ValueError, TypeError):
            if self.lower_limit == '>Q':
                print("\nThe program is now exiting... GOODBYE!")
                exit()
        print(f'ERROR: INVALID RANGE {self.lower_limit}')
    return self.lower_limit

def check_upper_limit_input(self, attribute_obj):
    while True:
        self.upper_limit = input(f"Enter the UPPER limit (inclusive) for the meteor's "
                                 f"{attribute_obj.get_filter_label()} (\">Q\" to "f"QUIT): ")
        try:
            if float(self.upper_limit) >= float(self.lower_limit): break
        except (ValueError, TypeError):
            if self.upper_limit == '>Q':
                print("\nThe program is now exiting... GOODBYE!")
                exit()
        print(f'ERROR: INVALID RANGE {self.upper_limit}')
    return self.upper_limit

def check_output_results_input():
    while True:
        print_output_results_prompt()
        output_results = input(f">> ")
        if output_results in ["1","2","3"]: break
        if output_results == "4":
                print("\nThe program is now exiting... GOODBYE!")
                exit()
    return output_results

def confirmation_input_message(message, user_input):
    # CONFIRMATION
    print(f"\n"
          f"{message}{user_input}"
          f"\n")


def print_filename_prompt():
    print("Enter a valid file name (ex. \"file_name.txt\") with its file extension (if applicable) |or|")


def print_filemode_prompt():
    # FILE MODE INPUT
    print("What mode would you like to open the file with?\n"
          "\"r\" - open for reading (default)\n"
          "\"w\" - open for writing. truncating the file first (WARNING: this mode will delete the contents of an "
          "existing file!)\n"
          "\"x\" - open for exclusive creation, failing if the file already exists\n"
          "\"a\" - open for writing, appending to the end of file if it exists\n"
          "Enter \">q\" or \">Q\" to quit ")


def print_attribute_prompt():
    print("What attribute would you like to filter the data on?\n"
          "1. Meteor MASS (g)\n"
          "2. The YEAR the meteor fell to Earth\n"
          "3. QUIT")

def print_output_results_prompt():
    print("How would you like to output the filter results?\n"
          "1. On screen (in terminal)\n"
          "2. To a TEXT file\n"
          "3. To an EXCEL file\n"
          "4. QUIT")

