import sqlite3
conexao = sqlite3.connect("akuarios.db")
cursor = conexao.cursor()
laco_de_repeticao = True

cursor.execute("""
CREATE TABLE IF NOT EXISTS akuarios(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    estoque INTEGER NOT NULL,
    preco REAL NOT NULL
                    
    )
""")
print("cadastre o um produto")
while laco_de_repeticao == True:
    nome = input("digite o nome do produto:")
    estoque = int(input("digite o estoque do produto:"))
    preco = float(input("digite o preco do produto:"))
        
        
    cursor.execute("""
    INSERT INTO akuarios(nome,estoque,preco) VALUES(?,?,?)
    """,(nome,estoque,preco))
    conexao.commit()
    print("produto cadastrado com sucesso")
    print("deseja sair do cadastro do produto")
    escolha = input("digite sim ou nao")
    if(escolha == "sim" or escolha == "SIM"):
        laco_de_repeticao = False
            
print("deseja ver os produtos:")
cursor.execute("SELECT * FROM loja")
dados = cursor.fetchall()
for akuario in dados:
    print(akuario)

print("deseja mudar um valor:")
id_1 = input("digite o id do produto que voce deseja mudar:")
print("o que voce deseja mudar:")
print("1 para nome")
print("2 para estoque")
print("3 para preco")
opcao = int(input("digite o numero: "))
if(opcao == 1):
    mudar_o_nome = input("digite o novo nome do produto:")
    cursor.execute("UPDATE loja SET nome = ?  WHERE id = ?", (mudar_o_nome,id_1))
    print("nome modificado")
elif(opcao == 2):
    mudar_o_estoque = int(input("digite o novo valor de estoque:"))
    cursor.execute("UPDATE loja SET estoque = ?  WHERE id = ?", (mudar_o_estoque,id_1))
    print("estoque modificado")
elif(opcao == 3):
    mudar_o_preco = float(input("digite o novo preco:"))
    id_1))
    print("preco modificado")
else:
    print("valor invalido")

print("deseja apagar alguma tabela:")

    id_2 = int(input("digite o id do produto que voce deseja apagar:"))
    cursor.execute("DELETE FROM loja WHERE id = ? ",(id_2,))


print("deseja procurar alguma tabela:")

    print("como deseja buscar por id ou nome:")
    print("1 para id")
    print("2 para nome")
    procura = int(input("digite a escolha:"))
if(procura == 1):
    id_3 = int(input("digite o id que deverar ser procurado:"))
    cursor.execute("SELECT * FROM loja WHERE id = ?", (id_3,))

elif(procura == 2):
    nome_de_busca = input("o que voce esta procurando?:")
    cursor.execute("SELECT * FROM loja WHERE nome = ?", (nome_de_busca,))

 else:
    print("valor invalido")


print("deseja ver os produtos novamente:")
cursor.execute("SELECT * FROM loja")
dados = cursor.fetchall()
for loja in dados:
    print(loja)

conexao.close