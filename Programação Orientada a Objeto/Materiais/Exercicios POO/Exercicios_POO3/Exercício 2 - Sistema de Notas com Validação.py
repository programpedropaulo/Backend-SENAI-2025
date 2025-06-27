# Definindo a classe Aluno
class Aluno:
    # Método construtor: é chamado automaticamente quando criamos um novo aluno
    def __init__(self, nome, nota): 
        self.__nome = nome  # Atributo privado para armazenar o nome do aluno
        self.__nota = nota  # Atributo privado para armazenar a nota do aluno

    # Método getter: retorna a nota atual do aluno
    def get_nota(self):
        return self.__nota

    # Método setter: atualiza a nota, com validação para garantir que esteja entre 0 e 10
    def set_nota(self, nota_nova):
        if 0 <= nota_nova <= 10:
            self.__nota = nota_nova  # Atualiza a nota se for válida
        else: 
            print("Nota inválida. Insira um valor entre 0 e 10.")  # Exibe erro se for inválida

    # Método para verificar se o aluno está aprovado (nota >= 6)
    def aprovado(self):
        return self.__nota >= 6  # Retorna True se a nota for 6 ou mais, senão False


# ---------- TESTES DO PROGRAMA ----------

# Criando um objeto da classe Aluno
aluno1 = Aluno("Lino", 8)

# Exibindo a nota inicial do aluno
print(aluno1.get_nota())   # Saída esperada: 8

# Alterando a nota para um valor válido
aluno1.set_nota(9.5)
print(aluno1.get_nota())   # Saída esperada: 9.5

# Tentando alterar para uma nota inválida (acima de 10)
aluno1.set_nota(15)        # Saída esperada: mensagem de erro
print(aluno1.get_nota())   # Saída esperada: continua 9.5

# Verificando se o aluno está aprovado
if aluno1.aprovado():
    print("Aprovado!")     # Saída esperada: Aprovado!
else:
    print("Reprovado!")
