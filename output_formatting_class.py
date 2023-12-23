def create_table(filtered_data):
    # CREATE TABLE AND SHOWCASE BY NAME AND DESIRED DATA
    # ITERATE OVER LIST OF LABELLED LISTS THAT MATCH DATA REQUIREMENTS
    for line in filtered_data:
        new_formatted_line = f'{filtered_data.index(line) + 1:<8}'
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
    print(new_formatted_line,"\n", dashes)