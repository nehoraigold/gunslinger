import unittest
from src.configs.ConfigsLoader import ConfigsLoader
from tests.utils_tests.load_json_tests import create_json_file, delete_json_file


class ConfigsLoaderGetTests(unittest.TestCase):
    def __init__(self, *args):
        super(ConfigsLoaderGetTests, self).__init__(*args)
        self.data = {
            "mapFilePath": "csv/map.csv",
            "roomFilePath": "csv/rooms.csv",
            "objectsFilePath": "csv/objects.csv"}
        self.json_file_name = "tests/configs_tests/configs.json"
        create_json_file(self.json_file_name, self.data)
        self.configs_loader = ConfigsLoader(self.json_file_name)
        delete_json_file(self.json_file_name)

    def test_empty_key(self):
        empty_key = ""
        with self.assertRaises(KeyError):
            self.configs_loader.Get(empty_key)

    def test_get_invalid_key(self):
        invalid_key = "invalidKey"
        with self.assertRaises(KeyError):
            self.configs_loader.Get(invalid_key)

    def test_get_valid_key(self):
        for key, value in self.data.items():
            self.assertEqual(self.configs_loader.Get(key), value)
