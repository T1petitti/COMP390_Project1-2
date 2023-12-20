def label_meteor_data(meteordata_list):
    # data labels
    data_field_labels = ["Name", "id", "nametype", "recclass", "mass (g)", "fall", "year", "reclat", "reclong",
                         "GeoLocation",
                         "States", "Counties"]
    labelled_dict = {}
    for label in data_field_labels:
        # give each label in data_fields a meteorData value in the same index.
        labelled_dict[label] = meteordata_list[data_field_labels.index(label)]
    return labelled_dict
