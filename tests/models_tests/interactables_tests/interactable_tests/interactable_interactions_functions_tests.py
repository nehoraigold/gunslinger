import unittest
from src.models.interactables.Interactable import Interactable


class InteractableInteractionFunctionsTests(unittest.TestCase):
    def test_default_examine_interaction_should_return_description(self):
        description = "An old, worn-out piano."
        interactable = Interactable("piano", description)

        self.assertEqual(interactable.Interact(Interactable.EXAMINE_INTERACTION), description)

    def test_default_examine_interaction_should_return_description_after_set(self):
        interactable = Interactable("piano")

        description = "An old, worn-out piano."
        interactable.SetDescription(description)

        self.assertEqual(interactable.Interact(Interactable.EXAMINE_INTERACTION), description)

    def test_get_interaction_that_is_not_present(self):
        name = "piano"
        interactable = Interactable(name, "An old, worn-out piano.")
        interaction = "play"
        expected_interaction = "You cannot {} the {}.".format(interaction, name)

        self.assertEqual(interactable.Interact(interaction), expected_interaction)

    def test_getting_added_interaction_returns_proper_description(self):
        interactable = Interactable("piano", "An old, worn-out piano.")

        interaction = "play"
        interaction_description = "You pluck an out-of-tune melody on the faded black and white keys."
        interactable.AddInteraction(interaction, interaction_description)

        self.assertEqual(interactable.Interact(interaction), interaction_description)

    def test_adding_same_interaction_twice_overrides_first_interaction_description(self):
        interactable = Interactable("piano", "An old, worn-out piano.")

        interaction = "play"
        old_description = "You pluck an out-of-tune melody on the faded black and white keys."
        interactable.AddInteraction(interaction, old_description)

        new_description = "The keys feel dusty against your fingers, and the strings are clearly out of tune."
        interactable.AddInteraction(interaction, new_description)

        self.assertEqual(interactable.Interact(interaction), new_description)
