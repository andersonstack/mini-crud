from os import system
from src.controller.student_register import StudentRegister

class StudentView:
    @staticmethod
    def screenOptions() -> None:
        print("Escolha uma opção:")
        print("1 - Cadastrar aluno")
        print("2 - Remover aluno")
        print("3 - Visualizar alunos")
        print("4 - Atualizar aluno")
        print("0 - Sair")
    
    @staticmethod
    def screenMessage(message: str) -> None:
        print(f"{message} \nEnter para continuar...")
        input("")

    @staticmethod
    def clearScreen() -> None:
        system("cls || clear")

    @staticmethod
    def screenRegister() -> None:
        try:
            register = StudentRegister().getRegister()
            if register is not None:
                print("|---------------------------------------------------------------------------|")
                for key, value in register.items():
                    print(f"\t#ID: {key} - #Nome: {value.getName()} - #Idade: {value.getAge()} anos \n")
                print("|---------------------------------------------------------------------------|")
            StudentView.screenMessage("Alunos carregados com sucesso!")
        except:
            StudentView.screenMessage("Alunos não encontrados!")
            return None