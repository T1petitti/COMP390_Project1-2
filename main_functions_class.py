from output_formatting_class import *
from input_formatting_class import *
from meteor_file_handler import MeteorFileHandler
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
        self.meteor_class_obj = None
        self.attribute_obj = None
        self.lower_limit = ""
        self.upper_limit = ""
        self.filtered_data = []
        self.header = []

    def get_file_input_read_mode(self):
        self.file_name = check_file_name_input()
        self.file_mode = check_file_mode_input()

    def get_attribute_input(self):
        filter_mode = check_attribute_input()
        self.attribute_obj = AttributeFilter(filter_mode)

    def get_filter_range(self):
        print("")
        check_lower_limit_input(self, self.attribute_obj)
        check_upper_limit_input(self, self.attribute_obj)
        print("")

    def run_filter_process(self):
        MeteorFileHandler.create_meteor_file_obj(self, self.file_name, self.file_mode)
        self.header = MeteorFileHandler.strip_header(self)
        formatted_lines = MeteorFileHandler.convert_file_lines_to_lists(self)
        for line in formatted_lines:
            desired_data = line[self.attribute_obj.filter_index]
            if desired_data and float(self.lower_limit) <= float(desired_data) <= float(self.upper_limit):
                self.filtered_data.append(line)

    def get_output_user_option(self):
        output_results = check_output_results_input()
        if output_results == "1":
            write_header_to_terminal(self.header)
            write_data_to_terminal(self.filtered_data)
        if output_results == "2":
            write_data_to_text(self.header,self.filtered_data)
        if output_results == "3":
            write_filtered_results_to_excel_file(self.header, self.filtered_data)



