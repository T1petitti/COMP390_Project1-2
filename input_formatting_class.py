def get_user_input(prompt, quit_command):
    user_input = input(prompt)
    if user_input == quit_command:
        print("\nThe program is now exiting... GOODBYE!")
        exit()
    return user_input


def confirmation_input_message(message, user_input):
    # CONFIRMATION
    print(f"\n"
          f"{message}{user_input}"
          f"\n")


def print_filename_prompt():
    print("Enter a valid file name (ex. \"file_name.txt\") with its file extension (if applicable) |or|")


def print_filemode_prompt():
    # FILE MODE INPUT
    print("What mode would you like to open the file with?\n"
          "\"r\" - open for reading (default)\n"
          "\"w\" - open for writing. truncating the file first (WARNING: this mode will delete the contents of an "
          "existing file!)\n"
          "\"x\" - open for exclusive creation, failing if the file already exists\n"
          "\"a\" - open for writing, appending to the end of file if it exists\n"
          "Enter \">q\" or \">Q\" to quit ")


def print_attribute_prompt():
    print("What attribute would you like to filter the data on?\n"
          "1. Meteor MASS (g)\n"
          "2. The YEAR the meteor fell to Earth\n"
          "3. QUIT")
