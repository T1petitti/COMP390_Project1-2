"""
This module assists with converting a string to an int or
float.+
Only the convert_string_to_numerical() function is available to outside files
"""


class MeteorFileHandler:
    def __init__(self, file_name, file_mode):
        self.file_name = file_name
        self.file_mode = file_mode
        self.header = []

    def create_file_obj(self):
        self.file_obj = open(self.file_name, self.file_mode)

    def convert_file_lines_to_lists(self, file_obj):
        lines_list = []
        self.file_obj.readline()
        for line in self.file_obj:
            line = line.strip('\n').split('\t')
            lines_list.append(line)
        file_obj.close()
        return lines_list

    def extract_filtered_data_from_file(self, data_list, filter_mode, lower_limit, upper_limit):
        filtered_data = []
        desired_data_index = {"MASS (g)": 4, "YEAR": 6}.get(filter_mode)
        if desired_data_index is not None:
            for line in data_list:
                desired_data = line[desired_data_index]
                if desired_data and float(lower_limit) <= float(desired_data) <= float(upper_limit):
                    filtered_data.append(line)
        return filtered_data

    def strip_header(self):
        if self.file_obj:
            self.header = self.file_obj.readline().strip('\n').split('\t')
            return self.header
