import typing
import csv
import json
from os import path


def LoadCSV(file_path: str) -> typing.List[typing.List[str]]:
    if not path.isfile(file_path):
        raise FileNotFoundError("Could not load CSV file {}".format(file_path))
    with open(file_path) as csv_file:
        rows = list(csv.reader(csv_file, delimiter=','))
        max_row_length = max([len(row) for row in rows])
        for row in rows:
            yield row + ([""] * (max_row_length - len(row)))


def LoadJSON(file_path: str) -> json:
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


def AddCoordinates(*coordinates: typing.Tuple[int, int]) -> typing.Tuple[int, int]:
    return tuple([sum(x) for x in zip(*coordinates)])
