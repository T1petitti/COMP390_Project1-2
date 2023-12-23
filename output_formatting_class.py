from datetime import datetime
from xlwt import Workbook

def write_header_to_terminal(header):
    new_formatted_line = f'{"":<8}'
    dashes = "========"
    for label in header:
        old_formatted_line = new_formatted_line
        new_formatted_line = f'{old_formatted_line}{label:<25}'
        dashes = dashes + "========================"
    print(new_formatted_line,"\n", dashes)


def write_data_to_terminal(filtered_data):
    # CREATE TABLE AND SHOWCASE BY NAME AND DESIRED DATA
    # ITERATE OVER LIST OF LABELLED LISTS THAT MATCH DATA REQUIREMENTS
    for line in filtered_data:
        new_formatted_line = f'{filtered_data.index(line) + 1:<8}'
        for label in line:
            old_formatted_line = new_formatted_line
            new_formatted_line = f'{old_formatted_line}{label:<25}'
        # EXTRACT AND PRINT THE NAME AND DESIRED DATA VALUE INTO TABLE
        print(f'{new_formatted_line}')

def write_data_to_text(header, filtered_data):
    timestamp_str = get_clean_datetime_string()
    filename = f"{timestamp_str}.txt"
    with open(filename, 'w') as file:
        header = "\t".join(header) + "\n"
        file.write(header)
        for row in filtered_data[0:]:
            row_line = "\t".join(row) + "\n"
            file.write(row_line)
    print(f"Filtered data written to {filename}")


def write_filtered_results_to_excel_file(header, filtered_data):
    excel_workbook = Workbook()
    filtered_data_sheet = excel_workbook.add_sheet('filteredMeteoriteData')
    for name in header:
        filtered_data_sheet.write(0, header.index(name), name)
    for row_index in range(1, len(filtered_data) + 1):  # Start from the second row
        line = filtered_data[row_index - 1]  # Adjusted index to start from 0
        for col_index in range(len(line)):
            attribute_value = line[col_index]
            filtered_data_sheet.write(row_index, col_index, attribute_value)
    clean_timestamp_str = get_clean_datetime_string()
    excel_workbook.save(f'{clean_timestamp_str}.xls')
    print(f'\n\033[92mFiltered output sent to "{clean_timestamp_str}.xls"\033[0m')

def get_clean_datetime_string():
    current_timestamp = datetime.now()
    current_timestamp.strftime("%Y-%m-%d %H-%M-%S")
    clean_timestamp_str = current_timestamp.__str__().replace(':', '_')
    clean_timestamp_str = clean_timestamp_str.replace('.', '_')
    clean_timestamp_str = clean_timestamp_str.replace(' ', '_')
    return clean_timestamp_str