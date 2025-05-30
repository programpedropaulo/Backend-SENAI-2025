import sqlite3

#criando conexao
conexao = sqlite3.connect("Cadastro_de_produtos.db")
cursor = conexao.cursor()

# Criando tabela
cursor.execute("""
CREATE TABLE IF NOT EXISTS Cadastro_de_produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    preco REAL NOT NULL,
    estoque INTEGER NOT NULL
)
""")

#INSERINDO OS DADOS NA TABELA
nome = input ("diga me o nome do produto: ")
preco = float(input("agora me informe seu valor por favor: "))
estoque = int(input ("Quantos itens tem disponivel no estoque? "))

cursor.execute("""
INSERT INTO Cadastro_de_produtos (nome, preco, estoque)
VALUES (?,?,?)             
""",(nome, preco , estoque))

#dando commit nas mudanças
conexao.commit()
print("Produto cadastrado com sucesso!")

#realizando consultas
cursor.execute("SELECT * FROM Cadastro_de_produtos")
dados = cursor.fetchall()

for produtos in dados:
    print(produtos)

#fechado conexao
conexao.close()