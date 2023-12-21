class AttributeFilter:
    def __init__(self, filter_mode):
        self.filter_mode = filter_mode

    def get_filter_label(self):
        if self.filter_mode == "1":
            return "MASS (g)"
        elif self.filter_mode == "2":
            return "YEAR"
        else:
            return ""
