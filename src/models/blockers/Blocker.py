from src.models.blockers.abstract.IBlocker import IBlocker, Player


class Blocker(IBlocker):
    def __init__(self, name: str):
        self.name = name
        self.block_message = self.DEFAULT_BLOCK_MESSAGE

    def AllowsPassage(self, player: Player = None) -> bool:
        return False

    def SetBlockMessage(self, block_message: str) -> None:
        self.block_message = block_message

    def GetBlockMessage(self) -> str:
        return self.block_message

    def Interact(self, interaction: str, interaction_data: any = None) -> str:
        return None

    def __repr__(self):
        return self.name
