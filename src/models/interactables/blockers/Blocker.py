from src.models.interactables.Interactable import Interactable


class Blocker(Interactable):
    DEFAULT_BLOCK_MESSAGE = "You can't go that way."

    def __init__(self, name: str, description: str = None, block_message: str = DEFAULT_BLOCK_MESSAGE):
        super().__init__(name, description)
        self.block_message = block_message

    def SetBlockMessage(self, block_message: str) -> None:
        self.block_message = block_message

    def GetBlockMessage(self) -> str:
        return self.block_message
