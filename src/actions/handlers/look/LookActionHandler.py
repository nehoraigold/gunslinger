from src.actions.handlers.abstract.IActionHandler import IActionHandler, Action, Room


class LookActionHandler(metaclass=IActionHandler):
    def Handle(self, action: Action, room: Room):
        print(room.Describe())
