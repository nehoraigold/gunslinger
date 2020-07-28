import typing
from abc import ABCMeta, abstractmethod
from src.interactables.base.Interactable import Interactable


class IInteractableBuilder(metaclass=ABCMeta):
    @abstractmethod
    def BuildInteractable(self, interactable: Interactable) -> Interactable:
        raise NotImplementedError
