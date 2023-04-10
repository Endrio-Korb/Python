import sqlite3


# Cria tabela de disciplinas
def criar_tb_disciplinas(cursor):
    comando = """
    CREATE TABLE IF NOT EXISTS tb_disciplinas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL
    );
    """
    cursor.execute(comando)

# Cria tabela de alunos
def criar_tb_alunos(cursor):
    comando = """
    CREATE TABLE IF NOT EXISTS tb_alunos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL
    );
    """
    cursor.execute(comando)

def criar_tb_cadastro_alunos(cursor):
    comando = """
    CREATE TABLE IF NOT EXISTS tb_cadastro_alunos(
        id INTEGER NOT NULL,
        disciplina_id INTEGER NOT NULL,
        aluno_id INTEGER NOT NULL,
        nota1 TEXT NOT NULL,
        nota2 TEXT NOT NULL,
        nota3 TEXT NOT NULL,
        PRIMARY KEY (id, disciplina_id, aluno_id),
        FOREIGN KEY (disciplina_id) REFERENCES tb_disciplinas(id),
        FOREIGN KEY (aluno_id) REFERENCES tb_alunos(id)
    ); 
    """
    cursor.execute(comando)


if __name__ == "__main__":

    conexao = sqlite3.connect("cadastroalunos.sqlite3")
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_key = ON;")

    criar_tb_disciplinas(cursor)
    criar_tb_alunos(cursor)
    criar_tb_cadastro_alunos(cursor)
