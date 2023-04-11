import sqlite3


# Criar tabela disciplina
def criar_tb_dicisplinas(cursor):
    comando = """
    CREATE TABLE IF NOT EXISTS tb_disciplinas(
        id INTEGER NOT NULL,
        disciplina_id INTEGER NOT NULL,
        nome TEXT NOT NULL,
        PRIMARY KEY (id, disciplina_id)
    );
    """
    cursor.execute(comando)


# Cria tabela departamento
def criar_tb_departamentos(cursor):
    comando = """
    CREATE TABLE IF NOT EXISTS tb_departamentos(
        id INTEGER NOT NULL,
        departamento_id INTEGER NOT NULL,
        nome TEXT NOT NULL,
        PRIMARY KEY(id, departamento_id)
    );
    """
    cursor.execute(comando)

# Criar tabela aluno
def criar_tb_alunos(cursor):
    comando = """
    CREATE TABLE IF NOT EXISTS tb_alunos(
        id INTEGER NOT NULL,
        aluno_id INTEGER NOT NULL,
        nome TEXT NOT NULL,
        PRIMARY KEY (id, aluno_id)
    );
    """
    cursor.execute(comando)

# Criar tabela professores
def criar_tb_professores(cursor):
    comando = """
    CREATE TABLE IF NOT EXISTS tb_professores(
        id INTEGER NOT NULL,
        professor_id INTEGER NOT NULL,
        nome TEXT NOT NULL,
        PRIMARY KEY (id, professor_id)
    );
    """
    cursor.execute(comando)

# Criar tabela de cursos
def criar_tb_cursos(cursor):
    comando = """
    CREATE TABLE IF NOT EXISTS tb_cursos(
        id INTEGER NOT NULL,
        disciplina_id INTEGER NOT NULL,
        departamento_id INTEGER NOT NULL,
        professor_id INTEGER NOT NULL,
        aluno_id INTEGER NOT NULL,
        nota TEXT NOT NULL,
        PRIMARY KEY (id, disciplina_id, professor_id, aluno_id, departamento_id),
        FOREIGN KEY (disciplina_id) REFERENCES tb_disciplinas(disciplina_id),
        FOREIGN KEY (departamento_id) REFERENCES tb_departamentos(departamento_id),
        FOREIGN KEY (professor_id) REFERENCES tb_professores(professor_id),
        FOREIGN KEY (aluno_id) REFERENCES tb_alunos(aluno_id)
    );
    """
    cursor.execute(comando)

if __name__ == "__main__":
    
    conexao = sqlite3.connect("cursos.sqlite3")
    cursor = conexao.cursor()

    comando = "PRAGMA foreign_key = ON;"
    cursor.execute(comando)

    criar_tb_alunos(cursor)
    criar_tb_departamentos(cursor)
    criar_tb_dicisplinas(cursor)
    criar_tb_professores(cursor)
    criar_tb_cursos(cursor)