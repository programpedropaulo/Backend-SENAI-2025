"""
Exercício 2 – Cadastro de Contas Bancárias
Crie um banco de dados chamado banco.db com uma tabela Contas contendo:
id (inteiro, chave primária, autoincremento)
titular (texto, obrigatório)
agencia (texto, obrigatório)
saldo (real, obrigatório)


Regras:
O script deve permitir o cadastro de 3 contas.
Só deve permitir cadastro se o saldo inicial for maior ou igual a 0.
Se o saldo for negativo, mostrar erro e não salvar.

"""

import sqlite3

#criando conexao e definindo função
conexao = sqlite3.connect("Cadastro_de_contas_bancarias.db")
cursor = conexao.cursor()

#crianndo banco de dados
cursor.execute("""
CREATE TABLE IF NOT EXISTS Cadastro_de_contas_bancarias(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titular TEXT NOT NULL,
    agencia TEXT NOT NULL,
    saldo REAL NOT NULL
)
""")

#variaveis de controle
numero_de_contas = 0
numero_maximo_de_contas = 3


#criando laço de repeticao
#inserção de valores
while numero_de_contas < numero_maximo_de_contas:

    titular = input("Para começarmos, por favor digite seu nome: ")
    print(f"Muito prazer em te conhecer, {titular}!")

    agencia = input(f"Agora {titular}, precisamos saber sua agência: ")
    
    try:
        saldo = float(input("Por fim, o saldo que deseja depositar:\n(Lembrando que se o saldo for inferior a 0, sua conta não poderá ser criada!)\n>>> "))
    except ValueError:
        print("❌ Por favor, digite um número válido para o saldo.")
        continue

    if saldo >= 0:
        print(f"✅ Conta criada com sucesso!\nTitular: {titular} | Agência: {agencia} | Saldo: R${saldo:.2f}\n")
        numero_de_contas += 1

    else:
        print("❌ Saldo inválido. A conta não foi criada.\n")

    #Executadndo inserção
    cursor.execute("""
    INSERT INTO Cadastro_de_contas_bancarias(titular, agencia, saldo)
    VALUES (?,?,?)               
    """,(titular, agencia, saldo))

    #commitadno mudanças
    conexao.commit()
    print("Conta bancaria cadastrada com sucesso! ")
   


#realizando consulta
cursor.execute ("SELECT * FROM Cadastro_de_contas_bancarias")
dados = cursor.fetchall()

#mostando dados na tela
print("Mostrano as contas cadastradas: ")
for contas in dados:
    print (contas)
#fechando a conexao
conexao.close
