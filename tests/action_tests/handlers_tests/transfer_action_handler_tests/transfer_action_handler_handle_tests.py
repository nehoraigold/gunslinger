import unittest
import typing
from src.actions.Action import ActionType, Action, TransferData
from src.actions.handlers.transfer.TransferActionHandler import TransferActionHandler, Player, TransferType
from src.models.Room import Room, Item


class TransferActionHandlerHandleTests(unittest.TestCase):
    @staticmethod
    def create_transfer_action(transfer_type: TransferType, item_name: str) -> Action:
        return Action(ActionType.TRANSFER, TransferData(transfer_type, item_name))

    def setUp(self) -> None:
        self.player = Player()
        self.handler = TransferActionHandler(self.player)
        self.transferable = True

    def add_items_to_player(self, *items: Item) -> None:
        for item in items:
            item.SetTransferability(self.transferable)
            self.player.GetInventory().Add(item)

    def create_room_with(self, *items: Item) -> Room:
        room = Room("name")
        for item in items:
            item.SetTransferability(self.transferable)
            room.GetInventory().Add(item)
        return room

    def test_handle_take_action_sanity(self):
        # Arrange
        item = Item("key")
        room = self.create_room_with(item)

        # Act
        action = self.create_transfer_action(TransferType.TAKE, str(item))
        self.handler.Handle(action, room)

        # Assert
        self.assertIsNone(room.GetInventory().Peek(str(item)))
        self.assertEqual(self.player.GetInventory().Peek(str(item)), item)

    def test_handle_take_action_with_alternate_name(self):
        # Arrange
        item = Item("key")
        alt_name = "small key"
        item.AddAlternativeName(alt_name)
        room = self.create_room_with(item)

        # Act
        action = self.create_transfer_action(TransferType.TAKE, alt_name)
        self.handler.Handle(action, room)

        # Assert
        self.assertIsNone(room.GetInventory().Peek(str(item)))
        self.assertEqual(self.player.GetInventory().Peek(str(item)), item)

    def test_handle_take_action_item_not_in_room(self):
        # Arrange
        item = Item("key")
        room = Room("room name")

        # Act
        action = self.create_transfer_action(TransferType.TAKE, str(item))
        self.handler.Handle(action, room)

        # Assert
        self.assertIsNone(room.GetInventory().Peek(str(item)))
        self.assertIsNone(self.player.GetInventory().Peek(str(item)))

    def test_handle_take_action_item_not_transferable(self):
        # Arrange
        item = Item("key")
        self.transferable = False
        room = self.create_room_with(item)

        # Act
        action = self.create_transfer_action(TransferType.TAKE, str(item))
        self.handler.Handle(action, room)

        # Assert
        self.assertIsNone(self.player.GetInventory().Peek(str(item)))
        self.assertEqual(room.GetInventory().Peek(str(item)), item)

    def test_handle_drop_action_sanity(self):
        # Arrange
        item = Item("key")
        self.add_items_to_player(item)
        room = Room("name")

        # Act
        action = self.create_transfer_action(TransferType.DROP, str(item))
        self.handler.Handle(action, room)

        # Assert
        self.assertIsNone(self.player.GetInventory().Peek(str(item)))
        self.assertEqual(room.GetInventory().Peek(str(item)), item)

    def test_handle_drop_action_with_alternate_name(self):
        # Arrange
        item = Item("key")
        alt_name = "small key"
        item.AddAlternativeName(alt_name)
        self.add_items_to_player(item)
        room = Room("name")

        # Act
        action = self.create_transfer_action(TransferType.DROP, alt_name)
        self.handler.Handle(action, room)

        # Assert
        self.assertIsNone(self.player.GetInventory().Peek(str(item)))
        self.assertEqual(room.GetInventory().Peek(str(item)), item)

    def test_handle_drop_action_item_not_in_player_inventory(self):
        # Arrange
        item = Item("key")
        room = Room("room name")

        # Act
        action = self.create_transfer_action(TransferType.DROP, str(item))
        self.handler.Handle(action, room)

        # Assert
        self.assertIsNone(room.GetInventory().Peek(str(item)))
        self.assertIsNone(self.player.GetInventory().Peek(str(item)))

    def test_handle_drop_action_item_not_transferable(self):
        # Arrange
        item = Item("key")
        self.transferable = False
        self.add_items_to_player(item)
        room = Room("name")

        # Act
        action = self.create_transfer_action(TransferType.DROP, str(item))
        self.handler.Handle(action, room)

        # Assert
        self.assertIsNone(room.GetInventory().Peek(str(item)))
        self.assertEqual(self.player.GetInventory().Peek(str(item)), item)
