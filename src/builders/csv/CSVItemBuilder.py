import typing
from src.builders.abstract.IBuilder import IBuilder
from src.models.interactables.Interactable import Interactable
from src.utils import Utils


class CSVInteractableBuilder(IBuilder):
    INNER_CELL_DELIMITER = ";"
    NAME_INDEX = 0

    def __init__(self, csv_file_path: str):
        self.csv_file_path = csv_file_path

    def Build(self, interactable_name: str) -> Interactable:
        for row in Utils.LoadCSV(self.csv_file_path):
            if interactable_name == row[self.NAME_INDEX]:
                return self.get_interactable_from_row(row)

    def get_interactable_from_row(self, row: typing.List[str]) -> Interactable:
        name, description, alt_names, interactions, interaction_descriptions = tuple(row)
        interactable = Interactable(name.strip())
        self.set_description(interactable, description)
        self.set_alternative_names(interactable, alt_names)
        self.set_interactions(interactable, interactions, interaction_descriptions)
        return interactable

    def set_description(self, interactable: Interactable, description: str) -> None:
        description = description.strip()
        if len(description) != 0:
            interactable.SetDescription(description)

    def set_alternative_names(self, interactable: Interactable, alternative_names: str) -> None:
        for alt_name in self.split_cell_contents(alternative_names):
            alt_name = alt_name.strip().lower()
            if len(alt_name) != 0:
                interactable.AddAlternativeName(alt_name)

    def set_interactions(self, interactable: Interactable, interactions: str, interaction_descriptions: str) -> None:
        interaction_desc_pairs = zip(self.split_cell_contents(interactions),
                                     self.split_cell_contents(interaction_descriptions))

        for interaction, interaction_desc in interaction_desc_pairs:
            interactable.AddInteraction(interaction.strip().lower(), interaction_desc.strip())

    def split_cell_contents(self, cell_contents: str) -> typing.List[str]:
        return cell_contents.split(self.INNER_CELL_DELIMITER)
