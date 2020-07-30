from src.builders.abstract.IBuilder import IBuilder
from src.models.environment.World import World, IWorld
from src.utils import utils


class CSVWorldBuilder(IBuilder):
    def __init__(self, csv_file_path: str, room_builder: IBuilder):
        self.csv_file_path = csv_file_path
        self.room_builder = room_builder

    def Build(self, name: str = None) -> IWorld:
        return World({(i, j): self.room_builder.Build(cell.strip())
                      for j, row in enumerate(utils.LoadCSV(self.csv_file_path))
                      for i, cell in enumerate(row) if cell is not None})
