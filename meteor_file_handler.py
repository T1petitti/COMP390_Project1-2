"""
This module assists with converting a string to an int or
float.+
Only the convert_string_to_numerical() function is available to outside files
"""


class MeteorFileHandler:
    def __init__(self):
        self.file_obj = None
        self.header = []

    def create_meteor_file_obj(self, file_name, file_mode):
        self.file_obj = open(file_name, file_mode)


    def convert_file_lines_to_lists(self):
        lines_list = []
        self.file_obj.readline()
        for line in self.file_obj:
            line = line.strip('\n').split('\t')
            lines_list.append(line)
        return lines_list

    def strip_header(self):
        self.header = self.file_obj.readline().strip('\n').split('\t')
        return self.header

