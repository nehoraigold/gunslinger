import typing
from src.actions.ActionType import ActionType
from src.actions.data_types.move.MoveDirection import MoveDirection
from src.actions.data_types.transfer.TransferData import TransferData
from src.actions.data_types.interaction.InteractionData import InteractionData

ActionData = typing.Union[None, str, MoveDirection, TransferData, InteractionData, typing.List[str]]


class Action:
    def __init__(self, action_type: ActionType, data: ActionData = None):
        self.type = action_type
        self.data = data

    def GetType(self) -> ActionType:
        return self.type

    def GetData(self) -> ActionData:
        return self.data
