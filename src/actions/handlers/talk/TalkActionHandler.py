from src.actions.Action import Action
from src.actions.handlers.abstract.IActionHandler import IActionHandler
from src.models.Player import Player
from src.models.npcs.Dialogue import Dialogue
from src.models.abstract.IRoom import IRoom
from src.utils import Print


class TalkActionHandler(IActionHandler):
    def __init__(self, player: Player):
        self.player = player

    def Handle(self, action: Action, current_room: IRoom) -> None:
        character_name = action.GetData()
        character = current_room.GetNonPlayableCharacter(character_name)
        if character is None:
            Print.Message("You cannot talk to {}.".format(self.get_properly_formatted_name(character_name)))
            return
        dialogue = Dialogue()
        while True:
            dialogue = character.TalkTo(self.player, dialogue)
            Print.Message(dialogue.GetNPCResponse())
            if dialogue.GetResponseOptions() is None:
                break
            Print.OrderedList(dialogue.GetResponseOptions())
            dialogue = self.player.TalkTo(character, dialogue)

    def get_properly_formatted_name(self, character_name: str) -> str:
        non_capitalized_words = ["the", "him", "her", "them"]
        words_to_add_article = ["man", "woman", "boy", "girl", "person", "human"]

        character_name = character_name.lower()
        if any(character_name.startswith(word) for word in non_capitalized_words):
            return character_name.lower()
        elif any(character_name.startswith(word) or character_name.endswith(word) for word in words_to_add_article):
            return "the {}".format(character_name)
        else:
            return character_name.capitalize()
