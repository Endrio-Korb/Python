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


    
    