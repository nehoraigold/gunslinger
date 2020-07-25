import typing
from src.actions.abstract.IActionDataFactory import IActionDataFactory
from src.actions.move.MoveDirection import MoveDirection


class MoveActionDataFactory(IActionDataFactory):
    MOVE_WORDS = ["move", "go", "walk"]
    UP_WORDS = ["u", "n", "north", "up"]
    DOWN_WORDS = ["d", "s", "south", "down"]
    LEFT_WORDS = ["l", "w", "west", "left"]
    RIGHT_WORDS = ["r", "e", "east", "right"]

    @staticmethod
    def GetWords() -> typing.List[str]:
        return MoveActionDataFactory.MOVE_WORDS + \
               MoveActionDataFactory.UP_WORDS + \
               MoveActionDataFactory.DOWN_WORDS + \
               MoveActionDataFactory.LEFT_WORDS + \
               MoveActionDataFactory.RIGHT_WORDS

    @staticmethod
    def CreateData(string: str) -> MoveDirection:
        words = string.split(' ')
        if len(words) == 1:
            return MoveActionDataFactory.handle_one_word_string(words[0])
        if len(words) == 2:
            return MoveActionDataFactory.handle_two_word_string(words[0], words[1])
        raise Exception("Unable to parse move action {}".format(string))

    @staticmethod
    def handle_two_word_string(first_word: str, second_word: str) -> MoveDirection:
        if second_word in MoveActionDataFactory.UP_WORDS:
            return MoveDirection.UP
        elif second_word in MoveActionDataFactory.DOWN_WORDS:
            return MoveDirection.DOWN
        elif second_word in MoveActionDataFactory.LEFT_WORDS:
            return MoveDirection.LEFT
        elif second_word in MoveActionDataFactory.RIGHT_WORDS:
            return MoveDirection.RIGHT
        else:
            raise Exception("Unable to parse move action {} {}".format(first_word, second_word))

    @staticmethod
    def handle_one_word_string(word: str) -> MoveDirection:
        if word in MoveActionDataFactory.UP_WORDS:
            return MoveDirection.UP
        elif word in MoveActionDataFactory.DOWN_WORDS:
            return MoveDirection.DOWN
        elif word in MoveActionDataFactory.LEFT_WORDS:
            return MoveDirection.LEFT
        elif word in MoveActionDataFactory.RIGHT_WORDS:
            return MoveDirection.RIGHT
        else:
            raise Exception("Unable to parse move action {}".format(word))
