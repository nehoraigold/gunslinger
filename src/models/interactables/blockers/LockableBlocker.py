from src.models.interactables.blockers.Blocker import Blocker


class LockableBlocker(Blocker):
    def __init__(self, name: str,
                 description: str = None,
                 blocking_message: str = Blocker.DEFAULT_BLOCK_MESSAGE,
                 is_locked: bool = False):
        super().__init__(name, description, blocking_message)
        self.locked = is_locked

    def IsLocked(self) -> bool:
        return self.locked

    def Lock(self) -> None:
        self.locked = True

    def Unlock(self) -> None:
        self.locked = False
