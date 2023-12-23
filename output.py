from meteor_file_handler import MeteorFileHandler
from main_functions_class import MainProgram

class Output:
def create_table():
    # CREATE TABLE AND SHOWCASE BY NAME AND DESIRED DATA
    # ITERATE OVER LIST OF LABELLED LISTS THAT MATCH DATA REQUIREMENTS
    main_obj = MainProgram()
    for line in main_obj.filtered_data:
        new_formatted_line = f'{main_obj.filtered_data.index(line) + 1:<8}'
        for label in line:
            old_formatted_line = new_formatted_line
            new_formatted_line = f'{old_formatted_line}{label:<25}'
        # EXTRACT AND PRINT THE NAME AND DESIRED DATA VALUE INTO TABLE
        print(f'{new_formatted_line}')

def print_header(self):
    header = MeteorFileHandler.strip_header(self)
    new_formatted_line = f'{"":<8}'
    dashes = "========"
    for label in header:
        old_formatted_line = new_formatted_line
        new_formatted_line = f'{old_formatted_line}{label:<25}'
        dashes = dashes + "========================"
    print(new_formatted_line,"\n", dashes)