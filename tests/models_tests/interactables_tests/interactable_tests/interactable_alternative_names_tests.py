import unittest
from src.models.interactables.Interactable import Interactable


class InteractableAlternativeNamesTests(unittest.TestCase):
    def test_get_all_names_includes_name(self):
        name = "name"
        interactable = Interactable(name)
        self.assertIn(name, interactable.GetAllNames())

    def test_add_alternative_name_increases_all_names_list_length(self):
        name = "name 1"
        alternative_name = "name 2"
        interactable = Interactable(name)
        all_name_count = len(interactable.GetAllNames())

        interactable.AddAlternativeName(alternative_name)

        self.assertEqual(all_name_count + 1, len(interactable.GetAllNames()))

    def test_add_alternative_name_included_in_all_names_list(self):
        name = "name 1"
        alternative_name = "name 2"
        interactable = Interactable(name)
        self.assertNotIn(alternative_name, interactable.GetAllNames())

        interactable.AddAlternativeName(alternative_name)

        self.assertIn(alternative_name, interactable.GetAllNames())

    def test_add_alternative_name_does_not_add_same_name_twice(self):
        name = "name"
        interactable = Interactable(name)
        all_name_count = len(interactable.GetAllNames())

        interactable.AddAlternativeName(name)

        self.assertEqual(all_name_count, len(interactable.GetAllNames()))
