from src.models.People import People
from typing import Dict, Any

class Student(People):
    def __init__(self, name: str, age: int):
        super().__init__()
        self.__name = name
        self.__age = age
        
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(Nome: {self.__name}, Idade: {self.__age})"

    def getName(self) -> str:
        return self.__name

    def getAge(self) -> int:
        return self.__age

    def to_dict(self) -> Dict[str, Any]:
        return {"name": self.__name, "age": self.__age}
    
