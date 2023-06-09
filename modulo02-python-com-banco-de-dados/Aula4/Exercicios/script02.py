import sqlite3


# Cria tabela de disciplinas
def criar_tb_disciplinas(cursor):
    comando = """
    CREATE TABLE IF NOT EXISTS tb_disciplinas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        disciplina_id INTEGER NOT NULL,
        nome TEXT NOT NULL
    );
    """
    cursor.execute(comando)


# Cria tabela de alunos
def criar_tb_alunos(cursor):
    comando = """
    CREATE TABLE IF NOT EXISTS tb_alunos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        aluno_id INTEGER NOT NULL,
        nome TEXT NOT NULL
    );
    """
    cursor.execute(comando)


# Criat tabela de cadastro de alunos
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
        FOREIGN KEY (disciplina_id) REFERENCES tb_disciplinas(disciplina_id),
        FOREIGN KEY (aluno_id) REFERENCES tb_alunos(aluno_id)
    ); 
    """
    cursor.execute(comando)


# Inserir alunos na tabela tb_alunos
def inserir_alunos(cursor):
    comando = """
    INSERT INTO tb_alunos(aluno_id, nome) VALUES
    (1, 'João Silva'),
    (2, 'Maiara Nogueira'),
    (3, 'Danielle Souza'),
    (4,'José Duarte');
    """
    cursor.execute(comando)
    conexao.commit()


# Inserir disciplinas na tabela tb_disciplinas
def inserir_disciplinas(cursor):
    comando = """
    INSERT INTO tb_disciplinas (disciplina_id, nome) VALUES
    (1, 'Estátistica'),
    (2, 'Matemática'),
    (3, 'Java'),
    (4, 'Ciência de Dados')
    """
    cursor.execute(comando)
    conexao.commit()

# Inserir cadastro na tabela tb_cadastro_alunos
def inserir_cadastro(cursor):
    comando = """
    INSERT INTO tb_cadastro_alunos (id, disciplina_id, aluno_id, nota1, nota2, nota3) VALUES
    (1, 1, 1, 8.5, 9, 8.5),
    (1, 2, 2, 10, 9.5, 9.5),
    (1, 3, 3, 7.5, 7.5, 7),
    (1, 4, 4, 6.5, 5.5, 7.5);
    """
    cursor.execute(comando)
    conexao.commit()

# Mostra tabela de cadastro
def mostrar_tb_cadastro_alunos(cursor):
    comando = """
    SELECT ta.nome as "Alunos", td.nome as "Disciplinas",
    tca.nota1 as "Nota 1", tca.nota2 as "Nota 2",
    tca.nota3 as "Nota 3", ( tca.nota1 + tca.nota2 + tca.nota3 ) / 3 as "Média"
    FROM
    tb_cadastro_alunos tca
    INNER JOIN
    tb_disciplinas td ON tca.disciplina_id = td.disciplina_id,
    tb_alunos ta ON tca.aluno_id = ta.aluno_id;
    """
    cursor.execute(comando)
    resultado = cursor.fetchall()
    for item in resultado:
        print(item)


if __name__ == "__main__":

    conexao = sqlite3.connect("cadastroalunos.sqlite3")
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_key = ON;")

    criar_tb_disciplinas(cursor)
    criar_tb_alunos(cursor)
    criar_tb_cadastro_alunos(cursor)

    #inserir_alunos(cursor)
    #inserir_disciplinas(cursor)
    #inserir_cadastro(cursor)

    mostrar_tb_cadastro_alunos(cursor)


    
    