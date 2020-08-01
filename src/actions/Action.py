import typing
from src.actions.ActionType import ActionType
from src.actions.data_types.move.MoveDirection import MoveDirection
from src.actions.data_types.interaction.InteractionData import InteractionData


class Action:
    def __init__(self, action_type: ActionType, data: typing.Union[None, str, MoveDirection] = None):
        self.type = action_type
        self.data = data

    def GetType(self) -> ActionType:
        return self.type

    def GetData(self) -> typing.Union[None,
                                      str,
                                      MoveDirection,
                                      InteractionData,
                                      typing.List[str]]:
        return self.data
