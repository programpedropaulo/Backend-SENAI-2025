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
cursor = conexao.cursor()

#criando tabela
cursor.execute("""
CREATE TABLE IF NOT EXISTS Cadastro_de_produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    preco REAL NOT NULL
) """)

#inserindo valores na tabela
cursor.execute("""
INSERT INTO Cadastro_de_produtos(nome,preco)
VALUES 
    ('Camiseta', 50.0),
    ('Tenis', 200.0),
    ('Bone', 30.0)
""")
#variaveis de controle

#criando laço de repetição
print("Bem vindo ao Banco de dados da Estilo Feito")
while True:
    comando = input("❌ Caso queira sair digite 'sair' ou ✅ 'ficar' para continuar \n Sua resposta: " )
    if comando.lower() == "sair":
        print("Estamos encerrando o programa, aguardamos sua proxima visita! \nTenha um bom dia!")
        break
    if comando.lower() == "ficar":
        print("continuando...")

                #inserção de valores e atualização de valores
        cursor.execute("UPDATE Cadastro_de_produtos SET preco = 180.0 WHERE nome = 'Tenis'")
        cursor.execute("UPDATE Cadastro_de_produtos SET preco = 60.0 WHERE nome = 'Camiseta'")
        #execultando inserção
                
        #commitando as mudanças
        conexao.commit()
       
        #realizando consulta 
        cursor.execute ("SELECT * FROM Cadastro_de_produtos")
        dados = cursor.fetchall()

        #mostrando na tela
        print("\n🛍️ Loja Estilo Feito - Produtos atualizados:")
        for produto in dados:
            print(f"ID: {produto[0]} | Produto: {produto[1]} | Preço: R${produto[2]:.2f}")


        #fechando conexão
        conexao.close

    else:
        print("Você digitou um comando invalido \n Tente novamente!")
