from src.actions.handlers.abstract.IActionHandler import IActionHandler, Action, Room
from src.utils import Print


class LookActionHandler(IActionHandler):
    def Handle(self, action: Action, room: Room) -> None:
        Print.Message(room.GetDescription())
