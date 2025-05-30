
import sqlite3

#criando conexao
conexao = sqlite3.connect("Cadastro_de_livros.db")
cursor = conexao.cursor()

#CRIANDO TABELA
cursor.execute("""
CREATE TABLE IF NOT EXISTS cadastro_de_livros(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    autor TEXT NOT NULL,
    ano_de_publicacao REAL NOT NULL
    )
""")

#inserçâo de dados na tabela
titulo = input("titiulo do livro: ")
autor = input("Quem escreveu o livro? ")
ano_de_publicacao = input("ano de publicaçâo: ")

cursor.execute("""
INSERT INTO Cadastro_de_livros
    (titulo, autor, ano_de_publicacao)
    VALUES (?,?,?)
""",(titulo, autor, ano_de_publicacao))

#dando commit nas mudanças
conexao.commit()
print("Livro cadastrado com sucesso! ")

#Realizando consultas
cursor.execute("SELECT * FROM Cadastro_de_livros")
dados = cursor.fetchall()

for livros in dados:
    print(livros)

#Fechando a conexão 
conexao.close()