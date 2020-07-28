import typing
from abc import ABCMeta, abstractmethod
from src.room.Room import Room


class IWorld(metaclass=ABCMeta):
    @abstractmethod
    def GetRoom(self, coordinate: typing.Tuple[int, int]) -> typing.Union[None, Room]:
        raise NotImplementedError
