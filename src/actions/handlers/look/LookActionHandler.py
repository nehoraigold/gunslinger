from src.actions.handlers.abstract.IActionHandler import IActionHandler, Action, Room


class LookActionHandler(IActionHandler):
    def Handle(self, action: Action, room: Room) -> None:
        print(room.Describe())
