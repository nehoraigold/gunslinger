import typing
from src.interactables.base.builders.IInteractableBuilder import IInteractableBuilder, Interactable
from src.utils import utils


class CSVInteractableBuilder(IInteractableBuilder):
    INNER_CELL_DELIMITER = ";"
    NAME_INDEX = 0
    DESCRIPTION_INDEX = 1
    ALTERNATIVE_NAMES_INDEX = 2
    INTERACTIONS_INDEX = 3
    INTERACTION_DESCRIPTIONS_INDEX = 4

    def __init__(self, csv_file_path: str):
        self.csv_file_path = csv_file_path

    def BuildInteractable(self, interactable: Interactable) -> Interactable:
        for row in utils.LoadCSV(self.csv_file_path):
            if row[self.NAME_INDEX] == str(interactable):
                return self.get_interactable_from_row(interactable, row)

    def get_interactable_from_row(self, interactable: Interactable, row: typing.List[str]) -> Interactable:
        self.set_description(interactable, row)
        self.set_alternative_names(interactable, row)
        self.set_interactions(interactable, row)
        return interactable

    def set_description(self, interactable: Interactable, row: typing.List[str]) -> None:
        description = row[self.DESCRIPTION_INDEX].strip()
        if len(description) != 0:
            interactable.SetDescription(description)

    def set_alternative_names(self, interactable: Interactable, row: typing.List[str]) -> None:
        for alt_name in self.split_cell_contents(row[self.ALTERNATIVE_NAMES_INDEX]):
            alt_name = alt_name.strip().lower()
            if len(alt_name) != 0:
                interactable.AddAlternativeName(alt_name)

    def set_interactions(self, interactable: Interactable, row: typing.List[str]) -> None:
        interaction_desc_pairs = zip(self.split_cell_contents(row[self.INTERACTIONS_INDEX]),
                                     self.split_cell_contents(row[self.INTERACTION_DESCRIPTIONS_INDEX]))

        for interaction, interaction_desc in interaction_desc_pairs:
            interactable.AddInteraction(interaction.strip().lower(), interaction_desc.strip())

    def split_cell_contents(self, cell_contents: str) -> typing.List[str]:
        return cell_contents.split(self.INNER_CELL_DELIMITER)
