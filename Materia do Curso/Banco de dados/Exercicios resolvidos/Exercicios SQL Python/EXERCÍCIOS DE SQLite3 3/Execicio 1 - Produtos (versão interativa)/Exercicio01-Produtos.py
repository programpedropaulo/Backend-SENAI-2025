"""
EXERCÍCIOS DE SQLite3 3

EXERCÍCIOS DE UPDATE

Exercício 1 – Produtos
1. Atualize o preço do Tênis para 180.0.
2. Aumente o preço da Camiseta em 10 reais.
""" 

#importando biblioteca
import sqlite3

#criando conexao e definindo função
conexao = sqlite3.connect("Cadastro_de_produtos.db")

#criando tabela
cursor.execute("""
CREATE TABLE IF NOT EXISTS Produtos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL
    preco REAL NOT NULL
): """)

#inserindo valores na tabela
INSERT INTO Produtos(nome,preco)
VALUES 
    ('Camiseta', 50.0),
    ('Tenis', 200.0),
    ('Bone', 30.0);


#variaveis de controle

#criando laço de repetição
print("Bem vindo ao Banco de dados da Estilo Feito")
nome =  input("Por favor digite seu nome para ter acesso ao banco de dados: ")
while True:
    comando = input("caso queira sair digite 'Sair'")
    if comando.lower() == "Sair":
        print("Estamos encerrando o programa, aguardamos sua proxima visita! \n Tenha um bom dia.")
        break
    else:
        print("Você digitou um comadno invalido \n Tente novamente!")
#inserção de valores e atualização de valores


#execcultadondo inserção

#commitando as mudanças

#realizando consulta 

#mostrando na tela

#fechando conexão

