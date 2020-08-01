import typing
from src.actions.handlers.abstract.IActionHandler import IActionHandler, Action, IRoom
from src.actions.data_types.transfer.TransferData import TransferData, TransferType
from src.utils import Print
from src.models.Player import Player, Inventory, Item


class TransferActionHandler(IActionHandler):
    def __init__(self, player: Player):
        self.player = player

    def Handle(self, action: Action, current_room: IRoom) -> None:
        transfer_type, item_name = self.unpack_transfer_data(action.GetData())
        src_inventory, dst_inventory = self.get_source_and_destination_inventories(transfer_type, current_room)
        item = src_inventory.Peek(item_name)

        if item is None:
            message = "There is no {} for you to {}.".format(item_name, str(transfer_type.value).lower())
        elif not item.IsTransferable():
            message = "You cannot {} the {}.".format(str(transfer_type.value).lower(), str(item))
        else:
            src_inventory.Remove(item)
            dst_inventory.Add(item)
            message = self.get_successful_transfer_message(transfer_type, item)

        Print.Message(message)

    def unpack_transfer_data(self, transfer_data: TransferData) -> typing.Tuple[TransferType, str]:
        return transfer_data.GetTransferType(), transfer_data.GetItemName()

    def get_successful_transfer_message(self, transfer_type: TransferType, item: Item) -> str:
        verb = "took" if transfer_type == TransferType.TAKE else "dropped"
        return "You {} the {}.".format(verb, str(item))

    def get_source_and_destination_inventories(self, transfer_type: TransferType, room: IRoom) -> typing.Tuple[Inventory, Inventory]:
        if transfer_type == TransferType.TAKE:
            src_inventory = room.GetInventory()
            dst_inventory = self.player.GetInventory()
        elif transfer_type == TransferType.DROP:
            src_inventory = self.player.GetInventory()
            dst_inventory = room.GetInventory()
        else:
            raise Exception("Unknown transfer type {}".format(transfer_type))
        return src_inventory, dst_inventory
