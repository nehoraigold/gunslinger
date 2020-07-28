from abc import ABCMeta, abstractmethod
from src.environment.Room import Room


class IRoomBuilder(metaclass=ABCMeta):
    @abstractmethod
    def BuildRoom(self, room: Room) -> Room:
        raise NotImplementedError
