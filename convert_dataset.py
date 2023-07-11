import csv
import json


# this method convert a csv dataset into a json one and return it
def csv_to_json(csv_file_path, json_file_path, data_key):
    json_array = []

    # read csv file
    with open(csv_file_path, encoding='utf-8') as csv_file:
        # load csv file data using csv library's dictionary reader
        csv_reader = csv.DictReader(csv_file, skipinitialspace=True)

        # convert each csv row into python dict
        for row in csv_reader:
            json_array.append(row)

        # insert the dict into a named dictionary
        json_dict = {data_key: json_array}

    # convert python jsonDict to JSON String and write to file
    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json_string = json.dumps(json_dict, indent=4)
        json_file.write(json_string)

    return json_dict
