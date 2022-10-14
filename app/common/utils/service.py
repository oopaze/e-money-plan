from abc import ABC, abstractmethod


class Service(ABC):
    @abstractmethod
    def handle(self):
        raise NotImplementedError("'handle' should be implemented")
