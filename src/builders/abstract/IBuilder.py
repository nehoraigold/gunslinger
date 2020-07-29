from abc import ABCMeta, abstractmethod


class IBuilder(metaclass=ABCMeta):
    @abstractmethod
    def Build(self, name: str) -> any:
        raise NotImplementedError
