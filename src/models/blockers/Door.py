from src.models.blockers.abstract.IBlocker import IBlocker, Player


class Door(IBlocker):
    DEFAULT_BLOCK_MESSAGE = "The door is locked."
    DEFAULT_REQUIRED_ITEM_NAME = "small key"

    def __init__(self, name: str):
        self.name = name
        self.locked = True
        self.required_item_name = self.DEFAULT_REQUIRED_ITEM_NAME
        self.block_message = self.DEFAULT_BLOCK_MESSAGE

    def AllowsPassage(self, player: Player = None) -> bool:
        return not self.locked

    def SetBlockMessage(self, block_message: str) -> None:
        self.block_message = block_message

    def GetBlockMessage(self) -> str:
        return self.block_message

    def Interact(self, interaction: str, player: Player = None) -> str:
        message = None
        if interaction == "unlock" and player is not None:
            message = self.try_unlocking_door(player)
        return message

    def try_unlocking_door(self, player: Player) -> str:
        if not self.locked:
            return "The {} is already unlocked.".format(self.name)

        item = player.Has(self.required_item_name)
        if item is not None:
            self.locked = False
            player.Drop(item)
            return "You unlocked the {}.".format(self.name)

        return "You could not unlock the {}.".format(self.name)

    def __repr__(self):
        return self.name
