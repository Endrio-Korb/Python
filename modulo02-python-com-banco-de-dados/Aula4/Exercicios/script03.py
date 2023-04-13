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


# Inserir alunos na tb_alunos
def inserir_tb_alunos(cursor):
    comando = """
    INSERT INTO tb_alunos (id, aluno_id, nome) VALUES
    (1, 1, 'João Silva'),
    (1, 2, 'Ana Santos'),
    (1, 3, 'Carlos Lima')
    """
    cursor.execute(comando)
    conexao.commit()

# Inserir departamento na tb_departamentos
def inserir_tb_departamentos(cursor):
    comando = """
    INSERT INTO tb_departamentos (id, departamento_id, nome) VALUES
    (1, 1, 'Matemática'),
    (1, 2, 'Computação')
    """
    cursor.execute(comando)
    conexao.commit()

# Inserir disciplinas na tb_disciplinas
def inserir_tb_disciplinas(cursor):
    comando = """
    INSERT INTO tb_disciplinas (id, disciplina_id, nome) VALUES
    (1, 1, 'Cálculo I'),
    (1, 2, 'Programação I')
    """
    cursor.execute(comando)
    conexao.commit()

# Inserir professores na tb_professores
def inserir_tb_professores(cursor):
    comando = """
    INSERT INTO tb_professores (id, professor_id, nome) VALUES
    (1, 1, 'Ana Souza'),
    (1, 2, 'Pedro silva')
    """
    cursor.execute(comando)
    conexao.commit()

# Inserir cadastro dos cursos na tb_cursos
def inserir_tb_cursos(cursor):
    comando = """
    INSERT INTO tb_cursos (id, disciplina_id, departamento_id, professor_id, aluno_id, nota) VALUES
    (1, 1, 1, 1, 1, 8),
    (1, 1, 1, 1, 2, 6.5),
    (1, 2, 2, 2, 2, 9),
    (1, 2, 2, 2, 3, 7.5)
    """
    cursor.execute(comando)
    conexao.commit()


# Mostrar tabela de cursos
def mostrar_tb_cursos(cursor):
    comando = """
    SELECT td.nome as "Disiciplinas", tds.nome as "Departamentos",
    tp.nome as "Professores",ta.nome as "Alunos", tc.nota as "Notas"
    FROM tb_cursos tc
    INNER JOIN 
    tb_departamentos tds ON tc.departamento_id = tds.departamento_id,
    tb_disciplinas td ON tc.disciplina_id = td.disciplina_id,
    tb_professores tp ON tc.professor_id = tp.professor_id,
    tb_alunos ta ON tc.aluno_id = ta.aluno_id;
    """
    cursor.execute(comando)
    resultado = cursor.fetchall()
    for item in resultado:
        print(item)


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

    inserir_tb_alunos(cursor)
    inserir_tb_departamentos(cursor)
    inserir_tb_disciplinas(cursor)
    inserir_tb_professores(cursor)
    inserir_tb_cursos(cursor)

    mostrar_tb_cursos(cursor)