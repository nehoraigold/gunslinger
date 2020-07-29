import typing
from src.builders.csv.CSVInteractableBuilder import CSVInteractableBuilder
from src.models.interactables.blockers.Blocker import Blocker
from src.utils import utils


class CSVBlockerBuilder(CSVInteractableBuilder):
    def __init__(self, csv_file_path: str):
        super().__init__(csv_file_path)

    def Build(self, blocker_name: str) -> Blocker:
        for row in utils.LoadCSV(self.csv_file_path):
            if blocker_name == row[self.NAME_INDEX]:
                return self.get_blocker_from_row(row)

    def get_blocker_from_row(self, row: typing.List[str]) -> Blocker:
        name, description, alt_names, interactions, interaction_descriptions, block_message, \
        lockable, starts_locked, unlock_failed_description, unlock_success_description = tuple(row)
        blocker = Blocker(name.strip())
        self.set_description(blocker, description)
        self.set_alternative_names(blocker, alt_names)
        self.set_interactions(blocker, interactions, interaction_descriptions)
        self.set_block_message(blocker, block_message)
        return blocker

    def set_block_message(self, blocker: Blocker, block_message: str) -> None:
        block_message = block_message.strip()
        if len(block_message) != 0:
            blocker.SetBlockMessage(block_message)
