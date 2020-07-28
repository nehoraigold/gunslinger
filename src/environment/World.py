import typing
from src.environment.abstract.IWorld import IWorld, Room
from src.utils import utils


class World(IWorld):
    def __init__(self, map_csv_file_path: str = None, room_descriptions_csv_file_path: str = None):
        self.board = self.load_board_from_csv(map_csv_file_path) if map_csv_file_path is not None else {}
        self.initialize_rooms(room_descriptions_csv_file_path)

    @staticmethod
    def load_board_from_csv(csv_file_path: str) -> typing.Dict[typing.Tuple[int, int], Room]:
        return {(i, j): Room(cell) for j, row in enumerate(utils.LoadCSV(csv_file_path)) for i, cell in enumerate(row)}

    def initialize_rooms(self, room_descriptions_csv_file_path: str):
        if room_descriptions_csv_file_path is None:
            return
        ROOM_NAME_INDEX = 0
        ROOM_DESCRIPTION_INDEX = 1
        for row in utils.LoadCSV(room_descriptions_csv_file_path):
            for room in self.board.values():
                if str(room) == row[ROOM_NAME_INDEX]:
                    room.SetDescription(row[ROOM_DESCRIPTION_INDEX])
                    break

    def GetRoom(self, coordinate: typing.Tuple[int, int]) -> typing.Union[None, Room]:
        return self.board.get(coordinate, None)
