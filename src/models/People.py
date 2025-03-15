from abc import ABC, abstractmethod
from typing import Dict, Any

class People(ABC):
    def __init__(self):
        self._name: str = ""
        self._age: int = 0

    @abstractmethod
    def to_dict(self) -> Dict[str, Any]:
        pass

    @abstractmethod
    def __repr__(self) -> str:
        pass
