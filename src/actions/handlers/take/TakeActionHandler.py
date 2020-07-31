import typing
from src.actions.handlers.abstract.IActionHandler import IActionHandler, Action, IRoom
from src.Player import Player


class TakeActionHandler(IActionHandler):
    def __init__(self, player: Player):
        self.player = player

    def Handle(self, action: Action, current_room: IRoom) -> None:
        raise NotImplementedError("TakeActionHandler not yet implemented - received take {} action".format(action.GetData()))
