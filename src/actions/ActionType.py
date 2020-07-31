import enum


class ActionType(enum.Enum):
    MOVE = "MOVE"
    LOOK = "LOOK"
    TAKE = "TAKE"
    DROP = "DROP"
    SPEAK = "SPEAK"
    UNLOCK = "UNLOCK"
    INTERACT = "INTERACT"
    INVENTORY = "INVENTORY"
    HELP = "HELP"
    QUIT = "QUIT"
