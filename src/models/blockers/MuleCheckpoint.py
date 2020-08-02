from src.models.blockers.abstract.IBlocker import IBlocker, Player


class MuleCheckpoint(IBlocker):
    def __init__(self):
        self.name = "mule checkpoint"
        self.block_message = "You cannot go inside with a mule!"

    def SetBlockMessage(self, block_message: str) -> None:
        self.block_message = block_message

    def GetBlockMessage(self) -> str:
        return self.block_message

    def Interact(self, interaction: str, context: any = None) -> str:
        return None

    def AllowsPassage(self, player: Player = None) -> bool:
        return not player.GetInventory().Has("mule")

    def __repr__(self):
        return self.name
