from abc import ABCMeta, abstractmethod


class IFactory(metaclass=ABCMeta):
    @abstractmethod
    def Create(*args: any) -> any:
        raise NotImplementedError
