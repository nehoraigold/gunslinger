import typing
from src.environment.builders.IRoomBuilder import IRoomBuilder
from src.interactables.blockers.builders.IBlockerBuilder import IBlockerBuilder
from src.environment.Room import Room, MoveDirection, Blocker
from src.utils import utils


class CSVRoomBuilder(IRoomBuilder):
    NAME_INDEX = 0
    DESCRIPTION_INDEX = 1
    FIRST_TIME_EVENT_INDEX = 2
    BLOCKER_INDICES = {
        MoveDirection.UP: 3,
        MoveDirection.DOWN: 4,
        MoveDirection.LEFT: 5,
        MoveDirection.RIGHT: 6
    }

    def __init__(self, csv_file_path: str, blocker_builder: IBlockerBuilder):
        self.csv_file_path = csv_file_path
        self.blocker_builder = blocker_builder

    def BuildRoom(self, room: Room) -> Room:
        for row in utils.LoadCSV(self.csv_file_path):
            if str(room) == row[self.NAME_INDEX]:
                return self.get_room_from_row(room, row)

    def get_room_from_row(self, room: Room, row: typing.List[str]) -> Room:
        self.set_room_description(room, row)
        self.set_room_blockers(room, row)
        return room

    def set_room_description(self, room: Room, row: typing.List[str]) -> None:
        description = row[self.DESCRIPTION_INDEX].strip()
        if len(description) != 0:
            room.SetDescription(description)

    def set_room_blockers(self, room: Room, row: typing.List[str]) -> None:
        for direction, index in self.BLOCKER_INDICES.items():
            if len(row[index].strip()) != 0:
                blocker = self.blocker_builder.BuildBlocker(Blocker(row[index]))
                room.AddBlocker(direction, blocker)
