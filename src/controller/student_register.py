from typing import Dict
from json import dumps, loads
from src.models.Student import Student
from random import randint

class StudentRegister:
    __register: Dict[int, Student] = {}

    def register(self, name: str, age: int) -> None:
        userId: int = randint(0, 9999)
        student: Student = Student(name, age)
        self.__register[userId] = student

        self.__openFile()
        self.__register[userId] = student
        self.__updateFile()

    def getRegister(self) -> Dict[int, Student] | None:
        try:
            self.__openFile()
            return self.__register
        except:
            return None
    
    def removeUse(self, userId: int) -> bool:
        try:
            self.__openFile()
            del self.__register[userId]
            self.__updateFile() 
            return True
        except:
            return False
        
    def updateUser(self, userId: int, name: str, age: int) -> None:
        self.__openFile()
        self.__register[userId] = Student(name, age)
        self.__updateFile()
    
    def __openFile(self) -> None:
        with open("./src/json/register.json", "r") as file:
            data = loads(file.read())
            self.__register = {
                int(userId): Student(**studentData) for userId, studentData in data.items()
            }
    
    def __updateFile(self) -> None:
        with open("./src/json/register.json", "w") as file:
            file.write(dumps({userId: student.to_dict() for userId, student in self.__register.items()}))