import typing
from src.utils.Utils import FormatToHeader
from src.models.abstract.IRoom import IRoom


def Message(message: str, new_line: bool = True) -> str:
    if new_line:
        message += "\n"
    print(message)
    return message


def VisitTo(room: IRoom) -> str:
    message = "{}\n".format(FormatToHeader(str(room)))
    if not room.HasVisited() and room.GetDescription():
        message += "{}\n".format(room.GetDescription())
    print(message)
    return message


def NewLine() -> str:
    print()
    return "\n"


def GetInput(request: str) -> str:
    response = input("{} ".format(request))
    return response.strip().lower()


def UnorderedList(unordered_list: typing.List[str], number_of_indents: int = 1, bullet: str = "-") -> str:
    joiner = "{}{} ".format("\t" * number_of_indents, bullet)
    message = joiner
    message += "\n{}".format(joiner).join(unordered_list)
    message += "\n"
    print(message)
    return message
