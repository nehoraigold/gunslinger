from abc import ABCMeta, abstractmethod
from src.actions.Action import Action
from src.models.environment.World import Room


class IActionHandler(metaclass=ABCMeta):
    @abstractmethod
    def Handle(self, action: Action, current_room: Room) -> None:
        raise NotImplementedError
