import typing
from src.interactables.blockers.builders.IBlockerBuilder import IBlockerBuilder, Blocker
from src.interactables.base.builders.CSVInteractableBuilder import CSVInteractableBuilder
from src.utils import utils


class CSVBlockerBuilder(IBlockerBuilder):
    NAME_INDEX = 0
    BLOCK_MESSAGE_INDEX = 5
    LOCKABLE_INDEX = 6

    def __init__(self, csv_file_path: str):
        self.file_path = csv_file_path
        self.interactable_builder = CSVInteractableBuilder(csv_file_path)

    def BuildBlocker(self, blocker: Blocker) -> Blocker:
        for row in utils.LoadCSV(self.file_path):
            if blocker.GetName() == row[self.NAME_INDEX]:
                return self.get_blocker_from_row(blocker, row)

    def get_blocker_from_row(self, blocker: Blocker, row: typing.List[str]) -> Blocker:
        blocker = self.interactable_builder.BuildInteractable(blocker)
        self.set_block_message(blocker, row)
        return blocker

    def set_block_message(self, blocker: Blocker, row: typing.List[str]) -> None:
        block_message = row[self.BLOCK_MESSAGE_INDEX].strip()
        if len(block_message) != 0:
            blocker.SetBlockMessage(block_message)
