from abc import ABC, abstractmethod


class IPipeline(ABC):
    def __init__(self):
        pass

    @staticmethod
    @abstractmethod
    def declare_args(subparser):
        pass

    @abstractmethod
    def run(self, args) -> int:
        pass
