"""EXERCÍCIOS DE SQLite3 2 
Exercício 1 – Cadastro de Veículos 
Crie um banco de dados chamado veiculos.db com uma tabela Veiculos contendo:
id (inteiro, chave primária, autoincremento)
modelo (texto, obrigatório)
marca (texto, obrigatório)
ano (inteiro, obrigatório)

Regras:
O script deve permitir o cadastro de 2 veículos.
Só deve permitir o cadastro se o ano for maior ou igual a 1886 (primeiro automóvel da história).
Se o ano for inválido, mostrar uma mensagem e não salvar.
"""

import sqlite3

# Criando conexão
conexao = sqlite3.connect("Cadastro_de_veiculos.db")
cursor = conexao.cursor()

# Criando tabela
cursor.execute("""
CREATE TABLE IF NOT EXISTS Cadastro_de_veiculos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    modelo TEXT NOT NULL,
    marca TEXT NOT NULL,
    ano INTEGER NOT NULL
)
""")

#variaveis de contole
numero_maximo_de_veiculos = 2
contador_de_veiculos = 0
ano_minimo = 1886

#laço de repetiçâo 
while contador_de_veiculos < numero_maximo_de_veiculos:
        # Inserção de valores      
    modelo = input("Diga-me o modelo do automóvel: ")
    marca = input("Agora, qual marca pertence ao seu automóvel? ")
    ano = int(input("Por fim, o ano de fabricação: "))

    if contador_de_veiculos <= numero_maximo_de_veiculos and ano >= ano_minimo:
        # Executando inserção
        cursor.execute("""
        INSERT INTO Cadastro_de_veiculos (modelo, marca, ano)
        VALUES (?, ?, ?)           
        """, (modelo, marca, ano))

        # Commitando mudanças
        conexao.commit()
        print("Veículo cadastrado com sucesso!")
        contador_de_veiculos +=1
   
    else:
        print("❌ Ano inválido! O primeiro carro foi criado em 1886. Tente novamente.\n")

# Realizando consulta
cursor.execute("SELECT * FROM Cadastro_de_veiculos")
dados = cursor.fetchall()

# Mostrando dados na tela
print("LISTA DE VEICULOS CADASTRADOS: ")
for veiculo in dados:
    print(veiculo)

# Fechando conexão
conexao.close()
