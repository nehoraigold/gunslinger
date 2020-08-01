import unittest
import typing
from src.actions.Action import ActionType, Action
from src.actions.handlers.take.TakeActionHandler import TakeActionHandler, Player
from src.models.Room import Room, Item


class TakeActionHandlerHandleTests(unittest.TestCase):
    def setUp(self) -> None:
        self.player = Player()
        self.handler = TakeActionHandler(self.player)

    def create_room_with(self, items: typing.List[Item], is_takeable: bool = True) -> Room:
        room = Room("name")
        for item in items:
            item.SetTakeability(is_takeable)
            room.AddItem(item)
        return room

    def test_take_action_with_invalid_item_name_results_in_no_inventory_change(self):
        room = self.create_room_with([Item("key")])

        different_item = "devil grass"

        action = Action(ActionType.TAKE, different_item)
        self.handler.Handle(action, room)

        self.assertIsNone(self.player.GetInventory().Peek(different_item))
        self.assertIsNone(room.ContainsItem(different_item))

    def test_take_action_with_no_item_in_room_results_in_no_inventory_change(self):
        item = "key"
        room = Room("room name")

        action = Action(ActionType.TAKE, item)
        self.handler.Handle(action, room)

        self.assertIsNone(self.player.GetInventory().Peek(item))
        self.assertIsNone(room.ContainsItem(item))

    def test_take_action_with_item_results_in_removing_item_from_room(self):
        item = Item("key")
        room = self.create_room_with([item])

        self.assertEqual(room.ContainsItem(str(item)), item)

        action = Action(ActionType.TAKE, str(item))
        self.handler.Handle(action, room)

        self.assertIsNone(room.ContainsItem(str(item)))

    def test_take_action_with_item_results_in_adding_item_to_player_inventory(self):
        item = Item("key")
        room = self.create_room_with([item])

        self.assertIsNone(self.player.GetInventory().Peek(str(item)))

        action = Action(ActionType.TAKE, str(item))
        self.handler.Handle(action, room)

        self.assertEqual(self.player.GetInventory().Peek(str(item)), item)

    def test_take_action_with_alternate_name_transfers_item_to_player(self):
        item = Item("key")
        alt_name = "small key"
        item.AddAlternativeName(alt_name)
        room = self.create_room_with([item])

        self.assertEqual(room.ContainsItem(alt_name), item)
        self.assertIsNone(self.player.GetInventory().Peek(alt_name))

        action = Action(ActionType.TAKE, alt_name)
        self.handler.Handle(action, room)

        self.assertIsNone(room.ContainsItem(alt_name))
        self.assertEqual(self.player.GetInventory().Peek(alt_name), item)

    def test_take_action_in_room_with_multiple_same_item_transfers_only_one_instance_to_player(self):
        item_1 = Item("key")
        item_2 = Item("key")
        room = self.create_room_with([item_1, item_2], True)

        action = Action(ActionType.TAKE, str(item_1))
        self.handler.Handle(action, room)

        item_in_room = room.ContainsItem(str(item_1))
        item_in_inventory = self.player.GetInventory().Peek(str(item_1))

        self.assertIsNotNone(item_in_room)
        self.assertIsNotNone(item_in_inventory)
        self.assertNotEqual(item_in_room, item_in_inventory)

    def test_take_action_on_untakeable_item_results_in_no_change_in_inventory(self):
        item = Item("key")
        room = self.create_room_with([item], False)

        self.assertEqual(room.ContainsItem(str(item)), item)
        self.assertIsNone(self.player.GetInventory().Peek(str(item)))

        action = Action(ActionType.TAKE, str(item))
        self.handler.Handle(action, room)

        self.assertEqual(room.ContainsItem(str(item)), item)
        self.assertIsNone(self.player.GetInventory().Peek(str(item)))

