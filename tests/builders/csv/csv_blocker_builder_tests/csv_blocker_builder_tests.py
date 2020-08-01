import unittest
import typing
import os
from src.builders.csv.CSVBlockerBuilder import CSVBlockerBuilder
from src.models.blockers.Blocker import Blocker
from tests.utils_tests.utils_tests.load_csv_tests import create_csv_file, delete_csv_file


class CSVBlockerBuilderTests(unittest.TestCase):
    DEFAULT_NAME = "wall"
    DEFAULT_TYPE = ""
    DEFAULT_BLOCK_MESSAGE = ""

    @staticmethod
    def create_blocker_csv_row(name: str, blocker_type: str, block_message: str):
        return [name, blocker_type, block_message]

    def create_default_blocker_row(self):
        return CSVBlockerBuilderTests.create_blocker_csv_row(self.DEFAULT_NAME,
                                                             self.DEFAULT_TYPE,
                                                             self.DEFAULT_BLOCK_MESSAGE)

    def create_blockers_csv_file(self, rows: typing.List[typing.List[str]]):
        header_row = ["name", "blocker type", "block message"]
        rows.insert(0, header_row)
        create_csv_file(self.file_path, rows)

    def setUp(self) -> None:
        self.file_path = str(os.path.join(os.getcwd(), "blockers.csv"))

    def tearDown(self) -> None:
        CSVBlockerBuilderTests.DEFAULT_BLOCK_MESSAGE = ""
        if os.path.isfile(self.file_path):
            delete_csv_file(self.file_path)

    def test_build_blocker_sets_default_block_message(self):
        self.create_blockers_csv_file([self.create_default_blocker_row()])
        builder = CSVBlockerBuilder(self.file_path)
        blocker = builder.Build(self.DEFAULT_NAME)
        self.assertEqual(Blocker.DEFAULT_BLOCK_MESSAGE, blocker.GetBlockMessage())

    def test_build_blocker_sets_custom_block_message(self):
        self.DEFAULT_BLOCK_MESSAGE = "Default block message!"
        self.create_blockers_csv_file([self.create_default_blocker_row()])
        builder = CSVBlockerBuilder(self.file_path)
        blocker = builder.Build(self.DEFAULT_NAME)
        self.assertEqual(self.DEFAULT_BLOCK_MESSAGE, blocker.GetBlockMessage())
