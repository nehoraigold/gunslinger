from abc import ABCMeta, abstractmethod
from src.interactables.blockers.Blocker import Blocker


class IBlockerBuilder(metaclass=ABCMeta):
    @abstractmethod
    def BuildBlocker(self, blocker: Blocker) -> Blocker:
        raise NotImplementedError
