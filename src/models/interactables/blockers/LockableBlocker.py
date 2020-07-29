from src.models.interactables.blockers.Blocker import Blocker


class LockableBlocker(Blocker):
    def __init__(self, name: str):
        super().__init__(name)
        self.locked = True

    def IsLocked(self) -> bool:
        return self.locked

    def Lock(self) -> None:
        self.locked = True

    def Unlock(self) -> None:
        self.locked = False
