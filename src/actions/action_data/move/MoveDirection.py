import enum


class MoveDirection(enum.Enum):
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)

    @staticmethod
    def GetOppositeDirection(direction: "MoveDirection") -> "MoveDirection":
        if direction == MoveDirection.UP:
            return MoveDirection.DOWN
        elif direction == MoveDirection.DOWN:
            return MoveDirection.UP
        elif direction == MoveDirection.LEFT:
            return MoveDirection.RIGHT
        elif direction == MoveDirection.RIGHT:
            return MoveDirection.LEFT
