import sqlite3

#  python -m venv .venv


# Criar tabela de usuários
def criar_tb_usuarios(cursor):
    comando = """
    CREATE TABLE IF NOT EXISTS tb_usuarios(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	email TEXT NOT NULL,
	senha TEXT NOT NULL);
    """
    cursor.execute(comando)


# Criar tabela de perfis de usuarios
def criar_tb_usuarios_perfis(cursor):
    comando = """
    CREATE TABLE IF NOT EXISTS tb_usuarios_perfis(
	id INTEGER PRIMARY KEY,
	nome TEXT NOT NULL,
	sobrenome TEXT NOT NULL,
	idade INTEGER NULL,
	FOREIGN KEY(id) REFERENCES tb_usuarios(id));
    """
    cursor.execute(comando)


# Criar tabela de postagens
def criar_tb_postagens(cursor):
    comando = """
    CREATE TABLE IF NOT EXISTS tb_postagens(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	usuario_id INTEGER NOT NULL,
	titulo TEXT NOT NULL,
	corpo TEXT NOT NULL,
	FOREIGN KEY (usuario_id) REFERENCES tb_usuarios(id));
    """
    cursor.execute(comando)


# Criar tabela de categorias
def criar_tb_categorias(cursor):
    comando = """
    CREATE TABLE IF NOT EXISTS tb_categorias(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	nome TEXT NOT NULL);
    """
    cursor.execute(comando)


# Criar tabela de categorias de postagens
def criar_tb_postagem_categorias(cursor):
    comando = """
    CREATE TABLE IF NOT EXISTS tb_postagens_categorias(
	postagem_id INTEGER NOT NULL,
	categoria_id INTEGER NOT NULL,
	PRIMARY KEY(postagem_id, categoria_id),
	FOREIGN KEY(postagem_id) REFERENCES tb_postagens(id),
	FOREIGN KEY(categoria_id) REFERENCES tb_categorias(id));
    """
    cursor.execute(comando)


if __name__ == "__main__":

    conexao = sqlite3.connect("aula05.sqlite3")
    cursor = conexao.cursor()

    comando = """
    PRAGMA foreign_key = ON;
    """
    cursor.execute(comando)

    criar_tb_usuarios(cursor)
    criar_tb_usuarios_perfis(cursor)
    criar_tb_postagens(cursor)
    criar_tb_categorias(cursor)
    criar_tb_postagem_categorias(cursor)