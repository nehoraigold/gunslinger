from src.utils.Utils import FormatToHeader
from src.models.environment.abstract.IRoom import IRoom


def Message(message: str) -> str:
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
