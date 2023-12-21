from MeteorFileHandler import *
from main_program_class import MainProgram
from input_formatting_class import *

def welcome_message():
    print("\n*** Welcome to the meteorite filtering program ***\n"
          "\nThis program is designed to open and read a meteor data file \n"
          "then extract the desired data in a clear readable table\n"
          "\n*** Developed by Tyler Petitti, October 2023 ***\n")


def extract_header(file_handler):
    file_handler.strip_header()
    return file_handler.strip_header


def get_filter_label():
    filter_options = { "1": "MASS (g)", "2": "YEAR" }
    user_input = get_user_input("What attribute would you like to filter the data on?\n"
                                "1. meteor MASS (g)\n"
                                "2. The YEAR the meteor fell to Earth\n"
                                "3. QUIT\n>> ", "3")
    return filter_options.get(user_input, "") #TODO refactor


def find_limit(data_filter, limit_type):
    limit = get_user_input(f"Enter the {limit_type} limit (inclusive) for the meteor's {data_filter} (\">Q\" to QUIT):"
                           f" ", ">Q")
    return limit


def convert_file_lines_to_lists(file_obj):
    lines_list = []
    file_obj.readline()
    for line in file_obj:
        line = line.strip('\n').split('\t')
        lines_list.append(line)
    file_obj.close()
    return lines_list


def extract_filtered_data_from_file(data_list, filter_mode, lower_limit, upper_limit):
    filtered_data = []
    desired_data_index = {"MASS (g)": 4, "YEAR": 6}.get(filter_mode)
    if desired_data_index is not None:
        for line in data_list:
            desired_data = line[desired_data_index]
            if desired_data and float(lower_limit) <= float(desired_data) <= float(upper_limit):
                filtered_data.append(line)
    return filtered_data


def create_table(test_list):
    # CREATE TABLE AND SHOWCASE BY NAME AND DESIRED DATA
    # ITERATE OVER LIST OF LABELLED LISTS THAT MATCH DATA REQUIREMENTS
    for line in test_list:
        new_formatted_line = f'{test_list.index(line) + 1:<8}'
        for label in line:
            old_formatted_line = new_formatted_line
            new_formatted_line = f'{old_formatted_line}{label:<25}'
        # EXTRACT AND PRINT THE NAME AND DESIRED DATA VALUE INTO TABLE
        print(f'{new_formatted_line}')


def print_header(header):
    new_formatted_line = f'{"":<8}'
    dashes = "========"
    for label in header:
        old_formatted_line = new_formatted_line
        new_formatted_line = f'{old_formatted_line}{label:<25}'
        dashes = dashes + "========================"
    print(new_formatted_line)
    print(dashes)


def main():
    welcome_message()
    main_program = MainProgram()
    main_program.get_file_input_read_mode()
    main_program.get_attribute_input()
    main_program.get_filter_range()
    main_program.run_filter_process() #TODO
    main_program.get_output_user_option() #TODO


if __name__ == '__main__':
    main()
