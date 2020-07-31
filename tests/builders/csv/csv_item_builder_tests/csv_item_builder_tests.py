import unittest
import os
import typing
from src.builders.csv.CSVItemBuilder import CSVItemBuilder, Item
from tests.utils_tests.utils_tests.load_csv_tests import create_csv_file, delete_csv_file


class CSVItemBuilderTests(unittest.TestCase):
    DEFAULT_NAME = "old piano"
    DEFAULT_DESC = "It's an old wooden piano. It's seen better days."
    DEFAULT_ALT_NAMES = []
    DEFAULT_INTERACTIONS = []
    DEFAULT_INTERACTION_DESCRIPTIONS = []
    DEFAULT_IS_TAKEABLE = False
    DEFAULT_VALUE = 0

    @staticmethod
    def create_interactable_csv_row(name: str, desc: str, alt_names: typing.List[str],
                                    interactions: typing.List[str], interaction_desc: typing.List[str],
                                    is_takeable: bool, value: int) -> typing.List[str]:
        return [name, desc, '; '.join(alt_names), '; '.join(interactions), '; '.join(interaction_desc),
                "TRUE" if is_takeable else "FALSE", str("" if value == 0 else value)]

    @staticmethod
    def create_default_interactable_csv_row():
        return CSVItemBuilderTests.create_interactable_csv_row(CSVItemBuilderTests.DEFAULT_NAME,
                                                               CSVItemBuilderTests.DEFAULT_DESC,
                                                               CSVItemBuilderTests.DEFAULT_ALT_NAMES,
                                                               CSVItemBuilderTests.DEFAULT_INTERACTIONS,
                                                               CSVItemBuilderTests.DEFAULT_INTERACTION_DESCRIPTIONS,
                                                               CSVItemBuilderTests.DEFAULT_IS_TAKEABLE,
                                                               CSVItemBuilderTests.DEFAULT_VALUE)

    def create_interactables_csv_file(self, rows: typing.List[typing.List[str]]):
        header_row = ["name", "description", "alternative names", "interactions",
                      "interaction descriptions", "takeable", "value"]
        rows.insert(0, header_row)
        create_csv_file(self.file_path, rows)

    def setUp(self) -> None:
        self.DEFAULT_ALT_NAMES.clear()
        self.DEFAULT_INTERACTIONS.clear()
        self.DEFAULT_INTERACTION_DESCRIPTIONS.clear()
        self.file_path = str(os.path.join(os.getcwd(), "items.csv"))

    def tearDown(self) -> None:
        if os.path.isfile(self.file_path):
            delete_csv_file(self.file_path)

    def test_build_interactable_has_correct_name(self):
        self.create_interactables_csv_file([self.create_default_interactable_csv_row()])
        builder = CSVItemBuilder(self.file_path)

        item = builder.Build(self.DEFAULT_NAME)

        self.assertEqual(item.GetName(), self.DEFAULT_NAME)
        self.assertEqual(str(item), self.DEFAULT_NAME)

    def test_build_interactable_has_correct_description(self):
        self.create_interactables_csv_file([self.create_default_interactable_csv_row()])
        builder = CSVItemBuilder(self.file_path)

        item = builder.Build(self.DEFAULT_NAME)
        self.assertEqual(item.GetDescription(), self.DEFAULT_DESC)

    def test_build_interactable_has_correct_alternative_names_no_alternative_names(self):
        self.create_interactables_csv_file([self.create_default_interactable_csv_row()])
        builder = CSVItemBuilder(self.file_path)

        item = builder.Build(self.DEFAULT_NAME)

        self.assertEqual(len(item.GetAllNames()), 1)
        self.assertEqual(self.DEFAULT_NAME, item.GetAllNames()[0])

    def test_build_interactable_has_correct_alternative_names_one_alternative_name(self):
        alt_name = "piano"
        self.DEFAULT_ALT_NAMES.append(alt_name)
        self.create_interactables_csv_file([self.create_default_interactable_csv_row()])
        builder = CSVItemBuilder(self.file_path)

        item = builder.Build(self.DEFAULT_NAME)

        self.assertIn(alt_name, item.GetAllNames())

    def test_build_interactable_has_correct_alternative_names_multiple_alternative_names(self):
        alt_name_1 = "piano"
        alt_name_2 = "pianoforte"
        self.DEFAULT_ALT_NAMES.append(alt_name_1)
        self.DEFAULT_ALT_NAMES.append(alt_name_2)

        self.create_interactables_csv_file([self.create_default_interactable_csv_row()])
        builder = CSVItemBuilder(self.file_path)

        item = builder.Build(self.DEFAULT_NAME)

        self.assertIn(alt_name_1, item.GetAllNames())
        self.assertIn(alt_name_2, item.GetAllNames())

    def test_build_interactable_has_correct_interaction_zero_custom_interactions(self):
        self.create_interactables_csv_file([self.create_default_interactable_csv_row()])
        builder = CSVItemBuilder(self.file_path)

        item = builder.Build(self.DEFAULT_NAME)

        self.assertEqual(self.DEFAULT_DESC, item.Interact(Item.EXAMINE_INTERACTION))
        interaction = "play"
        self.assertIsNone(item.Interact(interaction))

    def test_build_interactable_has_correct_interaction_one_custom_interaction(self):
        interaction = "play"
        interaction_desc = "You pluck a few of the dusty keys."
        self.DEFAULT_INTERACTIONS.append(interaction)
        self.DEFAULT_INTERACTION_DESCRIPTIONS.append(interaction_desc)

        self.create_interactables_csv_file([self.create_default_interactable_csv_row()])
        builder = CSVItemBuilder(self.file_path)

        interactable = builder.Build(self.DEFAULT_NAME)

        self.assertEqual(interaction_desc, interactable.Interact(interaction))

    def test_build_interactable_has_correct_interaction_multiple_custom_interactions(self):
        interaction_1 = "play"
        interaction_desc_1 = "You pluck a few of the dusty keys."
        interaction_2 = "touch"
        interaction_desc_2 = "The piano feels rough and dusty."

        self.DEFAULT_INTERACTIONS.append(interaction_1)
        self.DEFAULT_INTERACTION_DESCRIPTIONS.append(interaction_desc_1)
        self.DEFAULT_INTERACTIONS.append(interaction_2)
        self.DEFAULT_INTERACTION_DESCRIPTIONS.append(interaction_desc_2)

        self.create_interactables_csv_file([self.create_default_interactable_csv_row()])
        builder = CSVItemBuilder(self.file_path)

        item = builder.Build(self.DEFAULT_NAME)

        self.assertEqual(interaction_desc_1, item.Interact(interaction_1))
        self.assertEqual(interaction_desc_2, item.Interact(interaction_2))
