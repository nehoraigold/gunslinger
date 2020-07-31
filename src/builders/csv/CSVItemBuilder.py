import typing
from src.builders.abstract.IBuilder import IBuilder
from src.models.Item import Item
from src.utils import Utils


class CSVItemBuilder(IBuilder):
    INNER_CELL_DELIMITER = ";"
    NAME_INDEX = 0

    def __init__(self, csv_file_path: str):
        self.csv_file_path = csv_file_path

    def Build(self, item_name: str) -> Item:
        for row in Utils.LoadCSV(self.csv_file_path):
            if item_name == row[self.NAME_INDEX]:
                return self.get_interactable_from_row(row)

    def get_interactable_from_row(self, row: typing.List[str]) -> Item:
        name, description, alt_names, interactions, interaction_descriptions, is_takeable, value = tuple(row)
        item = Item(name.strip())
        self.set_description(item, description)
        self.set_alternative_names(item, alt_names)
        self.set_interactions(item, interactions, interaction_descriptions)
        self.set_takeability(item, is_takeable)
        self.set_value(item, value)
        return item

    def set_description(self, item: Item, description: str) -> None:
        description = description.strip()
        if len(description) != 0:
            item.SetDescription(description)

    def set_alternative_names(self, item: Item, alternative_names: str) -> None:
        for alt_name in self.split_cell_contents(alternative_names):
            alt_name = alt_name.strip().lower()
            if len(alt_name) != 0:
                item.AddAlternativeName(alt_name)

    def set_interactions(self, item: Item, interactions: str, interaction_descriptions: str) -> None:
        interaction_desc_pairs = zip(self.split_cell_contents(interactions),
                                     self.split_cell_contents(interaction_descriptions))

        for interaction, interaction_desc in interaction_desc_pairs:
            item.AddInteraction(interaction.strip().lower(), interaction_desc.strip())

    def set_takeability(self, item: Item, is_takeable_str: str) -> None:
        item.SetTakeability(is_takeable_str.strip().lower() == "true")

    def set_value(self, item: Item, value_str: str) -> None:
        try:
            value = int(value_str)
        except ValueError:
            value = 0
        item.SetValue(value)

    def split_cell_contents(self, cell_contents: str) -> typing.List[str]:
        return cell_contents.split(self.INNER_CELL_DELIMITER)
