from abc import ABC, abstractmethod


class Parser(ABC):
    def __init__(self, src: str):
        self._src: str = src
        self._buffer = None

    @property
    @abstractmethod
    def content(self) -> str:
        pass
