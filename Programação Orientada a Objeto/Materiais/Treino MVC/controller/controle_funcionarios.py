from model.funcionario_dao import FuncionarioDAO
from model.funcionario import Funcionario

class ControleFuncionarios:
    def __init__(self):
        self.dao = FuncionarioDAO()

    def inserir(self, nome, cargo, idade):
        funcionario = Funcionario(nome,cargo,idade)
        self.dao.inserir(funcionario)
        return "Funcionario cadastrado"
    
    def lista(self):
        return self.dao.listar_todos()