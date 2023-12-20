def meteordataentry(meteorData_list):
    # data labels
    data_field_labels = ["Name", "id", "nametype", "recclass", "mass (g)", "fall", "year", "reclat", "reclong", "GeoLocation",
                   "States", "Counties"]
    labelled_dict = {}
    for labels in data_field_labels:
        # give each label in data_fields a meteorData value in the same index.
        labelled_dict[labels] = meteorData_list[data_field_labels.index(labels)]
    return labelled_dict
