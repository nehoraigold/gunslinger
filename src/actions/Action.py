import typing
from src.actions.ActionType import ActionType
from src.actions.move.MoveDirection import MoveDirection


class Action:
    def __init__(self, action_type: ActionType, data: typing.Union[None, str, MoveDirection] = None):
        self.type = action_type
        self.data = data

    def GetType(self) -> ActionType:
        return self.type

    def GetData(self) -> typing.Union[None, str, MoveDirection]:
        return self.data
