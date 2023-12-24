
""" This class represents an attribute filter for meteor data. It is designed to handle different filter modes
and provides a method to retrieve the filter label and index based on the selected mode."""

class AttributeFilter:
    def __init__(self, filter_mode):
        self.filter_mode = filter_mode
        self.filter_index = ""

    def get_filter_label(self):
        if self.filter_mode == "1":
            self.filter_index = 4
            return "MASS (g)"
        elif self.filter_mode == "2":
            self.filter_index = 6
            return "YEAR"
        else:
            return ""
