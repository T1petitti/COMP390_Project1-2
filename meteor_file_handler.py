"""
This module assists with converting a string to an int or
float.+
Only the convert_string_to_numerical() function is available to outside files
"""


class MeteorFileHandler:
    def __init__(self, file_name, file_mode):
        self.file_name = file_name
        self.file_mode = file_mode
        self.file_obj = None
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

    def strip_header(self):
        if self.file_obj:
            self.header = self.file_obj.readline().strip('\n').split('\t')
            return self.header
