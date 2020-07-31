from abc import ABCMeta, abstractmethod
from src.actions.Action import Action
from src.models.environment.abstract.IRoom import IRoom


class IActionHandler(metaclass=ABCMeta):
    @abstractmethod
    def Handle(self, action: Action, current_room: IRoom) -> None:
        raise NotImplementedError
