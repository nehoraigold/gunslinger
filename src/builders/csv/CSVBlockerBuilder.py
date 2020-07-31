import typing
from src.builders.abstract.IBuilder import IBuilder
from src.models.Blocker import Blocker
from src.utils import Utils


class CSVBlockerBuilder(IBuilder):
    NAME_INDEX = 0

    def __init__(self, csv_file_path: str):
        self.csv_file_path = csv_file_path

    def Build(self, blocker_name: str) -> Blocker:
        for row in Utils.LoadCSV(self.csv_file_path):
            if blocker_name == row[self.NAME_INDEX]:
                return self.get_blocker_from_row(row)

    def get_blocker_from_row(self, row: typing.List[str]) -> Blocker:
        name, block_message, *unlockable = tuple(row)
        blocker = Blocker(name.strip())
        self.set_block_message(blocker, block_message)
        return blocker

    def set_block_message(self, blocker: Blocker, block_message: str) -> None:
        block_message = block_message.strip()
        if len(block_message) != 0:
            blocker.SetBlockMessage(block_message)
