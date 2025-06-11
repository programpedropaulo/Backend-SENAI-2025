import sqlite3

class produto_dao:
    def __init__(self):
        self.conexao = sqlite3.connect("database/produto.db")
        self.cursor = self.conexao.cursor()
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS produtos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            quantidade INTEGER NOT NULL,
            preco REAL NOT NULL
                                 
                )
        """)
        self.conexao.commit()

    def cadastrar_produto(self,produtos):
        self.cursor.execute("""INSERT INTO produtos(nome, quantidade, preco) VALUES(?,?,?)""",(produtos.nome, produtos.quantidade, produtos.preco))
    
    def ver_produtos(self):
        self.cursor.execute("""SELECT * FROM produtos""")
        return self.cursor.fetchall()

    def trocar_quantidade(self,id_1,quantidade_mud):
        self.cursor.execute("""UPDATE produtos SET quantidade = ? WHERE id = ? """,(id_1, quantidade_mud))
    
    def trocar_preco(self,preco_mud,id_1):
        self.cursor.execute("""UPDATE produtos SET preco = ? WHERE id""",(preco_mud, id_1))
    
    def excluir_produto(self,id_2):
        self.cursor.execute("""DELETE FROM produtos WHERE id = ? """,(id_2,))

    def consultar_nome(self,nome_mud):
        self.cursor.execute("""SELECT * FROM produtos WHERE nome = ?""",(nome_mud))
    
    def consultar_id(self,id_3):
        self.cursor.execute("""SELECT * FROM produtos WHERE id = ?""",(id_3,))

    def valor_total(self):
        self.cursor.execute("""SELECT quantidade * preco from produtos""")
