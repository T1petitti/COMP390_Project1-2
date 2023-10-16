import meteor_data_class
import quit_params

# WELCOME MESSAGE
print("\n*** Welcome to the meteorite filtering program ***\n"
      "\nThis program is designed to open and read a meteor data file \n"
      "then extract the desired data in a clear readable table\n"
      "\n*** Developed by Tyler Petitti, October 2023 ***\n")

# FILE NAME INPUT
file_name = input("Enter a valid file name (ex. \"file_name.txt\") with its file extension (if applicable) |or| \n"
                  "Enter \">q\" or \">Q\" to quit: ")
# CHECK FOR QUIT
quit_params.check4quit(file_name)

# CONFIRMATION
print(f"\n"
      f"Target file: {file_name}"
      f"\n")

# FILE MODE INPUT
print("What mode would you like to open the file with?\n"
      "\"r\" - open for reading (default)\n"
      "\"w\" - open for writing. truncating the file first\n"
      "\"x\" - open for exclusive creation, failing if the file already exists\n"
      "\"a\" - open for writing, appending to the end of file if it exists\n"
      "\"b\" - binary mode\n"
      "\"t\" - text mode (default)\n"
      "\"+\" - open for updating (reading and writing) \n"
      "Enter \">q\" or \">Q\" to quit")
file_mode = input("Mode -> ")
# CHECK FOR QUIT
quit_params.check4quit(file_mode)

# CONFIRMATION
print(f"\n"
      f"File mode: {file_mode}"
      f"\n")

# OPEN FILE IN DESIRED MODE
file_obj = open(file_name, file_mode)
file_obj.readline()

# FILTER MODE INPUT
print("What attribute would you like to filter the data on?\n"
      "\"m\" - meteor MASS (g)\n"
      "\"y\" - the YEAR the meteor fell to Earth\n"
      "Enter \">q\" or \">Q\" to quit")
filter_mode = input(">> ")
# CHECK FOR QUIT
quit_params.check4quit(filter_mode)

# CREATE DATA FILTER LABEL
data_filter = ""
if filter_mode == "m":
    data_filter = "MASS (g)"
elif filter_mode == "y":
    data_filter = "YEAR"

# SPECIFY LOWER LIMIT AND UPPER LIMIT
# CHECK FOR QUIT x2
lower_limit = input(f"\nEnter the LOWER limit (inclusive) for the meteor's {data_filter} (\">q\" or \">Q\" to QUIT): ")
quit_params.check4quit(lower_limit)
upper_limit = input(f"Enter the UPPER limit (inclusive) for the meteor's {data_filter} (\">q\" or \">Q\" to QUIT): ")
quit_params.check4quit(upper_limit)

# CREATE LIST TO HOLD LINES THAT MATCH DATA REQUIREMENTS
data_holder = []

# ITERATE OVER FILE, LINE BY LINE AND EXTRACT LINES THAT MATCH DATA REQUIREMENTS
desired_data = ""
for line in file_obj:
    line = line.strip('\n').split('\t')
    # ONLY LOOK FOR DATA BASED ON FILTER
    if filter_mode == "m":
        desired_data = line[4]
    elif filter_mode == "y":
        desired_data = line[6]
    if desired_data == '':
        continue
    # IF DATA MATCHES UPPER AND LOWER LIMIT, LABEL EACH DATA VALUE IN LINE WITH FUNCTION AND ADD TO LIST
    if float(lower_limit) <= float(desired_data) <= float(upper_limit):
        labelled_line = meteor_data_class.meteordataentry(line)
        data_holder.append(labelled_line)

# CREATE TABLE AND SHOWCASE BY NAME AND DESIRED DATA
print(f'\n{"":<5}{"NAME":<24}{data_filter:<20}')
print("=======================================")
# ITERATE OVER LIST OF LABELLED LISTS THAT MATCH DATA REQUIREMENTS
for line in data_holder:
    print(
        # EXTRACT AND PRINT THE NAME AND DESIRED DATA VALUE INTO TABLE
        f'{data_holder.index(line) + 1:<5}{line.get("Name"):<24}{line.get(f"{data_filter.lower()}"):<20}')

file_obj.close()
