"""Exercício 2 – Funcionários
CREATE TABLE IF NOT EXISTS Funcionarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    cargo TEXT NOT NULL,
    salario REAL NOT NULL
);

INSERT INTO Funcionarios (nome, cargo, salario) VALUES
('Joao', 'Analista', 3000),
('Maria', 'Gerente', 5000),
('Lucas', 'Estagiario', 1500);

1. Aumente o salário de Maria para 5500.
2. Mude o cargo de Lucas para 'Assistente'."""

import sqlite3

conexao = sqlite3.connect("Funcionarios.db")
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS "Funcionarios.db" (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    cargo TEXT NOT NULL,
    salario REAL NOT NULL)
""")

cursor.execute("""
INSERT INTO  Funcionarios(nome,cargo,salario)
VALUES(?,?,?)   
    ('Joao', 'Analista', 3000),
    ('Maria', 'Gerente', 5000),
    ('Lucas', 'Estagiario', 1500) 
""")
print("Bem vindo ao Banco de dados da CSN")
while True:
    comando = input("❌ Caso queira sair digite 'sair' ou ✅ 'ficar' para continuar \n Sua resposta: " )
    if comando.lower() == "sair":
        print("Estamos encerrando o programa, aguardamos sua proxima visita! \nTenha um bom dia!")
        break
    if comando.lower() == "ficar":
        print("continuando...")

    cursor.execute("UPDATE Funcionarios SET salario = 5000.00 WHERE nome = 'Maria'")
    cursor.execute("UPDATE Funcionarios SET cargo  = 'Assistente' WHERE nome = 'Lucas'")
    conexao.commit()
    cursor.eecute("SELECT * FROM Funcionarios")
    dados =  cursor.fetchall()
    print("\nTabela dos funcionarios da CSN atualizada! ")
    for funcionario in dados:
        print(f"ID: {funcionario[0]} | nome: {funcionario[1]} | cargo: {funcionario[2]} | salario: {funcionario[3]:.2f}")
    conexao.close

else:
    print("Você digitou um comando invalido \n Tente novamente!")