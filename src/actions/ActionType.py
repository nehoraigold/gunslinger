import enum


class ActionType(enum.Enum):
    MOVE = "MOVE"
    LOOK = "LOOK"
    TAKE = "TAKE"
    DROP = "DROP"
    SPEAK = "SPEAK"
    UNLOCK = "UNLOCK"
    INTERACTION = "INTERACTION"
    INVENTORY = "INVENTORY"
    HELP = "HELP"
    QUIT = "QUIT"
