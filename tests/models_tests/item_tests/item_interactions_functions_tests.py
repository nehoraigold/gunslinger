import unittest
from src.models.Item import Item


class ItemInteractionFunctionsTests(unittest.TestCase):
    def test_default_examine_interaction_should_return_description_after_set(self):
        item = Item("piano")

        description = "An old, worn-out piano."
        item.SetDescription(description)

        self.assertEqual(item.Interact(Item.EXAMINE_INTERACTION), description)

    def test_get_interaction_that_is_not_present_should_return_none(self):
        name = "piano"
        item = Item(name)
        interaction = "play"

        self.assertIsNone(item.Interact(interaction))

    def test_getting_added_interaction_returns_proper_description(self):
        item = Item("piano")

        interaction = "play"
        interaction_description = "You pluck an out-of-tune melody on the faded black and white keys."
        item.AddInteraction(interaction, interaction_description)

        self.assertEqual(item.Interact(interaction), interaction_description)

    def test_adding_same_interaction_twice_overrides_first_interaction_description(self):
        item = Item("piano")

        interaction = "play"
        old_description = "You pluck an out-of-tune melody on the faded black and white keys."
        item.AddInteraction(interaction, old_description)

        new_description = "The keys feel dusty against your fingers, and the strings are clearly out of tune."
        item.AddInteraction(interaction, new_description)

        self.assertEqual(item.Interact(interaction), new_description)
