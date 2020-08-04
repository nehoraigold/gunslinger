import enum


class ActionType(enum.Enum):
    MOVE = "MOVE"
    LOOK = "LOOK"
    TRANSFER = "TRANSFER"
    TALK = "TALK"
    INTERACT = "INTERACT"
    INVENTORY = "INVENTORY"
    HELP = "HELP"
    QUIT = "QUIT"
