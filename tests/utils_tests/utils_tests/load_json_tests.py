import unittest
import json
from os import path, remove
from src.utils import Utils


def create_json_file(file_path: str, json_data: dict):
    with open(file_path, "w") as json_file:
        json.dump(json_data, json_file)


def delete_json_file(file_path: str):
    remove(file_path)


class LoadJSONTests(unittest.TestCase):
    def test_load_empty_file_path(self):
        json_file_path = ""
        with self.assertRaises(FileNotFoundError):
            Utils.LoadJSON(json_file_path)

    def test_load_invalid_json_file(self):
        json_file_path = "invalid/path/to/file.json"
        with self.assertRaises(FileNotFoundError):
            Utils.LoadJSON(json_file_path)

    def test_load_valid_json(self):
        json_file_path = path.join(path.dirname(__file__), "file.json")
        json_data = {"A": 1, "B": "Hello", "C": {"X": "Y", "Z": [1, 2, 3]}}
        create_json_file(json_file_path, json_data)

        self.assertEqual(json_data, Utils.LoadJSON(json_file_path))

        delete_json_file(json_file_path)
