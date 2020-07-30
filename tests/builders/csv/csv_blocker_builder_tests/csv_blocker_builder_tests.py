import unittest
import typing
import os
from src.builders.csv.CSVBlockerBuilder import CSVBlockerBuilder, Blocker
from tests.utils_tests.utils_tests.load_csv_tests import create_csv_file, delete_csv_file


class CSVBlockerBuilderTests(unittest.TestCase):
    DEFAULT_NAME = "door"
    DEFAULT_DESC = "It's an old wooden door with a metal keyhole."
    DEFAULT_ALT_NAMES = []
    DEFAULT_INTERACTIONS = []
    DEFAULT_INTERACTION_DESCRIPTIONS = []
    DEFAULT_BLOCK_MESSAGE = ""
    DEFAULT_LOCKABLE = True
    DEFAULT_STARTS_LOCKED = True
    DEFAULT_UNLOCK_FAILED = "You could not unlock the door."
    DEFAULT_UNLOCK_SUCCESSFUL = "You unlocked the door!"

    @staticmethod
    def create_blocker_csv_row(name: str, desc: str, alt_names: typing.List[str], interactions: typing.List[str],
                               interaction_desc: typing.List[str], block_message: str, lockable: bool,
                               starts_locked: bool, unlock_failed_description: str,	unlock_success_description: str):
        return [name, desc,
                '; '.join(alt_names),
                '; '.join(interactions),
                "; ".join(interaction_desc),
                block_message,
                "TRUE" if lockable else "FALSE",
                "TRUE" if starts_locked else "FALSE",
                unlock_failed_description,
                unlock_success_description]

    def create_default_blocker_row(self):
        return CSVBlockerBuilderTests.create_blocker_csv_row(self.DEFAULT_NAME,
                                                             self.DEFAULT_DESC,
                                                             self.DEFAULT_ALT_NAMES,
                                                             self.DEFAULT_INTERACTIONS,
                                                             self.DEFAULT_INTERACTION_DESCRIPTIONS,
                                                             self.DEFAULT_BLOCK_MESSAGE,
                                                             self.DEFAULT_LOCKABLE,
                                                             self.DEFAULT_STARTS_LOCKED,
                                                             self.DEFAULT_UNLOCK_FAILED,
                                                             self.DEFAULT_UNLOCK_SUCCESSFUL)

    def create_blockers_csv_file(self, rows: typing.List[typing.List[str]]):
        header_row = ["name", "description", "alternative names", "interactions", "interaction descriptions",
                      "block message", "lockable", "starts locked", "unlock failed", "unlock successful"]
        rows.insert(0, header_row)
        create_csv_file(self.file_path, rows)

    def setUp(self) -> None:
        self.file_path = str(os.path.join(os.getcwd(), "blockers.csv"))

    def tearDown(self) -> None:
        CSVBlockerBuilderTests.DEFAULT_ALT_NAMES.clear()
        CSVBlockerBuilderTests.DEFAULT_INTERACTIONS.clear()
        CSVBlockerBuilderTests.DEFAULT_INTERACTION_DESCRIPTIONS.clear()
        CSVBlockerBuilderTests.DEFAULT_BLOCK_MESSAGE = ""
        CSVBlockerBuilderTests.DEFAULT_LOCKABLE = True
        CSVBlockerBuilderTests.DEFAULT_STARTS_LOCKED = True
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
