import typing
from src.actions.handlers.abstract.IActionHandler import IActionHandler, Action, IRoom
from src.actions.data_types.transfer.TransferData import TransferData, TransferType
from src.interfaces.Transferor import Transferor
from src.models.Player import Player
from src.models.Item import Item
from src.utils import Print


class TransferActionHandler(IActionHandler):
    def __init__(self, player: Player):
        self.player = player

    def Handle(self, action: Action, current_room: IRoom) -> None:
        transfer_type, item_name = self.unpack_transfer_data(action.GetData())
        dropper, taker = self.get_dropper_and_taker(transfer_type, current_room)
        item = dropper.Has(item_name)

        if item is None:
            message = "There is no {} for you to {}.".format(item_name, str(transfer_type.value).lower())
        elif not item.IsTransferable():
            message = "You cannot {} the {}.".format(str(transfer_type.value).lower(), str(item))
        else:
            dropper.Drop(item)
            taker.Take(item)
            message = self.get_successful_transfer_message(transfer_type, item)

        Print.Message(message)

    def unpack_transfer_data(self, transfer_data: TransferData) -> typing.Tuple[TransferType, str]:
        return transfer_data.GetTransferType(), transfer_data.GetItemName()

    def get_successful_transfer_message(self, transfer_type: TransferType, item: Item) -> str:
        verb = "took" if transfer_type == TransferType.TAKE else "dropped"
        return "You {} the {}.".format(verb, str(item))

    def get_dropper_and_taker(self, transfer_type: TransferType, room: IRoom) -> typing.Tuple[Transferor, Transferor]:
        dropper = room if transfer_type == TransferType.TAKE else self.player
        taker = self.player if transfer_type == TransferType.TAKE else room
        return dropper, taker
