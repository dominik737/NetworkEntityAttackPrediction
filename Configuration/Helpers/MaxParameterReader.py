import csv
from Communication.Helpers import DetailParameterRetriever
from Exceptions.MissingConfigEntry import MissingConfigEntry
from Exceptions.DuplicitConfigEntry import DuplicitConfigEntry

csv_file_path = 'Configuration/MaxParameterValues.csv'
type_index = 0
sub_type_index = 1
info_key_index = 2
max_volume_index = 3
weight_index = 4


def get_csv_data():
    with open(csv_file_path, "r") as csvFile:
        return csvFile.readlines()


csv_data = get_csv_data()


def get_csv_reader():
    return csv.reader(csv_data, delimiter=";")


def get_info_key_and_max_volume(event_type: str, event_sub_type: str) -> (str, float):
    row = get_row(event_type, event_sub_type)
    info_key: str = row[info_key_index]
    return info_key, DetailParameterRetriever.retrieve(row[max_volume_index])


def get_row(event_type: str, event_sub_type: str):
    matching_rows = get_matching_rows(event_type, event_sub_type)
    if subtype_and_type_found(matching_rows, event_type, event_sub_type):
        return matching_rows[0]


def get_matching_rows(event_type: str, event_sub_type: str) -> list:
    return list(filter(lambda x: x[type_index] == event_type and x[sub_type_index] == event_sub_type, get_csv_reader()))


def subtype_and_type_found(matching_rows: list, event_type: str, event_sub_type: str) -> bool:
    if len(matching_rows) == 1:
        return True
    elif len(matching_rows) == 0:
        raise MissingConfigEntry("Not found type: " + event_type + " and subtype:" + event_sub_type + " in file " + csv_file_path)
    else:
        raise DuplicitConfigEntry("Duplicit type: " + event_type + " and subtype:" + event_sub_type + " in file " + csv_file_path)


def get_weight(event_type: str, event_sub_type: str) -> float:
    row = get_row(event_type, event_sub_type)
    return float(row[weight_index])
