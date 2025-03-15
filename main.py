from src.controller.student_register import StudentRegister # type: ignore
from src.enums.options import Options
from src.view.student_view import StudentView

option: str = Options.START.value

while Options(option) != Options.EXIT:
    StudentView.screenOptions()
    option = input("Opção: ")

    match Options(option):
        case Options.REGISTER:
            name: str = input("Nome: ") 
            age: int = int(input("Idade: "))
            StudentRegister().register(name, age)
            StudentView.screenMessage("Aluno cadastrado com sucesso!")

        case Options.REMOVE:
            userId: int = int(input("Id: "))
            if StudentRegister().removeUse(userId):
                StudentView.screenMessage("Aluno removido com sucesso!")
            else:
                StudentView.screenMessage("Aluno não encontrado!")
        
        case Options.VIEW:
            StudentView.screenRegister()
        
        case Options.UPDATE:
            userId: int = int(input("Id: "))
            name: str = input("Nome: ") 
            age: int = int(input("Idade: "))
            StudentRegister().updateUser(userId, name, age)
            StudentView.screenMessage("Aluno atualizado com sucesso!")

        case Options.EXIT:
            print("Saindo...")
            break
        case _:
            StudentView.screenMessage("Opção não encontrada!")

    StudentView.clearScreen()