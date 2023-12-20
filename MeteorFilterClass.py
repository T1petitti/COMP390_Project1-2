class MeteorFileHandler:
    def __init__(self, file_name, file_mode):
        self.file_name = file_name
        self.file_mode = file_mode
        self.file_obj = None
        self.header = []

    def open_file(self):
        self.file_obj = open(self.file_name, self.file_mode)

    def strip_header(self):
        if self.file_obj:
            self.header = self.file_obj.readline().strip('\n').split('\t')
