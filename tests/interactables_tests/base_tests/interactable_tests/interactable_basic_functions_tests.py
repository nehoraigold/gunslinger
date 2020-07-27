import unittest
from src.interactables.base.Interactable import Interactable


class InteractableBasicFunctionsTests(unittest.TestCase):
    def test_get_name_empty_string(self):
        empty_string = ""
        interactable = Interactable(empty_string)
        self.assertEqual(interactable.GetName(), empty_string)

    def test_get_name_normal_string(self):
        normal_string = "piano"
        interactable = Interactable(normal_string)
        self.assertEqual(interactable.GetName(), normal_string)

    def test_get_description_empty_string(self):
        empty_string = ""
        interactable = Interactable("piano", empty_string)
        self.assertEqual(interactable.GetDescription(), empty_string)

    def test_get_description_normal_string(self):
        normal_string = "An old, worn-out piano."
        interactable = Interactable("piano", normal_string)
        self.assertEqual(interactable.GetDescription(), normal_string)

    def test_set_description_empty_string(self):
        description = "An old, worn-out piano."
        interactable = Interactable("piano", description)

        empty_string = ""
        interactable.SetDescription(empty_string)

        self.assertEqual(interactable.GetDescription(), empty_string)

    def test_set_description_normal_string(self):
        interactable = Interactable("piano")

        description = "An old, worn-out piano."
        interactable.SetDescription(description)

        self.assertEqual(interactable.GetDescription(), description)

    def test_is_takeable_always_returns_false(self):
        interactable = Interactable("piano")
        self.assertFalse(interactable.IsTakeable())
