from MeteorFilterClass import *


def welcome_message():
    print("\n*** Welcome to the meteorite filtering program ***\n"
          "\nThis program is designed to open and read a meteor data file \n"
          "then extract the desired data in a clear readable table\n"
          "\n*** Developed by Tyler Petitti, October 2023 ***\n")


def get_user_input(prompt, quit_command):
    user_input = input(prompt)
    if user_input == quit_command:
        print("\nThe program is now exiting... GOODBYE!")
        exit()
    return user_input


def confirm_input_message(message, user_input):
    # CONFIRMATION
    print(f"\n"
          f"{message}: {user_input}"
          f"\n")


def get_file_name():
    # FILE NAME INPUT
    file_name = get_user_input(
        "Enter a valid file name (ex. \"file_name.txt\") with its file extension (if applicable) |or| \n" "Enter "
        "\">q\" or \">Q\" to quit: ", ">q")
    confirm_input_message("Target file", file_name)
    return file_name


def get_file_mode():
    # FILE MODE INPUT
    print("What mode would you like to open the file with?\n"
          "\"r\" - open for reading (default)\n"
          "\"w\" - open for writing. truncating the file first (WARNING: this mode will delete the contents of an "
          "existing file!)\n"
          "\"x\" - open for exclusive creation, failing if the file already exists\n"
          "\"a\" - open for writing, appending to the end of file if it exists\n"
          "Enter \">q\" or \">Q\" to quit")
    file_mode = get_user_input("Mode -> ", ">q")
    confirm_input_message("File mode", file_mode)
    return file_mode


def create_file_object():
    file_handler = MeteorFileHandler(get_file_name(), get_file_mode())
    file_handler.open_file()
    return file_handler.file_obj


def extract_header(file_handler):
    file_handler.strip_header()
    return file_handler.strip_header


def get_filter_label():
    filter_options = {
        "1": "MASS (g)",
        "2": "YEAR",
        # Add more options as needed
    }
    user_input = get_user_input("What attribute would you like to filter the data on?\n"
                                "1. meteor MASS (g)\n"
                                "2. The YEAR the meteor fell to Earth\n"
                                "3. QUIT\n>> ", "QUIT")
    return filter_options.get(user_input, "")


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


def extract_data_from_file(data_list, filter_mode, lower_limit, upper_limit):
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
    name = get_file_name()
    mode = get_file_mode()
    file_handler = MeteorFileHandler(name, mode)
    file_handler.open_file()
    file_handler.strip_header()
    data_filter = get_filter_label()
    lower_limit = find_limit(data_filter, "LOWER")
    upper_limit = find_limit(data_filter, "UPPER")
    data_lists = convert_file_lines_to_lists(file_handler.file_obj)
    filtered_data = extract_data_from_file(data_lists, data_filter, lower_limit, upper_limit)
    print_header(file_handler.header)
    create_table(filtered_data)


if __name__ == '__main__':
    main()
