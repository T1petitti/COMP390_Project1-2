from input_formatting_class import *
from MeteorFileHandler import MeteorFileHandler
from attribute_menu import AttributeFilter

"""
This module assists with converting a string to an int or
float.+
Only the convert_string_to_numerical() function is available to outside files
"""


class MainProgram:
    def __init__(self):
        # Initialize instance variables
        self.file_name = ""
        self.file_mode = ""
        self.file_obj = None
        self.attribute_obj = None
        self.lower_limit = ""
        self.upper_limit = ""

    def get_file_input_read_mode(self):
        # TODO check for right answers
        print_filename_prompt()
        self.file_name = get_user_input("Enter ""\">q\" or \">Q\" to quit: ", ">q")
        confirmation_input_message("Target file: ", self.file_name)
        # TODO check for right answers
        print_filemode_prompt()
        self.file_mode = get_user_input("Mode -> ", ">q")
        confirmation_input_message("File mode: ", self.file_name)
        self.file_obj = MeteorFileHandler(self.file_name, self.file_mode)

    def get_attribute_input(self):
        # TODO check for right answers
        print_attribute_prompt()
        filter_mode = get_user_input(">>", "3")
        self.attribute_obj = AttributeFilter(filter_mode)

    def get_filter_range(self):
        self.lower_limit = get_user_input(
            f"Enter the LOWER limit (inclusive) for the meteor's {self.attribute_obj.get_filter_label()} (\">Q\" to "
            f"QUIT): ", ">Q")
        self.upper_limit = get_user_input(
            f"Enter the UPPER limit (inclusive) for the meteor's {self.attribute_obj.get_filter_label()} (\">Q\" to "
            f"QUIT): ", ">Q")

    def run_filter_process(self):
        return

    def get_output_user_option(self):
        return
