import unittest
import typing
import csv
from os import path, remove
from src.utils import Utils


def create_csv_file(file_path: str, data: typing.List[typing.List[str]]):
    with open(file_path, "w", newline='\n') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerows(data)


def delete_csv_file(file_path: str):
    remove(file_path)


class UtilsLoadCSVTests(unittest.TestCase):
    def test_load_empty_file_path(self):
        csv_file_path = ""
        with self.assertRaises(FileNotFoundError):
            for row in Utils.LoadCSV(csv_file_path):
                pass

    def test_load_nonexistent_file_path(self):
        csv_file_path = "path/that/does/not/exist.csv"
        with self.assertRaises(FileNotFoundError):
            for row in Utils.LoadCSV(csv_file_path):
                pass

    def test_load_valid_csv(self):
        csv_file_path = path.join(path.dirname(__file__), "valid_csv_file.csv")
        data = [["A", "B", "C", "D"], ["W", "X", "Y", "Z"]]
        create_csv_file(csv_file_path, data)

        for row_index, row in enumerate(Utils.LoadCSV(csv_file_path)):
            for cell_index, cell in enumerate(row):
                self.assertEqual(data[row_index][cell_index], cell)

        delete_csv_file(csv_file_path)
