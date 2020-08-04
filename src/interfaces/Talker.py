from abc import ABCMeta, abstractmethod
from src.models.npcs.Dialogue import Dialogue


class Talker(metaclass=ABCMeta):
    @abstractmethod
    def TalkTo(self, talker: "Talker", dialogue: Dialogue) -> Dialogue:
        raise NotImplementedError
