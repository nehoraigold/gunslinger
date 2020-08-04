from src.models.abstract.IFactory import IFactory
from src.models.npcs.NonPlayableCharacter import NonPlayableCharacter, INonPlayableCharacter


class NPCFactory(IFactory):
    CHARACTERS = {

    }

    @staticmethod
    def Create(character_name: str) -> INonPlayableCharacter:
        character = NPCFactory.CHARACTERS.get(character_name.lower())
        if character is not None:
            return character
        else:
            capitalized_name = " ".join([word.capitalize() for word in character_name.split(" ")])
            return NonPlayableCharacter(capitalized_name)

