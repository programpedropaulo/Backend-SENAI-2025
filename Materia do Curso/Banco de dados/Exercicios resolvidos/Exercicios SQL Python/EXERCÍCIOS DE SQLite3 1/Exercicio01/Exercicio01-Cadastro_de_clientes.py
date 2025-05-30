import sqlite3

# CRIANDO CONEXÃO
conexao = sqlite3.connect("cadastro_de_clientes.db")
cursor = conexao.cursor()

# CRIANDO TABELA
cursor.execute(""" 
CREATE TABLE IF NOT EXISTS Cadastro_de_clientes(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    email TEXT,
    idade REAL        
)
""")

# INSERÇÃO DE DADOS NA TABELA
nome = input("Por favor, digite seu nome: ")
email = input("Agora vamos para seu email, por favor digite-o: ")
idade = input("Por fim, me diga sua idade: ")

cursor.execute(""" 
INSERT INTO Cadastro_de_clientes(nome, email, idade)
VALUES (?, ?, ?)
""", (nome, email, idade))

# DANDO COMMIT NAS MUDANÇAS
conexao.commit()
print("Cliente cadastrado com sucesso!")

# REALIZANDO CONSULTA
cursor.execute("SELECT * FROM Cadastro_de_clientes")
dados = cursor.fetchall()

for cliente in dados:  # <-- variável corrigida aqui
    print(cliente)

# FECHANDO CONEXÃO
conexao.close()
