from output_formatting_class import *
from input_formatting_class import *
from meteor_file_handler import MeteorFileHandler
from attribute_menu import AttributeFilter


class MainProgram:
    """
        Main program for filtering meteor data based on user inputs.

        Attributes:
        - file_name (str): The name of the meteor data file.
        - file_mode (str): The file mode for reading the meteor data file.
        - meteor_class_obj (MeteorFileHandler): The object representing the Meteor File.
        - attribute_obj (AttributeFilter): The object representing the chosen attribute for filtering.
        - lower_limit (str): The lower limit for the filtering range.
        - upper_limit (str): The upper limit for the filtering range.
        - filtered_data (list): List to store the filtered meteor data.
        - header (list): List to store the header information of the meteor data file.
        """
    def __init__(self):
        """ Initialize instance variables"""
        self.file_name = ""
        self.file_mode = ""
        self.meteor_class_obj = None
        self.attribute_obj = None
        self.lower_limit = ""
        self.upper_limit = ""
        self.filtered_data = []
        self.header = []

    def get_file_input_read_mode(self):
        """ Get the meteor data file name and file mode from user inputs. """
        self.file_name = check_file_name_input()
        self.file_mode = check_file_mode_input()

    def get_attribute_input(self):
        """ Get the attribute for filtering from user input. """
        filter_mode = check_attribute_input()
        self.attribute_obj = AttributeFilter(filter_mode)

    def get_filter_range(self):
        """ Get the lower and upper limits for the filtering range from user input. """
        print("")
        check_lower_limit_input(self, self.attribute_obj)
        check_upper_limit_input(self, self.attribute_obj)
        print("")

    def run_filter_process(self):
        """ Run the meteor data filtering process based on user inputs. """
        MeteorFileHandler.create_meteor_file_obj(self, self.file_name, self.file_mode)
        self.header = MeteorFileHandler.strip_header(self)
        formatted_lines = MeteorFileHandler.convert_file_lines_to_lists(self)
        for line in formatted_lines:
            desired_data = line[self.attribute_obj.filter_index]
            if desired_data and float(self.lower_limit) <= float(desired_data) <= float(self.upper_limit):
                self.filtered_data.append(line)

    def get_output_user_option(self):
        """ Get the user's choice for outputting the filtered meteor data. """
        output_results = check_output_results_input()
        if output_results == "1":
            write_header_to_terminal(self.header)
            write_data_to_terminal(self.filtered_data)
        if output_results == "2":
            write_data_to_text(self.header,self.filtered_data)
        if output_results == "3":
            write_filtered_results_to_excel_file(self.header, self.filtered_data)



