import typing
from src.Room import Room
from src.utils import utils


class World:
    def __init__(self, map_csv_file_path: str, room_descriptions_csv_file_path: str):
        self.board: typing.Dict[typing.Tuple[int, int], Room] = self.load_board_from_csv(map_csv_file_path)
        self.initialize_rooms(room_descriptions_csv_file_path)

    @staticmethod
    def load_board_from_csv(csv_file_path: str) -> typing.Dict[typing.Tuple[int, int], Room]:
        return {(i, j): Room(cell) for j, row in enumerate(utils.load_csv(csv_file_path)) for i, cell in enumerate(row)}

    def initialize_rooms(self, room_descriptions_csv_file_path: str):
        ROOM_NAME_INDEX = 0
        ROOM_DESCRIPTION_INDEX = 1
        for row in utils.load_csv(room_descriptions_csv_file_path):
            for room in self.board.values():
                if str(room) == row[ROOM_NAME_INDEX]:
                    room.SetDescription(row[ROOM_DESCRIPTION_INDEX])
                    break

    def GetRoom(self, coordinate: typing.Tuple[int, int]) -> Room:
        return self.board.get(coordinate, None)
