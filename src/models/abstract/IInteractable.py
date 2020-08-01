from abc import ABCMeta, abstractmethod


class IInteractable(metaclass=ABCMeta):
    @abstractmethod
    def Interact(self, interaction: str, context: any = None) -> str:
        raise NotImplementedError
