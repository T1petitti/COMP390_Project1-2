"""
Class for handling meteor data file operations.

Attributes:
- file_obj: File object representing the meteor data file.
- header (list): List to store the header information of the meteor data file.
"""

class MeteorFileHandler:
    """ Initialize instance variables"""
    def __init__(self):
        self.file_obj = None
        self.header = []

    def create_meteor_file_obj(self, file_name, file_mode):
        """ Create a file object for the meteor data file using file_name and file_mode """
        self.file_obj = open(file_name, file_mode)


    def convert_file_lines_to_lists(self):
        """ Convert lines from the meteor data file to lists. """
        lines_list = []
        self.file_obj.readline()
        for line in self.file_obj:
            line = line.strip('\n').split('\t')
            lines_list.append(line)
        return lines_list

    def strip_header(self):
        """ Strip and store the header information from the meteor data file. """
        self.header = self.file_obj.readline().strip('\n').split('\t')
        return self.header

