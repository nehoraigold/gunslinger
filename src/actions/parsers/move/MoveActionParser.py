import typing
from src.actions.parsers.abstract.IActionParser import IActionParser
from src.actions.data_types.move.MoveDirection import MoveDirection
from src.utils.ParseException import ParseException


class MoveActionParser(IActionParser):
    MOVE_WORDS = ["move", "go", "walk"]
    UP_WORDS = ["u", "n", "north", "up"]
    DOWN_WORDS = ["d", "s", "south", "down"]
    LEFT_WORDS = ["l", "w", "west", "left"]
    RIGHT_WORDS = ["r", "e", "east", "right"]

    @staticmethod
    def GetWords() -> typing.List[str]:
        return MoveActionParser.MOVE_WORDS + \
               MoveActionParser.UP_WORDS + \
               MoveActionParser.DOWN_WORDS + \
               MoveActionParser.LEFT_WORDS + \
               MoveActionParser.RIGHT_WORDS

    @staticmethod
    def ParseToData(string: str) -> MoveDirection:
        words = string.split(' ')
        if len(words) == 1:
            return MoveActionParser.handle_one_word_string(words[0])
        if len(words) == 2:
            return MoveActionParser.handle_two_word_string(words[0], words[1])
        raise ParseException("Unable to parse move action {}".format(string))

    @staticmethod
    def handle_two_word_string(first_word: str, second_word: str) -> MoveDirection:
        if second_word in MoveActionParser.UP_WORDS:
            return MoveDirection.UP
        elif second_word in MoveActionParser.DOWN_WORDS:
            return MoveDirection.DOWN
        elif second_word in MoveActionParser.LEFT_WORDS:
            return MoveDirection.LEFT
        elif second_word in MoveActionParser.RIGHT_WORDS:
            return MoveDirection.RIGHT
        else:
            raise ParseException("Unable to parse move action {} {}".format(first_word, second_word))

    @staticmethod
    def handle_one_word_string(word: str) -> MoveDirection:
        if word in MoveActionParser.UP_WORDS:
            return MoveDirection.UP
        elif word in MoveActionParser.DOWN_WORDS:
            return MoveDirection.DOWN
        elif word in MoveActionParser.LEFT_WORDS:
            return MoveDirection.LEFT
        elif word in MoveActionParser.RIGHT_WORDS:
            return MoveDirection.RIGHT
        else:
            raise ParseException("Unable to parse move action {}".format(word))
