from src.actions.handlers.abstract.IActionHandler import IActionHandler, Action, IRoom
from src.utils import Print


class LookActionHandler(IActionHandler):
    def Handle(self, action: Action, room: IRoom) -> None:
        Print.Message(room.GetDescription())
