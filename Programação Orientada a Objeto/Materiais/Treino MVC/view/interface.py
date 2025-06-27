from controller.controle_funcionarios import ControleFuncionarios

class Interface:
    def __init__(self):
        self.controle = ControleFuncionarios()

        while True:
            print("Opção 1 - Inserir")
            print("Opção 2 - Listar")
            print("Opção 3 - Fechar")
            opcao =int(input())

            if opcao == 1:
                self.inserir_interface()
            elif opcao == 2:
                self.lista_interface()
            elif opcao == 3:
                break
            else: 
                print("Opcao invalida")

    def inserir_interface(self):
            nome = input("Insira o nome")
            cargo = input("Insira o cargo")
            idade = int(input("Insira a idade"))
            self.controle.inserir(nome, cargo, idade)
        
    def lista_interface(self):
            print(self.controle.lista())
