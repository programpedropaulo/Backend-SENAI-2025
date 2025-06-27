import sqlite3

# Criando conexão e cursor
conexao = sqlite3.connect("Cadastro_de_produtos.db")
cursor = conexao.cursor()

# Criando tabela
cursor.execute("""
CREATE TABLE IF NOT EXISTS Cadastro_de_produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    preco REAL NOT NULL
)
""")

# Limpando e reinserindo dados iniciais (opcional)
cursor.execute("DELETE FROM Cadastro_de_produtos")
cursor.executemany("""
INSERT INTO Cadastro_de_produtos (nome, preco) VALUES (?, ?)
""", [
    ('Camiseta', 50.0),
    ('Tenis', 200.0),
    ('Bone', 30.0)
])

conexao.commit()

print("Bem-vindo ao Banco de Dados da Estilo Feito")
nome_usuario = input("Digite seu nome para acessar o sistema: ")

while True:
    comando = input(f"\n{nome_usuario}, digite 'Sair' para encerrar ou 'Confirme' para acessar o menu: ")

    if comando.lower() == "sair":
        print(f"Estamos encerrando o programa. Até logo, {nome_usuario}!")
        break

    elif comando.lower() == "confirme":
        print("\nMenu:")
        print("1 - Adicionar novo produto")
        print("2 - Atualizar produto (nome, preço ou ambos)")
        print("3 - Listar todos os produtos")
        opcao = input("Escolha uma opção (1/2/3): ")

        if opcao == "1":
            nome_produto = input("Nome do produto: ")
            preco_produto = float(input("Preço do produto: "))
            cursor.execute("INSERT INTO Cadastro_de_produtos (nome, preco) VALUES (?, ?)", (nome_produto, preco_produto))
            conexao.commit()
            print("Produto adicionado com sucesso!")

        elif opcao == "2":
            print("\nLista de Produtos:")
            cursor.execute("SELECT * FROM Cadastro_de_produtos")
            produtos = cursor.fetchall()
            for p in produtos:
                print(f"ID: {p[0]} | Produto: {p[1]} | Preço: R${p[2]:.2f}")

            nome_antigo = input("Digite o nome exato do produto que deseja atualizar: ")
            tipo_atualizacao = input("Deseja atualizar 'nome', 'preço' ou 'ambos'? ").lower()

            if tipo_atualizacao == "nome":
                novo_nome = input("Digite o novo nome: ")
                cursor.execute("UPDATE Cadastro_de_produtos SET nome = ? WHERE nome = ?", (novo_nome, nome_antigo))
                conexao.commit()
                print("Nome atualizado com sucesso!")

            elif tipo_atualizacao == "preço" or tipo_atualizacao == "preco":
                novo_preco = float(input("Digite o novo preço: "))
                cursor.execute("UPDATE Cadastro_de_produtos SET preco = ? WHERE nome = ?", (novo_preco, nome_antigo))
                conexao.commit()
                print("Preço atualizado com sucesso!")

            elif tipo_atualizacao == "ambos":
                novo_nome = input("Digite o novo nome: ")
                novo_preco = float(input("Digite o novo preço: "))
                cursor.execute("UPDATE Cadastro_de_produtos SET nome = ?, preco = ? WHERE nome = ?", (novo_nome, novo_preco, nome_antigo))
                conexao.commit()
                print("Nome e preço atualizados com sucesso!")

            else:
                print("Opção inválida para atualização.")

        elif opcao == "3":
            print("\nLista de Produtos:")
            cursor.execute("SELECT * FROM Cadastro_de_produtos")
            produtos = cursor.fetchall()
            for p in produtos:
                print(f"ID: {p[0]} | Produto: {p[1]} | Preço: R${p[2]:.2f}")

        else:
            print("Opção inválida!")

    else:
        print("Comando inválido. Por favor, digite 'Confirme' ou 'Sair'.")

# Fechando conexão
conexao.close()
