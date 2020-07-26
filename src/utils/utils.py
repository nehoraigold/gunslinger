import csv
import json
from os import path


def LoadCSV(file_path: str):
    if not path.isfile(file_path):
        raise FileNotFoundError("Could not load CSV file {}".format(file_path))
    with open(file_path) as csv_file:
        read_csv = csv.reader(csv_file, delimiter=',')
        for row in read_csv:
            yield row


def LoadJSON(file_path: str):
    if not path.isfile(file_path):
        raise FileNotFoundError("Could not load JSON file {}".format(file_path))
    return json.load(open(file_path))


def FormatToHeader(title: str) -> str:
    if title is None or len(title) == 0:
        return ""

    BUFFER_SIZE = 2
    HORIZONTAL_BORDER = "-"
    VERTICAL_BORDER = "|"
    CORNER_BORDER = "+"

    horizontal_bar = CORNER_BORDER + (HORIZONTAL_BORDER * (2 * BUFFER_SIZE + len(title))) + CORNER_BORDER
    middle_bar = VERTICAL_BORDER + (" " * BUFFER_SIZE) + title + (" " * BUFFER_SIZE) + VERTICAL_BORDER
    return "{}\n{}\n{}".format(horizontal_bar, middle_bar, horizontal_bar)
