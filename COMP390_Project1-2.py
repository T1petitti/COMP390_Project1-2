
""" Main window for storing main program. Welcomes user then prompts for data with written functions. """

from main_functions_class import MainProgram


def welcome_message():
    """ Display a welcome message for the meteorite filtering program. """
    print("\n*** Welcome to the meteorite filtering program ***\n"
          "\nThis program is designed to open and read a meteor data file \n"
          "then extract the desired data in a clear readable table\n"
          "\n*** Developed by Tyler Petitti, October 2023 ***\n")


def main():
    """ The main entry point for the meteorite filtering program. This function orchestrates the entire
    filtering process, including getting file input, attribute input, filter range, running the filter process,
    and getting the user's output option. """

    welcome_message()
    main_program = MainProgram()
    main_program.get_file_input_read_mode()
    main_program.get_attribute_input()
    main_program.get_filter_range()
    main_program.run_filter_process()
    main_program.get_output_user_option()


if __name__ == '__main__':
    main()
