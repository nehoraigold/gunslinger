import csv
import json
from os import path


def load_csv(file_path: str):
    if not path.isfile(file_path):
        raise FileNotFoundError("Could not load CSV file {}".format(file_path))
    with open(file_path) as csv_file:
        read_csv = csv.reader(csv_file, delimiter=',')
        for row in read_csv:
            yield row


def load_json(file_path: str):
    if not path.isfile(file_path):
        raise FileNotFoundError("Could not load JSON file {}".format(file_path))
    return json.load(open(file_path))
