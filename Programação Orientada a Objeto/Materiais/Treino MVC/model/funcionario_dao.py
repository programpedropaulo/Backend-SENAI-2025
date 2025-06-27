import sqlite3

class FuncionarioDAO:
    def __init__(self):
        self.conn = sqlite3.connect("database/funcionarios.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS funcionarios (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nome TEXT NOT NULL,
                            cargo TEXT NOT NULL, 
                            idade INTEGER NOT NULL
                            )
        """)

        self.conn.commit()

    def inserir(self, funcionarios):
        self.cursor.execute(" INSERT INTO funcionarios(nome,cargo,idade) VALUES (?,?,?)",(funcionarios.nome, funcionarios.cargo, funcionarios.idade))

    def listar_todos(self):
        self.cursor.execute("SELECT * FROM funcionarios")
        return self.cursor.fetchall()

