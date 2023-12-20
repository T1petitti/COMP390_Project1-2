import meteor_data_class
import quit_params


def welcome_message():
    print("\n*** Welcome to the meteorite filtering program ***\n"
          "\nThis program is designed to open and read a meteor data file \n"
          "then extract the desired data in a clear readable table\n"
          "\n*** Developed by Tyler Petitti, October 2023 ***\n")


def get_file_name():
    # FILE NAME INPUT
    file_name = input("Enter a valid file name (ex. \"file_name.txt\") with its file extension (if applicable) |or| \n"
                      "Enter \">q\" or \">Q\" to quit: ")
    return file_name


def confirmation(file_name):
    # CONFIRMATION
    print(f"\n"
          f"Target file: {file_name}"
          f"\n")


def get_file_mode():
    # FILE MODE INPUT
    print("What mode would you like to open the file with?\n"
          "\"r\" - open for reading (default)\n"
          "\"w\" - open for writing. truncating the file first (WARNING: this mode will delete the contents of an "
          "existing file!)\n "
          "\"x\" - open for exclusive creation, failing if the file already exists\n"
          "\"a\" - open for writing, appending to the end of file if it exists\n"
          "Enter \">q\" or \">Q\" to quit")
    file_mode = input("Mode -> ")
    return file_mode


def confirmation2(file_mode):
    # CONFIRMATION
    print(f"\n"
          f"File mode: {file_mode}"
          f"\n")


def create_file(file_name, file_mode):
    # OPEN FILE IN DESIRED MODE
    file_obj = open(file_name, file_mode)
    return file_obj


def strip_header(file_obj):
    header = file_obj.readline()
    header = header.strip('\n').split('\t')
    return header


def get_filter_mode():
    # FILTER MODE INPUT
    print("What attribute would you like to filter the data on?\n"
          "1. meteor MASS (g)\n"
          "2. The YEAR the meteor fell to Earth\n"
          "3. QUIT")
    filter_mode = input(">> ")
    return filter_mode


def create_filter_label(filter_mode):
    # CREATE DATA FILTER LABEL
    data_filter = ""
    if filter_mode == "1":
        data_filter = "MASS (g)"
    elif filter_mode == "2":
        data_filter = "YEAR"
    return data_filter


def find_lower_limits(data_filter):
    lower_limit = input(f"\nEnter the LOWER limit (inclusive) for the meteor's {data_filter} (\">Q\" to QUIT): ")
    return lower_limit


def find_upper_limits(data_filter):
    upper_limit = input(f"Enter the UPPER limit (inclusive) for the meteor's {data_filter} (\">Q\" to QUIT): ")
    return upper_limit


def extract_data_from_file(file_obj, filter_mode, lower_limit, upper_limit):
    # ITERATE OVER FILE, LINE BY LINE AND EXTRACT LINES THAT MATCH DATA REQUIREMENTS
    desired_data = ''
    test_list = []
    file_obj.readline()
    for line in file_obj:
        line = line.strip('\n').split('\t')
        # ONLY LOOK FOR DATA BASED ON FILTER
        if filter_mode == "1":
            desired_data = line[4]
        elif filter_mode == "2":
            desired_data = line[6]
        if desired_data == '':
            continue
        # IF DATA MATCHES UPPER AND LOWER LIMIT, LABEL EACH DATA VALUE IN LINE WITH FUNCTION AND ADD TO LIST
        if float(lower_limit) <= float(desired_data) <= float(upper_limit):
            test_list.append(line)
    return test_list


def create_table(test_list):
    # CREATE TABLE AND SHOWCASE BY NAME AND DESIRED DATA
    # ITERATE OVER LIST OF LABELLED LISTS THAT MATCH DATA REQUIREMENTS
    for line in test_list:
        new_formatted_line = f'{test_list.index(line) + 1:<5}'
        for label in line:
            old_formatted_line = new_formatted_line
            new_formatted_line = f'{old_formatted_line}{label:<24}'
        # EXTRACT AND PRINT THE NAME AND DESIRED DATA VALUE INTO TABLE
        print(f'{new_formatted_line}')


def print_header(header):
    new_formatted_line = f'{"":<5}'
    dashes = "====="
    for label in header:
        old_formatted_line = new_formatted_line
        new_formatted_line = f'{old_formatted_line}{label:<24}'
        dashes = dashes + "======================="
    print(new_formatted_line)
    print(dashes)


def main():
    welcome_message()
    file_name = get_file_name()
    # TODO check for quit
    confirmation(file_name)
    file_mode = get_file_mode()
    # TODO check for quit
    confirmation2(file_mode)
    file_obj = create_file(file_name, file_mode)
    header = strip_header(file_obj)
    filter_mode = get_filter_mode()
    # TODO check for quit
    data_filter = create_filter_label(filter_mode)
    lower_limit = find_lower_limits(data_filter)
    # TODO check for quit
    upper_limit = find_upper_limits(data_filter)
    # TODO check for quit
    data_holder = extract_data_from_file(file_obj, filter_mode, lower_limit, upper_limit)
    print_header(header)
    create_table(data_holder)
    file_obj.close()


if __name__ == '__main__':
    main()
