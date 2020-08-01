from src.actions.data_types.transfer.TransferType import TransferType


class TransferData:
    def __init__(self, transfer_type: TransferType, item_name: str):
        self.transfer_type = transfer_type
        self.item_name = item_name

    def GetTransferType(self) -> TransferType:
        return self.transfer_type

    def GetItemName(self) -> str:
        return self.item_name
