import typing
from src.builders.abstract.IBuilder import IBuilder
from src.models.environment.Room import Room, MoveDirection
from src.utils import utils


class CSVRoomBuilder(IBuilder):
    NAME_INDEX = 0
    DESCRIPTION_INDEX = 1
    FIRST_TIME_EVENT_INDEX = 2
    BLOCKER_INDICES = {
        MoveDirection.UP: 3,
        MoveDirection.DOWN: 4,
        MoveDirection.LEFT: 5,
        MoveDirection.RIGHT: 6
    }

    def __init__(self, csv_file_path: str, blocker_builder: IBuilder):
        self.csv_file_path = csv_file_path
        self.blocker_builder = blocker_builder

    def Build(self, room_name: str) -> Room:
        for row in utils.LoadCSV(self.csv_file_path):
            if room_name == row[self.NAME_INDEX]:
                return self.get_room_from_row(row)

    def get_room_from_row(self, row: typing.List[str]) -> Room:
        room = Room(row[self.NAME_INDEX])
        self.set_room_description(room, row[self.DESCRIPTION_INDEX])
        self.set_room_blockers(room, row)
        return room

    def set_room_description(self, room: Room, description: str) -> None:
        description = description.strip()
        if len(description) != 0:
            room.SetDescription(description)

    def set_room_blockers(self, room: Room, row: typing.List[str]) -> None:
        for direction, index in self.BLOCKER_INDICES.items():
            if len(row[index].strip()) != 0:
                blocker = self.blocker_builder.Build(row[index])
                room.AddBlocker(direction, blocker)
