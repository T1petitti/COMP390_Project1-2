def meteordataentry(meteorData_list):
    Data_Fields = ["Name", "id", "nametype", "recclass", "mass (g)", "fall", "year", "reclat", "reclong", "GeoLocation",
                   "States", "Counties"]
    labelled_dict = {}
    for label in Data_Fields:
        labelled_dict[label] = meteorData_list[Data_Fields.index(label)]
    return labelled_dict
